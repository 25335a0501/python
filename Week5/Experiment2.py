#Displaying Fibonacci Series Using Iteration
def fibo1(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
n=int(input("enter the number:"))
fibo1(n)

#Displaying Fibonacci Series Using Recursion
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2)+fib(n-1)
num=int(input("\nenter the range:"))
for i in range(0,num):
    print(fib(i),end=" ")
