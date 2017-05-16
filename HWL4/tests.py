'''Module documentation'''
import http.client

if __name__ == '__main__':
    client = http.client.HTTPConnection('127.0.0.1:9090')
    client.request("GET", "ilyas")
    response = client.getresponse()
    print(response.read().decode())
