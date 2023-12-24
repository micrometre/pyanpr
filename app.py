from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
import inotify.adapters
from flask import jsonify
import os   
import time
from time import time
from redis.exceptions import ConnectionError, DataError, NoScriptError, RedisError, ResponseError
import cv2
app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)



r = redis.Redis(
    host='localhost',
    port=6379,
)
redis_host = "redis"
stream_key = "skey"
stream2_key = "alpr"
group1 = "grp1"
group2 = "grp2"


 
def alpr_from_img():
    result_stdout = os.popen('./scripts/monit.sh').read()
    stdout_list = result_stdout.split()
    l2=stdout_list[::2]
    l3=stdout_list[1::2]
    z=zip(l2,l3)
    stdout_dictionary_sorted = (dict(z))
    stdout_dictionary_json  = json.dumps(stdout_dictionary_sorted)
    foo = ["res","ttt"]
    bar = ["ser","ooo"]
    for f, b in zip(l2, l3):
        print(f, b)
        r.xadd( stream_key, { f: b} )
        #print( f"stream length: {r.xlen( stream_key )}")
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

@app.route('/alprd', methods=["POST"])
def alpr_from_video():
    alpr_from_img()
    try:
        data = json.loads(request.data)
        r.publish("alprd", json.dumps(data))
        return jsonify(status="success", message="published", data=data)
    except:
        return jsonify(status="fail", message="not published")
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