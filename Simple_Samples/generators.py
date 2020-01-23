def get_number():
    for i in range(4):
        yield i

if __name__ == '__main__':
    x = get_number()
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))

    try:
        print(next(x))
    except Exception as e:
        print(type(e))
        print(e.args)

    print()
    for number in get_number():
        print(number)




