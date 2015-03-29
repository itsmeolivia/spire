from flask import Flask, request
import os
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/start_job', methods=['POST'])
def start_job():
    f = request.files['script_file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print f
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
