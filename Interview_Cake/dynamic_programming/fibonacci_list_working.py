# This list method of calculating the nth Fibonacci number is
# similar to the iterative version. However, it takes O(n) space

def fibonacci(n):
    nums = [0, 1]
    i = 2
    while i <= n:
        nums.append(nums[i - 1] + nums[i - 2])
        i += 1
    return nums


x = 10
fibonacci_list = fibonacci(x)
print(fibonacci_list)
fibonacci_value = fibonacci_list[-1]
print(fibonacci_value)

