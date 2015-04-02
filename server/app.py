from flask import Flask, request
import os
from werkzeug import secure_filename
from subprocess import call, Popen

app = Flask(__name__)
app.debug = True
jobs = {}

@app.route('/start_job', methods=['POST'])
def start_job():

    f = request.files['script_file']
    file_path = os.tmpnam()
    f.save(file_path)

    call(["chmod",  "+x" , file_path])

    p = Popen([file_path])

    jobs[p.pid] = p
    return str(p.pid)

@app.route('/status', methods=['GET'])
def status():

    pid = request.args.get('req_pid', -1)
    if (pid == -1) or int(pid) not in jobs:
        return "Not a valid ID"

    state = jobs[int(pid)]
    state.poll()
    return str(state.returncode) #evan hahn is The Wurst

if __name__ == '__main__':
    app.run(host='0.0.0.0')
