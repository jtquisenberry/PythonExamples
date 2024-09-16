from multiprocessing import Process
from tracing3 import target3


def target_func():
    print("target start")

def func2():
    print("func2")
    p = Process(target=target3)
    p.start()

def main():
    print("main")
    func2()


if __name__ == '__main__':
    main()
