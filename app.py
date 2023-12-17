# flask_sse.py
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
import inotify.adapters
import os 
from flask import jsonify
import cv2
from subprocess import check_output



app = Flask(__name__, static_folder='static', static_url_path='')


CORS(app)
r = redis.Redis(
    host='localhost',
    port=6379,
)


def start_alpr():
    result = os.popen('./scripts/monit.sh').read()
    print(type(result))
    return result

def get_shell_output():
    stdout = check_output(['./scripts/monit.sh']).decode('utf-8')
    print(type((stdout )))
    return stdout

@app.route('/alprd', methods=["POST"])
def hello_world():
    start_alpr()
    get_shell_output()
    return "<p>Hello, World!</p>"

@app.route("/video")
def video():
    return send_file("./static/upload/alprVideo.mp4")
if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )
