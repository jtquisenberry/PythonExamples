from multiprocessing import JoinableQueue, Queue
from threading import Thread

class JoinableQueue2(object):

    def __init__(self):
        #super().__init__(0,0,0,0)
        self.q = JoinableQueue()
        self.q.put(0)
        self.q.put(1)
        self.q.put(2)
        self.q.put(3)
        self.q.join()
        self.a = 0
        print("Released block")

def do_work():
    # q = JoinableQueue2()

    print("Start 'do_work'")
    q.join()
    print("End 'do_work'")

if __name__ == '__main__':
    q = JoinableQueue()
    q.put(0)
    q.put(1)
    q.put(2)
    q.put(3)
    thread = Thread(target=do_work)
    thread.start()
    q.qsize()
    q.task_done()
    while True:
        aaa = 999
#print(dir(q))