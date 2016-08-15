import requests

req = requests.post("http://text-processing.com/api/sentiment/", data={'text':"great"})
print req.status_code
print req.json()
