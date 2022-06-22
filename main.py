
n = int(input("enter number:"))
def Fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return Fibonacci(i-1)+ Fibonacci(i-2)
for x in range(n):
     print(Fibonacci(x))

n = int(input("enter number:"))
def Fibonacci_recursive(i):
    return 1 if i == 1 else Fibonacci(i-1)+ Fibonacci(i-2)
print(Fibonacci(n))