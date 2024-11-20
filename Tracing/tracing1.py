from multiprocessing import Process
from tracing3 import target3
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self):
        super().__init__()
        self.a = 1
        self.b = 2

    def run(self):
        x = 0
        while x <= 500:
            if x % 100 == 0:
                print(x)
            x += 1
        return True


class MyThread2(Thread):
    def __init__(self):
        super().__init__()
        self.a = 1
        self.b = 2

    def run(self):
        x = 1000
        while x <= 1500:
            if x % 100 == 0:
                print(x)
            x += 1
        return True




def target3():
    print("target3")
    t = MyThread2()
    t.start()
    time.sleep(1)
    print("target3")


def func2():
    print("func2")
    p = Process(target=target3)
    p.start()
    t = MyThread()
    t.start()

def main():
    print("main")
    func2()


if __name__ == '__main__':
    main()
