import os
from flask import Flask, request,  render_template, send_from_directory, send_file
from flask import render_template_string 
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output

import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)
redis_client.set('key', 'value')
data = redis_client.get('key')
redis_client.set("name", "John")
redis_client.set("Age", '15')
name = redis_client.get("name")
age = redis_client.get("Age")
redis_client.hset("user:1", "name", "Alice")
redis_client.hset("user:1", "age", 30)
 
user_data = redis_client.hgetall("user:1")

def get_shell_script_output_using_communicate():
    session = Popen(['./scripts/manage.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

def get_shell_script_output_using_check_output():
    stdout = check_output(['./scripts/manage.sh']).decode('utf-8')
    return stdout

app = Flask(__name__)

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
        redis_client.hset("alpr_results:1", "plate", alpr_id)
        redis_client.hset("alpr_results:1", "uuid", alpr_id)
        redis_client.set("plate", alpr_id)
        print((type (alpr_plate_str)))
        return request_data

    
    


@app.route('/',methods=['GET',])
def home():
    return '<pre>'+get_shell_script_output_using_check_output()+'</pre>'


@app.route("/video")
def video():
    return send_file("./public/upload/alprVideo.mp4")


if __name__ == "__main__":
    app.run(port=5000)
