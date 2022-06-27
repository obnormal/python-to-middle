import threading
import uuid
from multiprocessing import Process, Queue, Pipe, Manager
from time import sleep


class Back:

    def __init__(self, manager_dict):
        self.worker = None
        self.manager_dict = manager_dict

    def start(self):
        self.worker = Process(target=self.inner_process, args=(self.manager_dict,))
        self.worker.start()

    def stop(self):
        self.worker.terminate()
        self.worker.join()

    @staticmethod
    def inner_process(manager):
        commands = {
            'sum': sum,
            'max': max,
            'mun': min,
        }
        while True:
            for id_, data in manager.items():

                if not isinstance(data, tuple):
                    continue

                cmd, *nums = data
                command = commands.get(cmd)
                if command:
                    manager[id_] = command(*nums)
                else:
                    manager[id_] = None


class Front:

    def __init__(self, manager_dict):
        super().__init__()
        self.worker = None
        self.manager_dict = manager_dict
        self.message_queue = Queue()

    def call_command(self, cmd, *args):
        id_ = str(uuid.uuid4())
        self.message_queue.put((id_, cmd, *args),)
        sleep(2)

        return id_

    def get_result(self, id_):
        return self.manager_dict.pop(id_)

    def start(self):
        self.worker = Process(target=self.inner_process, args=(self.message_queue, self.manager_dict,))
        self.worker.start()

    def stop(self):
        self.worker.terminate()
        self.worker.join()

    @staticmethod
    def inner_process(queue, manager):

        def inner_thread(msg, mngr):
            id_, cmd, *nums = msg
            mngr[id_] = (cmd, *nums)

        while True:
            message = queue.get()
            if message:
                thread = threading.Thread(target=inner_thread, args=(message, manager))
                thread.start()
                thread.join()

            sleep(1)




class Composer:
    def __init__(self):
        self.result = None
        manager = Manager()
        manager_dict = manager.dict()
        print(manager_dict)
        self.back_process = Back(manager_dict)
        self.front_process = Front(manager_dict)

    def start(self):
        self.back_process.start()
        self.front_process.start()

    def stop(self):
        self.back_process.stop()
        self.front_process.stop()

    def get_front(self):
        return self.front_process

