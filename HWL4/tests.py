'''Module documentation'''
import http.client

if __name__ == '__main__':
    CLIENT = http.client.HTTPConnection('127.0.0.1:9090')
    CLIENT.request("GET", "ilyas")
    RESPONSE = CLIENT.getresponse()
    print(RESPONSE.read().decode())
