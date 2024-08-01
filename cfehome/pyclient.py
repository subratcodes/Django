import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "localhost:8000/service" #http://127.0.0.1:8000/ 

get_response = requests.get(endpoint) # HTTP Request
print(get_response.headers)
# print(get_response.status_code)