from multiprocessing import Process
import sys
from pprint import pprint

def target_func():
    print("target start")

def func2():
    print("func2")
    p = Process(target=target_func)
    p.start()

def tracefunc(frame, event, arg, indent=[0]):
    if event == "call":
        print(type(frame), type(event), arg)
        indent[0] += 2
        print("-" * indent[0] + "> call function", frame.f_code.co_name)
    elif event == "return":
        print("<" + "-" * indent[0], "exit function", frame.f_code.co_name)
        indent[0] -= 2
    return tracefunc

def tracefunc2(frame, event, arg, indent=[0]):
    print(frame.f_code.co_name)

def tracefunc3(frame, event, arg, indent = [0]):
    frame.f_trace_lines = True

    pprint(vars(frame))
    print(event, frame, type(frame))




def main():
    print("main")
    func2()


if __name__ == '__main__':
    #sys.setprofile(tracefunc3)
    sys.settrace(tracefunc3)
    main()


# python -m trace -t tracing1.py
