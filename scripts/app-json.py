# flask_sse.py
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
from flask import jsonify
from subprocess import check_output
import os
import re
import inotify.adapters
from openalpr import Alpr
import json
import ast

app = Flask(__name__, static_folder='static', static_url_path='')


def get_images():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/images/')
    result_stdout = os.popen('./scripts/monit.sh').read()
    d = ast.literal_eval(result_stdout)
    print(type(d))
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        #print("http://localhost:5000/images/{}\n\n".format(filename))
        alpr_images = {"img": "http://localhost:5000/images/{}\n".format(filename)}
        return ("alprd", json.dumps("http://localhost:5000/images/{}\n".format(filename)))







@app.route('/alprd', methods=["POST"])
def hello_world():
    get_images()
    return "<p>Hello, World!</p>"

@app.route("/video")
def video():
    return send_file("./static/upload/alprVideo.mp4")
if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )
