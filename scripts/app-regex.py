# flask_sse.py
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
from flask import jsonify
from subprocess import check_output
import os
import re


app = Flask(__name__, static_folder='static', static_url_path='')





def start_alpr():
    result_stdout = os.popen('./scripts/monit.sh').read()
    text = "I was searching my source to make a big desk yesterday."
    re.findall(r'\bs\w+', text)
    print(result_stdout)
    return result_stdout




@app.route('/alprd', methods=["POST"])
def hello_world():
    text = "I was searching plate my source to make a big desk yesterday."
    print(re.findall(r'\bp\w+', text))
    return "<p>Hello, World!</p>"

@app.route("/video")
def video():
    start_alpr()
    return send_file("./static/upload/alprVideo.mp4")
if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )
