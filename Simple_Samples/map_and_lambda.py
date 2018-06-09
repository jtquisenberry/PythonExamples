
def doCube(n):
    return n**3

cube = lambda n: n**3

nums = [0,1,2,3,4]
nums_abs = list(map(abs, nums))
print(nums_abs)

nums3 = list(map(doCube, nums))
print(nums3)
nums3 = list(map(cube, nums))
print(nums3)