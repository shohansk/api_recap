import requests

endpoint ="http://www.github.com"
endpoint="http://httpbin.org/anything"

get_res = requests.get(endpoint) # http request
print(get_res.text) #print raw text response
