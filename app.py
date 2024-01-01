from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
import inotify.adapters
import os   
from time import time
from redis.exceptions import ConnectionError, DataError, NoScriptError, RedisError, ResponseError
import mysql.connector
import json
import logging
import pandas as pd
UPLOAD_FOLDER = './static/upload'
ALLOWED_EXTENSIONS = {'mp4', 'png', 'jpg', 'jpeg', 'gif'}
logging.getLogger('flask_cors').level = logging.DEBUG

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


alprdb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="395F844E696D423F6B7ACBBA301539668E6",
  port= 3306,
  database="alprdata"
)

alprdbcamera = mysql.connector.connect(
  host="localhost",
  port= 3307,
  user="root",
  password="395F844E696D423F6B7ACBBA301539668E6",
  database="cameradata"
)

r = redis.Redis(
    host='localhost',
    port=6379,
)
redis_host = "redis"
stream_key = "alpr"

               

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_images_alprd():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/images/')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        alpr_images = {"img": "http://172.187.216.226:5000/images/{}\n".format(filename)}
        r.publish("bigboxcode", json.dumps((alpr_images)))
        return ("alprd", json.dumps("http://localhost:5000/images/{}\n".format(filename)))


def get_images_camera():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/camera-images/')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        alpr_images = {"img": "http://172.187.216.226:5000/camera-images/{}\n".format(filename)}
        r.publish("cameraimg", json.dumps((alpr_images)))
        return ("cameraimg", json.dumps("http://localhost:5000/camera-images/{}\n".format(filename)))

@app.route('/alprd', methods=["POST"])
def alpr_from_video():
    request_data = request.get_json()
    alpr_results = request_data["results"]
    alpr_uuid = request_data["uuid"]
    alpr_plate = alpr_results[0]["plate"]
    alpr_img = get_images_alprd()
    alpr_img_plate = alpr_img[1]
    alprcursor = alprdb.cursor()
    alprcursor.execute("CREATE DATABASE IF NOT EXISTS alprdata;")
    alprcursor.execute("CREATE TABLE  IF NOT EXISTS  plates (uuid TEXT, plate TEXT, img TEXT );")
    sql = "INSERT INTO plates (uuid, plate, img) VALUES (%s, %s, %s)"
    val = (alpr_uuid, alpr_plate, alpr_img_plate)
    alprcursor.execute(sql,val)
    alprdb.commit()
    print(alpr_img_plate)
    try:
        data = json.loads(request.data)
        r.publish("alprd", json.dumps(data))
        return jsonify(status="success", message="published", data=data)
    except:
        return jsonify(status="fail", message="not published")
@app.route('/camera', methods=["POST"])
def alpr_camera():
    request_data = request.get_json()
    camera_results = request_data["results"]
    camera_uuid = request_data["uuid"]
    camera_plate = camera_results[0]["plate"]
    camera_img = get_images_camera()
    camera_img_plate = camera_img[1]
    cameracursor = alprdbcamera.cursor()
    cameracursor.execute("CREATE DATABASE IF NOT EXISTS cameradata;")
    cameracursor.execute("CREATE TABLE  IF NOT EXISTS  camera (uuid TEXT, plate TEXT, img TEXT );")    
    sql = "INSERT INTO camera (uuid, plate, img) VALUES (%s, %s, %s)"
    val = (camera_uuid, camera_plate, camera_img_plate)
    cameracursor.execute(sql,val)
    alprdbcamera.commit()
    print(cameracursor)
    try:
        data = json.loads(request.data)
        r.publish("camera", json.dumps(data))
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

@app.route('/camerasse', methods=["GET"])
def camera_sse():
    def sse_events_camera():
        pubsub = r.pubsub()
        pubsub.subscribe("camera")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data, 'utf-8'))
            except:
                pass
    return Response(sse_events_camera(), mimetype="text/event-stream")
@app.route("/cameraimg", methods=["GET"])
def alprd_camera_images():
    def alpr_camera_sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("cameraimg")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data, 'utf-8'))
            except:
                pass
    return Response(alpr_camera_sse_events(), mimetype="text/event-stream")  

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

@app.route("/") 
def home():
    return render_template('index.html')      

if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )
