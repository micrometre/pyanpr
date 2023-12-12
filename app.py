# flask_sse.py
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
from inotify_simple import INotify, flags
import inotify.adapters


app = Flask(__name__, static_folder='static', static_url_path='')

CORS(app)
r = redis.Redis(
    host='localhost',
    port=6379,
)

def get_images():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/images')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        print("http://localhost:5000/images/{}\n\n".format(filename))
        r.publish("bigboxcode", (filename))
        return ("http://localhost:5000/images/{}\n\n".format(filename))


@app.route('/alprd', methods=["POST"])
def publish():
    get_images()
    try:
        data = json.loads(request.data)
        r.publish("alprd", json.dumps(data))
        return jsonify(status="success", message="published", data=data)
    except:
        return jsonify(status="fail", message="not published")

@app.route("/images", methods=["GET"])
def alpr_images():
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

        
@app.route('/alprdsse', methods=["GET"])
def sse():
    def sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("alprd")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data, 'utf-8'))
            except:
                pass
    return Response(sse_events(), mimetype="text/event-stream")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/video")
def video():
    return send_file("./public/upload/alprVideo.mp4")
if __name__ == "__main__":
     app.run(debug=True)   