import datetime


class Task:

    def __init__(self, title, estimate, state='in_progress'):
        if type(title) != str:
            raise TypeError('неверный формат заголовка')
        elif type(estimate) != datetime.date:
            raise TypeError('неверный тип даты')
        elif type(state) != str:
            raise TypeError('неверный формат состояния')
        elif state != 'in_progress' and state != 'ready':
            raise AttributeError('невозможное состояние задачи')
        else:
            self._title = title
            self._estimate = estimate
            self._state = True if state == 'in_progress' else False

    @property
    def title(self) -> str:
        '''
        
        :return: tittle
        :rtype: str
        '''
        return self._title

    @property
    def estimate(self) -> datetime.date:
        return self._estimate

    @property
    def state(self) -> str:
        return 'in_progress' if self._state else 'ready'

    @property
    def remaining(self) -> datetime.timedelta:
        if self._state:
            return self._estimate - datetime.date.today()
        else:
            return datetime.timedelta(0)

    @property
    def is_failed(self) -> bool:
        if self._state and self.remaining < datetime.timedelta(0):
            return True
        else:
            return False

    def ready_task(self):
        self._state = False


class Roadmap:
    '''
    :type _tasks: list
    '''
    def __init__(self, tasks=None):
        if not tasks:
            self._tasks = []
        elif type(tasks) == list and all(type(task) == Task for task in tasks):
            self._tasks = tasks
        else:
            raise TypeError

    def add(self, task):
        if type(task) != Task:
            raise TypeError('ожидается элемент типа Task')
        else:
            self._tasks.append(task)

    def filter(self, state) -> list:
        if type(state) != str:
            raise TypeError
        elif state != 'in_progress' and state != 'ready':
            raise AttributeError('невозможное состояние задачи')
        else:
            returned_list = []
            for task in self._tasks:
                if task.state == state:
                    returned_list.append(task)
            return returned_list

    def get_critical_tasks(self) -> list:
        active_tasks = self.filter('in_progress')
        critical_tasks = []
        for task in active_tasks:
            if task.remaining <= datetime.timedelta(3):
                critical_tasks.append(task)
        return critical_tasks

