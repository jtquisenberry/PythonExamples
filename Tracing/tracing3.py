import time

def target3():
    print("target3")
    t = MyThread()
    t.start()
    time.sleep(1)
    print("target3")