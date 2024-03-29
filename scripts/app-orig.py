import os
from flask import Flask, flash, request, json, jsonify, redirect, url_for, send_file, render_template, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename
import redis
import inotify.adapters
import logging
import subprocess
import pandas as pd
import cv2



UPLOAD_FOLDER = './static/upload'
ALLOWED_EXTENSIONS = {'mp4', 'png', 'jpg', 'jpeg', 'gif'}
logging.getLogger('flask_cors').level = logging.DEBUG
app = Flask(__name__, static_folder='static', static_url_path='')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True,
)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_images_alprd():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/images/')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        alpr_images_sse = ("http://127.0.0.1:5000/images/{}".format(filename))
        r.publish("alprdimages", json.dumps((alpr_images_sse)))
        return ("alprd-upload", json.dumps("http://127.0.0.1:5000/images/{}".format(filename)))
        
def get_camera_alprd_images():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/camera-images/')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        alpr_images_sse = ("http://127.0.0.1:5000/camera-images/{}".format(filename))
        print(alpr_images_sse)
        r.publish("alprdcameraimages", json.dumps((alpr_images_sse)))
        return ("alprd-camera", json.dumps("http://127.0.0.1:5000/camera-images/{}".format(filename)))




@app.route('/check_key', methods=['GET'])
def check_key():
    key = request.args.get('key')  # Retrieve key from request arguments
    field = request.args.get('field')  # Retrieve field from request arguments
    get_plate = r.hget(key, field)  # Check if the field exists in the hash
    plate = format(get_plate)
    get_image = r.hget("alpr_plate_to_img", get_plate)  # Check if the field exists in the hash
    img = format(get_image)
    print((get_image))
    data = [plate, img]
    return jsonify(status="success", data=data)


@app.route("/alprdb", methods=["GET"])
def list_items():
    stored_alpr  = r.hgetall(
        "alpr_plate_to_img"
        )
    res = format(stored_alpr)    
    res_values = []
    for x in stored_alpr:
        res_values.append(x)
    return(res)

@app.route("/uploaddb", methods=["GET"])
def alpr_result():
        res = r.hgetall("upload_plate_to_img")
        resj = format(res)
        print(type(res))
        return(resj)


@app.route('/camera', methods=["POST"])
def alpr_from_camera():
    get_camera_alprd_images()
    request_data = request.get_json()
    alpr_camera_results = request_data["results"]
    alpr_camera_plate = alpr_camera_results[0]["plate"]
    alpr_camera_img = get_camera_alprd_images()
    alpr_camera_img_plate = alpr_camera_img[1]
    print(alpr_camera_img_plate)
    try:
        data = alpr_camera_plate
        r.hset(
            f"alpr_camera_plate:{alpr_camera_plate}",
            mapping={
                "alpr_camera_plate_id": alpr_camera_plate,
                "alpr_camera_plate": alpr_camera_plate,
                "alpr_camera_plate_img": alpr_camera_img_plate,
            },
        )
        r.hset("alpr_camera_plate_to_id", alpr_camera_plate, alpr_camera_plate)
        r.hset("alpr_camera_plate_to_img", alpr_camera_plate, alpr_camera_img_plate)
        r.publish("alprdcamera", json.dumps(data))
        return jsonify(status="success", message="published", data=data)
    except:
        return jsonify(status="fail", message="not published")


    
@app.route('/alprd', methods=["POST"])
def alpr_from_video():
    get_images_alprd()
    request_data = request.get_json()
    alpr_results = request_data["results"]
    alpr_plate = alpr_results[0]["plate"]
    alpr_img = get_images_alprd()
    alpr_img_plate = alpr_img[1]
    try:
        data = alpr_plate
        r.hset(
            f"alpr_plate:{alpr_plate}",
            mapping={
                "alpr_plate_id": alpr_plate,
                "alpr_plate": alpr_plate,
                "alpr_plate_img": alpr_img_plate,
            },
        )
        r.hset("alpr_plate_to_id", alpr_plate, alpr_plate)
        r.hset("alpr_plate_to_img", alpr_plate, alpr_img_plate)
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
                yield "data: {}\n\n".format(str(data))
            except:
                pass
    return Response(sse_events(), mimetype="text/event-stream")

@app.route('/camerasse', methods=["GET"])
def camera_sse():
    def camera_sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("alprdcamera")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data))
            except:
                pass
    return Response(camera_sse_events(), mimetype="text/event-stream")
@app.route("/images", methods=["GET"])
def alprd_images():
    def alpr_sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("alprdimages")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data))
            except:
                pass
    return Response(alpr_sse_events(), mimetype="text/event-stream")


@app.route("/cameraimages", methods=["GET"])
def alprd_camera_images():
    def alpr_camera_sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("alprdcameraimages")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data))
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
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            alpr_file = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            alpr_arg1 = "-c"
            alpr_arg2 = "gb"
            alpr_arg3 = "-j"
            alpr_arg4 = "-n 1"
            output = subprocess.check_output(['alpr',str(alpr_file), str(alpr_arg1), str(alpr_arg2), str(alpr_arg3), str(alpr_arg4)]).decode('utf-8')
            jl = json.loads(output)
            result = jl["results"]
            result_plate = result[0]["plate"]
            upload_id = r.incr("alpr_ids")
            r.hset("upload_plate_to_img", upload_id, result_plate)
            r.hset(f"upload_plate:{upload_id}",mapping={"alpr_plate": result_plate,},)
            print((output))
            return redirect(url_for('home'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploadvideo', methods=['GET', 'POST'])
def upload_alpr_file():
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
            return redirect(url_for('home'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/display/<filename>')
def display_video(filename):
	print('display_video filename: ' + filename)
	return redirect(url_for('static', filename='upload/' + filename), code=301)

def gen_frames():  # generate frame by frame from camera
    camera = cv2.VideoCapture('http://127.0.0.1:8082')
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/video")
def video():
    return send_file("./static/upload/alprVideo.mp4")

@app.route("/") 
def home():
    return render_template('index.html')      

if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )