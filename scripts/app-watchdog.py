# flask_sse.py
from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
from subprocess import check_output
from subprocess import Popen, PIPE
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
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

@app.route("/images", methods=["GET"])
def alpr_images():
    def alpr_sse_events():
            while True:
                yield "{}".format(get_shell_script_output_using_check_output())
            time.sleep(2)
    return Response(alpr_sse_events(), mimetype="text/event-stream")    


@app.route('/alprd', methods=["POST"])
def publish():
    class EventHandler2(FileSystemEventHandler):
        def on_created(self,event):
            print("A new create event was made",event.src_path)
    path =  './public/images'    
    event_handler = EventHandler2()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        data = json.loads(request.data)
        r.publish("bigboxcode", json.dumps(data))
        return jsonify(status="success", message="published", data=data)
    except:
        return jsonify(status="fail", message="not published")
@app.route('/test',methods=['GET',])
def home():
    return '<pre>'+get_shell_script_output_using_check_output()+'</pre>'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/alpr", methods=["GET"])
def alpr_sse():
    def alpr_sse_events():
            while True:
                yield "{}".format(get_shell_script_output_using_check_output())
            time.sleep(2)
    return Response(alpr_sse_events(), mimetype="text/event-stream")    
        
@app.route('/alprsse', methods=["GET"])
def sse():
    def sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("bigboxcode")
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
if __name__ == "__main__":
     app.run(debug=True)   