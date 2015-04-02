import requests
from sys import argv

if len(argv) != 3:
    print 'Not valid input!'
    exit(-1)

if argv[1] == 'add':

    url = 'http://127.0.0.1:5000/start_job'
    file = open(argv[2], 'rb')
    files = {'script_file': file}

    r = requests.post(url, files=files)

    print r.text

elif argv[1] == 'status':

    pid = argv[2]
    url = 'http://127.0.0.1:5000/status'
    data = {'req_pid': pid}

    r = requests.get(url, params=data)

    print r.text

else:
    pass
