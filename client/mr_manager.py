import requests
from sys import argv

if len(argv) != 3:
    print 'Not valid input!'
    exit(-1)

if argv[1] == 'add':

    url = 'http://127.0.0.1:5000/start_job'
    file = open(argv[2], 'rb')
    files = {'script_file': file}

    try:
        r = requests.post(url, files=files)
    except requests.exceptions.ConnectionError:
        print 'Server Not Running'
        exit(-1)

    print r.text

elif argv[1] == 'status':

    pid = argv[2]
    url = 'http://127.0.0.1:5000/status'
    data = {'req_pid': pid}

    try:
        r = requests.get(url, params=data)
    except requests.exceptions.ConnectionError:
        print 'Server Not Running'
        exit(-1)

    print r.text

else:

    print 'Bad Command!'
    exit(-1)
