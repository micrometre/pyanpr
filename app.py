# flask_sse.py

from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import time
import redis

app = Flask(__name__)
CORS(app)
r = redis.Redis(
    host='localhost',
    port=6379,
)


@app.route("/")
def index():
    return render_template('index.html')

        


@app.route('/alpr', methods=["POST"])
def publish():
    res1 = r.xadd(
    "race:france",
    {"rider": "Castilla", "speed": 30.2, "position": 1, "location_id": 1},
)
    try:
        # Get data from request and parse it
        data = json.loads(request.data)

        # Send to Redis publisher

        r.publish("bigboxcode", json.dumps(data))
        #r.xadd("bigboxcode", json.dumps(data))
        print(r)
        
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

