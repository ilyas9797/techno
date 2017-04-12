import http.client

h2 = http.client.HTTPConnection('127.0.0.1:9090')
h2.request("GET", "ilyas")
resp = h2.getresponse()
print(resp.read().decode())