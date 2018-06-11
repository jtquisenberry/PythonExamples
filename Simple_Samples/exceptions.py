# https://docs.python.org/3/library/exceptions.html

try:
    print(1/0)
except ZeroDivisionError as e:
    print('Specific exception')
    print(e)
except Exception as e:
    print('General exception')
    print(e)
finally:
    print('done')

