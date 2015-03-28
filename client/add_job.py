import requests
from sys import argv

url = "http://127.0.0.1:5000/start_job"
files = {'script_file': open(argv[1], 'rb')}

r = requests.post(url, files=files)
print r.text
