# Python
# Generates a sequence of numbers where each number is the sum of the two preceding ones,
# but with a twist: it only includes numbers divisible by 3.
# This is a modified Fibonacci sequence.

def twisted_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0] if 0 % 3 == 0 else []

    sequence = []
    a, b = 0, 1
    count = 0

    while count < n:
        if a % 3 == 0:
            sequence.append(a)
            count += 1
        a, b = b, a + b
    return sequence

print(twisted_fibonacci(10))
print(twisted_fibonacci(5))
print(twisted_fibonacci(0))
print(twisted_fibonacci(2))