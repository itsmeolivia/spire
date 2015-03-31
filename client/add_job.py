import requests
from sys import argv

url = "http://127.0.0.1:5000/start_job"
file = open(argv[1], 'rb')
files = {'script_file': file}

r = requests.post(url, files=files)
print r.text
