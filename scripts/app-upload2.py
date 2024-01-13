from __future__ import print_function
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from flask import Flask, Response, jsonify, json, render_template
from flask import redirect, session

from flask_cors import CORS
import redis
import inotify.adapters
import os   
from time import time
import mysql.connector
from mysql.connector import errorcode
import json
import logging
import pandas as pd
import datetime
import subprocess
from datetime import date, datetime, timedelta
from redis.commands.json.path import Path

UPLOAD_FOLDER = './static/upload'
ALLOWED_EXTENSIONS = {'mp4', 'png', 'jpg', 'jpeg', 'gif'}
logging.getLogger('flask_cors').level = logging.DEBUG
app = Flask(__name__, static_folder='static', static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)



r = redis.Redis(
    host='localhost',
    port=6379,
)
alprdb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="395F844E696D423F6B7ACBBA301539668E6",
  database="alprdata"
)






def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
            dict2 = dict(jl)
            result = dict2["results"]
            result_zip = dict(zip(range(len(result)),result))
            result_zip_plate = result_zip[0]["plate"]
            result_zip_confidence = result_zip[0]["confidence"]
            result_img = ("http://172.187.216.226/:5000/uplaod/{}\n\n".format(filename))
            alprcursor = alprdb.cursor()
            alprcursor.execute("CREATE DATABASE IF NOT EXISTS alprdata;")
            alprcursor.execute("CREATE TABLE  IF NOT EXISTS  plates (plate TEXT, img TEXT, confidence TEXT);")
            sql = "INSERT INTO plates (plate, img, confidence) VALUES (%s, %s, %s)"
            val = result_zip_plate, result_img, result_zip_confidence
            r.publish("bigboxcode", json.dumps((val)))
            alprcursor.execute(sql,val)
            alprdb.commit()
            return redirect(url_for('upload_file', name=filename))
    return Response(alpr_result())
def alpr_result():
    upcursor = alprdb.cursor()
    upcursor.execute("SELECT * FROM plates")
    upresult = upcursor.fetchall()
    upresult_tuple = upresult[0]
    upresult_plate = upresult_tuple[0]
    upresult_img = upresult_tuple[1]
    upresult_confidence = upresult_tuple[2]
    alpr_images = {
        "plate": upresult_plate,
        "img": upresult_img,
        "confidence": upresult_confidence,
        }
    print(upresult)
    return(json.dumps(alpr_images))

@app.route("/video")
def video():
    return send_file("./static/upload/alprVideo.mp4")


@app.route("/") 
def home():
    return render_template('index.html')      

if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )
