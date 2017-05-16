'''Module documentation'''
import http.client

h2_client = http.client.HTTPConnection('127.0.0.1:9090')
h2_client.request("GET", "ilyas")
resp = h2_client.getresponse()
print(resp.read().decode())
