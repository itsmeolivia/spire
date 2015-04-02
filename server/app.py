from flask import Flask, request, jsonify
import os
from subprocess import call, Popen, PIPE

app = Flask(__name__)
app.debug = True
jobs = {}


@app.route('/start_job', methods=['POST'])
def start_job():

    f = request.files['script_file']
    file_path = os.tmpnam()
    f.save(file_path)

    call(['chmod', '+x', file_path])

    p = Popen([file_path], stdout=PIPE, stderr=PIPE)

    jobs[p.pid] = p
    return str(p.pid)


@app.route('/status', methods=['GET'])
def status():

    pid = request.args.get('req_pid', -1)
    if (pid == -1) or int(pid) not in jobs:
        return 'Not a valid ID'

    state = jobs[int(pid)]
    state.poll()
    if state.returncode is None:
        return jsonify({'process_terminated': False})

    return jsonify({
        'return_code': state.returncode,
        'stderr': state.stderr.read(),
        'stdout': state.stdout.read(),
        'process_terminated': True
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
