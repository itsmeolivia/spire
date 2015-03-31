from flask import Flask, request
import os
from werkzeug import secure_filename
from subprocess import call

app = Flask(__name__)

@app.route('/start_job', methods=['POST'])
def start_job():

    f = request.files['script_file']
    file_path = os.tmpnam()
    f.save(file_path)
    #run the file

    call(["chmod",  "+x" , file_path])
    call([file_path])

    return 'ur mom!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
