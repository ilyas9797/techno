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

    def get_default_headers(self):
        '''Function docstring'''
        return self.default_headers

    def second_public_func(self):
        '''Function docstring'''
        pass

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

if __name__ == '__main__':
    HTTP_SERVER = make_server('127.0.0.1', 9090, WSGIApplication)
    HTTP_SERVER.handle_request()
