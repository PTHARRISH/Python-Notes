def fibonacci_sequence():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

# Generate the first 10 numbers in the Fibonacci series
for i, num in enumerate(fibonacci_sequence()):
    if i == 10:
        break
    print(num)