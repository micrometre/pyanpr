# flask_sse.py
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
from subprocess import check_output
import time

app = Flask(__name__)
CORS(app)
r = redis.Redis(
    host='localhost',
    port=6379,
)


def get_shell_script_output_using_check_output():
    stdout = check_output(['./scripts/manage.sh']).decode('utf-8')
    return stdout

@app.route("/alpr", methods=["GET"])
def alpr_sse():
    def alpr_sse_events():
        counter = 0
        while True:
            yield "data test: message counter - {}\n\n".format(get_shell_script_output_using_check_output())
            counter  += 1
            time.sleep(2)
    return Response(alpr_sse_events(), mimetype="text/event-stream")    
    
    

@app.route('/test',methods=['GET',])
def home():
    return '<pre>'+get_shell_script_output_using_check_output()+'</pre>'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/alprd', methods=["POST"])
def publish():
    try:
        data = json.loads(request.data)
        r.publish("bigboxcode", json.dumps(data))
        return jsonify(status="success", message="published", data=data)
    except:
        return jsonify(status="fail", message="not published")

        
@app.route('/sse', methods=["GET"])
def sse():
    def sse_events():
        # Initiate Redis pub/sub 
        pubsub = r.pubsub()
        # Subscribe to channel "bigboxcode"
        pubsub.subscribe("bigboxcode")

        # Listen to message and perform action when a new message arrives
        for message in pubsub.listen():
            try:
                data = message["data"]

                yield "data: {}\n\n".format(str(data, 'utf-8'))
            except:
                pass

    return Response(sse_events(), mimetype="text/event-stream")

    
    
@app.route("/video")
def video():
    return send_file("./public/upload/alprVideo.mp4")