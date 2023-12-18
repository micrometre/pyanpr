# flask_sse.py
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import os
import ast

app = Flask(__name__, static_folder='static', static_url_path='',)


def get_alpr_images_result():
    result_stdout = os.popen('./scripts/monit.sh').read()
    d = ast.literal_eval(result_stdout)
    print((d))
    return (result_stdout)





@app.route('/',methods=['GET',])
def home():
    return '<pre>'+get_alpr_images_result()+'</pre>'





@app.route('/alprd', methods=["POST"])
def hello_world():
    get_alpr_images_result()
    return "<p>Hello, World!</p>"


@app.route("/video")
def video():
    return send_file("./static/upload/alprVideo.mp4")
if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )
