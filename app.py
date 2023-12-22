from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
import inotify.adapters
from flask import jsonify
import os   
import mysql.connector

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)



r = redis.Redis(
    host='localhost',
    port=6379,
)


data2 = ("static/tmp//frame0.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "87.5398", "static/tmp//frame1.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "87.5398", "static/tmp//frame10.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "87.012", "static/tmp//frame2.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "87.5398", "static/tmp//frame3.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "87.084", "static/tmp//frame4.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "86.6608", "static/tmp//frame5.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "86.811", "static/tmp//frame6.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "85.9441", "static/tmp//frame7.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "84.573", "static/tmp//frame8.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "84.5297", "static/tmp//frame9.jpg", "plate0:", "1", "results", "-", "GL19TNJ", "confidence:", "86.1544")


 
def alpr_from_img():
    result_stdout = os.popen('./scripts/monit.sh').read()
    s = result_stdout.split()
    r.set('key', 'value')
    r.set('foo', 'bar')
    print((s))

def get_images():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/images/')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        print("http://localhost:5000/images/{}\n\n".format(filename))
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
def alpr_from_video():
    alpr_from_img()
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