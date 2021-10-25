def fac(n):
    if n==1:
        return 1
    else:
        return n * fac(n-1)

in1=int(input("Enter your number\n"))
print("Factorial is ", fac(in1))