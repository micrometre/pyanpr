import os
from flask import Flask, flash, request, json, jsonify, redirect, url_for, send_file, render_template, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename
import redis
import mysql.connector
import inotify.adapters
import logging
import subprocess

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
r = redis.Redis(
    host='localhost',
    port=6379,
)



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
        return ("alprd", json.dumps("http://172.187.216.226:5000/images/{}\n".format(filename)))
@app.route('/alprd', methods=["POST"])
def alpr_from_video():
    request_data = request.get_json()
    alpr_results = request_data["results"]
    alpr_uuid = request_data["uuid"]
    alpr_plate = alpr_results[0]["plate"]
    alpr_img = get_images_alprd()
    alpr_img_plate = alpr_img[1]
    alprcursor = alprdb.cursor()
    print(request_data)
    alprcursor.execute("CREATE DATABASE IF NOT EXISTS alprdata;")
    alprcursor.execute("CREATE TABLE  IF NOT EXISTS  plates (uuid TEXT, plate TEXT, img TEXT );")
    sql = "INSERT INTO plates (uuid, plate, img) VALUES (%s, %s, %s)"
    val = (alpr_uuid, alpr_plate, alpr_img_plate)
    alprcursor.execute(sql,val)
    alprdb.commit()
    get_images_alprd()
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
            alprcursor = alprdb.cursor()
            alprcursor.execute("CREATE DATABASE IF NOT EXISTS alprdata;")
            alprcursor.execute("CREATE TABLE  IF NOT EXISTS  uploads (id INT KEY AUTO_INCREMENT,  plate TEXT);")
            sql = "INSERT INTO uploads (plate) VALUES (%s)"
            val = result_plate,
            alprcursor.execute(sql,val)
            alprdb.commit()
            print((result_plate))
            return redirect(url_for('upload_file', name=filename))
    return Response(alpr_result())

@app.route("/uploaddb", methods=["GET"])
def alpr_result():
        upcursor = alprdb.cursor()
        upcursor.execute("SELECT plate FROM uploads ORDER BY id DESC LIMIT 1;")
        upresult = upcursor.fetchall()
        j = json.dumps(upresult)
        return(j)



@app.route('/uploadvideo', methods=['GET', 'POST'])
def upload_alpr_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename('alprVideo.mp4')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            alpr_arg1 = "-f"
            output2 = subprocess.check_output(['alprd', str(alpr_arg1)]).decode('utf-8')
            print('returned value:', output2)
            data = json.loads(output2)
            r.publish("alprd", json.dumps(data))
            return redirect(url_for('upload_alpr_file', name=filename))
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
