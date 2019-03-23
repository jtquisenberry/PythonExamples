# https://docs.python.org/3/library/exceptions.html

def do_division(divisor):
    try:
        print(1/divisor)
    except ZeroDivisionError as e:
        print('Specific exception')
        print(e)
    except Exception as e:
        print('General exception')
        print(e)
    else:
        print('SUCCESS, no exception.')
    finally:
        print('DONE')
        print()


if __name__ == '__main__':
    divisors = [1,0,'a']
    for divisor in divisors:
        do_division(divisor)

