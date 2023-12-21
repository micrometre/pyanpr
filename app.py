from flask import Flask, Response, jsonify, json, request, render_template, send_file
from flask_cors import CORS
import redis
import inotify.adapters
from flask import jsonify
import os   
import mysql.connector

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)
alprdb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="395F844E696D423F6B7ACBBA301539668E6",
  database="alprdata"
)



r = redis.Redis(
    host='localhost',
    port=6379,
)

def sql_create_db():
    alprcursor = alprdb.cursor()
    alprcursor.execute("CREATE DATABASE IF NOT EXISTS alprdata;")
    alprcursor.execute("CREATE TABLE  IF NOT EXISTS  plates2 (plate TEXT, img TEXT );")
    sql = "INSERT INTO plates2 (plate, img) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    alprcursor.execute(sql,val)
    alprdb.commit()
    print(alprcursor.rowcount, "record inserted.")

 
def start_alpr():
    result_stdout = os.popen('./scripts/monit.sh').read()
    r.publish("alprd", json.dumps(result_stdout))
    s = result_stdout.split()
    #print((len(s)))
    print((s[0]))

def get_images():
    i = inotify.adapters.Inotify()
    i.add_watch('./static/images/')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        print("http://localhost:5000/images/{}\n\n".format(filename))
        #r.publish("bigboxcode","http://localhost:5000/images/{}\n".format (filename))
        alpr_images = {"img": "http://localhost:5000/images/{}\n".format(filename)}
        r.publish("bigboxcode", json.dumps((alpr_images)))
        return ("alprd", json.dumps("http://localhost:5000/images/{}\n".format(filename)))
@app.route("/images", methods=["GET"])
def alprd_images():
    def alpr_sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("bigboxcode")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data, 'utf-8'))
            except:
                pass
    return Response(alpr_sse_events(), mimetype="text/event-stream")  

@app.route('/alprd', methods=["POST"])
def publish():
    start_alpr()
    sql_create_db()
    try:
        data = json.loads(request.data)
        r.publish("alprd", json.dumps(data))
        return jsonify(status="success", message="published", data=data)
    except:
        return jsonify(status="fail", message="not published")

@app.route('/alprdsse', methods=["GET"])
def sse():
    def sse_events():
        pubsub = r.pubsub()
        pubsub.subscribe("alprd")
        for message in pubsub.listen():
            try:
                data = message["data"]
                yield "data: {}\n\n".format(str(data, 'utf-8'))
                #yield "data: {}\n\n".format(str(data, 'utf-8'))
            except:
                pass
    return Response(sse_events(), mimetype="text/event-stream")

@app.route("/video")
def video():
    return send_file("./static/upload/alprVideo.mp4")
@app.route('/')
def hello():
    return render_template('index.html')     
if __name__ == "__main__":
     app.config['TEMPLATES_AUTO_RELOAD']=True
     app.run(debug=True, host='0.0.0.0' )        