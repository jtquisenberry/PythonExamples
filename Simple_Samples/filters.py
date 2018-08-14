
my_list = [1,2,3,4,5,6,7,8,9]
smallers = filter(lambda x: True if x < 4 else False, my_list)
print(list(smallers))


def get_smallers(num):
    if num < 6:
        return True

smallers2 = filter(get_smallers,my_list)
print(list(smallers2))