def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get the value of n from the user
n = int(input("Enter a positive integer n: "))

# Calculate the nth number in the Fibonacci series
result = fibonacci(n)

# Print the result
print(f"The {n}th number in the Fibonacci series is: {result}")
