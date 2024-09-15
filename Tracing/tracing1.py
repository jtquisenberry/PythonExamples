from multiprocessing import Process


def target_func():
    print("target start")

def func2():
    print("func2")
    p = Process(target=target_func)
    p.start()

def main():
    print("main")
    func2()


if __name__ == '__main__':
    main()


# python -m trace -t tracing1.py
