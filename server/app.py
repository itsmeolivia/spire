from flask import Flask, request

app = Flask(__name__)

@app.route('/start_job', methods=['POST'])
def start_job():
    f = request.files['script_file']
    print f
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
