from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
import inotify.adapters
from flask import jsonify
import os   
from time import time
from redis.exceptions import ConnectionError, DataError, NoScriptError, RedisError, ResponseError
import cv2

UPLOAD_FOLDER = './static/upload'
ALLOWED_EXTENSIONS = {'mp4', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__, static_folder='static', static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)
r = redis.Redis(
    host='localhost',
    port=6379,
)
redis_host = "redis"
stream_key = "alpr"


               

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def alpr_from_img():
    result_stdout = os.popen('./scripts/monit.sh').read()
    stdout_list = result_stdout.split()
    l2=stdout_list[::2]
    l3=stdout_list[1::2]
    for f, b in zip(l2, l3):
        r.xadd( stream_key, { f: b} )

def get_images_alprd():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/images/')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        #print("http://localhost:5000/images/{}\n\n".format(filename))
        #r.publish("bigboxcode","http://localhost:5000/images/{}\n".format (filename))
        alpr_images = {"img": "http://localhost:5000/images/{}\n".format(filename)}
        r.publish("alprdata", json.dumps((alpr_images)))
        r.publish("bigboxcode", json.dumps((alpr_images)))
        return ("alprd", json.dumps("http://localhost:5000/images/{}\n".format(filename)))

@app.route('/alprd', methods=["POST"])
def alpr_from_video():
    get_images_alprd()
    try:
        data = json.loads(request.data)
        r.publish("alprdata", json.dumps(data))
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

@app.route("/data", methods=["GET"])
def alprd_db():
    def alpr_sse():
        pubsub = r.pubsub()
        pubsub.subscribe("alprdata")
        for message in pubsub.listen():
           data2 = message["data"]
           print((data2))
    return Response(alpr_sse(), mimetype="text/event-stream")  



@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename('alprVideo.mp4')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@app.route("/video")
def video():
    return send_file("./static/upload/alprVideo.mp4")


@app.route("/test") 
def test():
    return("test")    