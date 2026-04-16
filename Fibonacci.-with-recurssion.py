# Recursive function to calculate Fibonacci using if-else
def fibonacci(x):
    if x == 0 or x == 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

if __name__ == "__main__":
    terms = 10
    print("Fibonacci Series using recursion and if-else: ", end="")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()
