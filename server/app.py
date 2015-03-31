from flask import Flask, request
import os
from werkzeug import secure_filename
from subprocess import call, Popen

app = Flask(__name__)

jobs = {}

@app.route('/start_job', methods=['POST'])
def start_job():

    f = request.files['script_file']
    file_path = os.tmpnam()
    f.save(file_path)
    #run the file

    call(["chmod",  "+x" , file_path])
    p = Popen([file_path])
    jobs[p.pid] = p
    return p.pid

@app.route('/status', methods=['GET'])
def status():
    state = jobs[p.pid]
    state.poll()
    return state.returncode

if __name__ == '__main__':
    app.run(host='0.0.0.0')
