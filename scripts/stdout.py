import os
from flask import Flask, request,  render_template, send_from_directory, send_file
from subprocess import check_output
import redis
import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_shell_script_output_using_communicate():
    session = Popen(['./scripts/manage.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

def get_shell_script_output_using_check_output():
    stdout = check_output(['./scripts/manage.sh']).decode('utf-8')
    print((type (stdout )))
    return stdout

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')



@app.route('/alpr', methods=['GET', 'POST'])
def alpr():
    if request.method == 'POST':
        request_data = request.get_json()
        request_data = request.get_json()
        alpr_results = request_data["results"]
        alpr_id = request_data["uuid"]
        alpr_plate_dict = alpr_results[0]
        alpr_plate_set = {alpr_plate_dict["plate"]}
        alpr_plate_str = repr(alpr_plate_set)
        alpr_stdout = get_shell_script_output_using_check_output()
        redis_client.hset("alpr_results:1", "plate", alpr_plate_str)
        redis_client.hset("alpr_results:1", "uuid", alpr_stdout)
        print( (alpr_stdout))
        return request_data

    
    


@app.route('/test',methods=['GET',])
def home():
    return '<pre>'+get_shell_script_output_using_check_output()+'</pre>'


@app.route("/video")
def video():
    return send_file("./public/upload/alprVideo.mp4")


if __name__ == "__main__":
    app.run(port=5000)
