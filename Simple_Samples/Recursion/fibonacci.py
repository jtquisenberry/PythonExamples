

def fibonacci(n):
    if (n < 2):
        #print(n)
        return n
    else:
        #print(fibonacci(n-1) + fibonacci(n-2))
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    nums = [0,1]
    i = 2
    while i < n:
        nums.append(nums[i - 1] + nums[i - 2])
        i += 1
    return nums


n = 9
print(fibonacci(n))
print(fibonacci2(n+1))
