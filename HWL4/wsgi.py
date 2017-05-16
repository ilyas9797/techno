'''Module documentation'''
from wsgiref.simple_server import make_server
from HWL4.parse import get_dataset
from HWL3 import Roadmap, Task


class WSGIApplication(object):
    '''WSGIApplication class docstring'''
    default_headers = [
        ('Content-Type', 'text/html; charset=utf8'),
        ('Server', 'WSGIExample/1.0'),
    ]

    def __init__(self, environment, start_response_callback):
        self.environment = environment
        self.start_response = start_response_callback

    def __iter__(self):
        self.start_response('200 OK', self.default_headers)

        roadmap = Roadmap()
        for task in get_dataset('dataset.yml'):
            roadmap.add(Task(task[0], task[2], task[1]))
        critical_tasks = roadmap.get_critical_tasks()
        for task in critical_tasks:
            yield (task.title + ' -- до ' + str(task.estimate) + '\n').encode('utf-8')


http_wsgi_server = make_server('127.0.0.1', 9090, WSGIApplication)
http_wsgi_server.handle_request()
