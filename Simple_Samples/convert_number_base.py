
# Given a number, return the number as a string in base 9.
# Don't use a built-in function to solve this problem.
# Example input:
# n: 10
# Example output:
# 11
# Example input:
# n: 120
# Example output:
# 143


def solution(n):
    sign = 1
    if n < 0:
        sign = -1
        n *= -1
    result = 0
    index = 0
    while n > 0:
        result += (n%9) * 10**index
        n //= 9
        index += 1
    print(result * sign)
    return str(result * sign)