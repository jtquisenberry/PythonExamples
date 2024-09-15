def main():
    print("main")
    if False:
        print("False")


if __name__ == '__main__':
    #sys.setprofile(tracefunc3)

    main()


# python -m trace -t tracing1.py


# coverage run --branch target1.py
# coverage report -m