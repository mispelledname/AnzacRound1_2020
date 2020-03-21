import math

def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def max_prime_diff(n):
    
    if n==4:
        return 0

    for i in range(3, n, 2):
        if is_prime(i):
            if is_prime(n-i):
                return (n-i-i)


def goldbach_steps(num):
    count = 0
    curr = num
    while curr > 2:
        curr = max_prime_diff(curr)
        count += 1
    return count

n = int(input())
print(goldbach_steps(n))
#print(max_prime_diff(28))