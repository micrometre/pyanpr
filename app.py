from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
import inotify.adapters
import os   
from time import time
import mysql.connector
import json
import logging
import pandas as pd
import datetime
import subprocess

UPLOAD_FOLDER = './static/upload'
ALLOWED_EXTENSIONS = {'mp4', 'png', 'jpg', 'jpeg', 'gif'}
logging.getLogger('flask_cors').level = logging.DEBUG
app = Flask(__name__, static_folder='static', static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

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
            f = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(f)
            cat_call=subprocess.Popen('file %s' % (str(f),),stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,  shell=True)
            print(cat_call.communicate())
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


if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )
