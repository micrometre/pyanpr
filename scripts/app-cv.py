# flask_sse.py
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
import inotify.adapters
from os import path, walk
from flask import jsonify
import cv2



app = Flask(__name__, static_folder='static', static_url_path='')


CORS(app)
r = redis.Redis(
    host='localhost',
    port=6379,
)


def get_images():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/images/')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        #print("http://localhost:5000/images/{}\n\n".format(filename))
        #r.publish("bigboxcode","http://localhost:5000/images/{}\n".format (filename))
        alpr_images = {"img": "http://localhost:5000/images/{}\n".format(filename)}
        r.publish("bigboxcode", json.dumps((alpr_images)))
        return ("alprd", json.dumps("http://localhost:5000/images/{}\n".format(filename)))



@app.route("/images", methods=["GET"])
def alprd_images():
    def alpr_sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("bigboxcode")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data, 'utf-8'))
            except:
                pass
    return Response(alpr_sse_events(), mimetype="text/event-stream")  

@app.route('/alprd', methods=["POST"])
def publish():
    get_images()
    vidcap = cv2.VideoCapture('./static/upload/alprVideo.mp4')
    success,image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite("./alpr-images/frame%d.jpg" % count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1
    try:
        data = json.loads(request.data)
        r.publish("alprd", json.dumps(data))
        return jsonify(status="success", message="published", data=data)
    except:
        return jsonify(status="fail", message="not published")
        
@app.route('/alprdsse', methods=["GET"])
def sse():
    def sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("alprd")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data, 'utf-8'))
                #yield "data: {}\n\n".format(str(data, 'utf-8'))
            except:
                pass
    return Response(sse_events(), mimetype="text/event-stream")

@app.route("/video")
def video():
    return send_file("./static/upload/alprVideo.mp4")
@app.route('/')
def hello():
    return render_template('index.html')     
if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )