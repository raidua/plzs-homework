def F(n):
    if n <= 1: return max(n,0)
    f=0
    f0=1
    f1=1
    for i in range(1, n-1):
        f = f0 + f1
        f0, f1 = f1, f
    return f
n=int(input("Please enter an integer."))
print("Fibonacci number from 1 to", n, "is", F(n))
