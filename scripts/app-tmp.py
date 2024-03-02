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


@app.route('/camera', methods=["POST"])
def alpr_from_video():
    request_data = request.get_json()
    alpr_results = request_data["results"]
    alpr_plate = alpr_results[0]["plate"]
    print(request_data)
    return (alpr_plate)


if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )