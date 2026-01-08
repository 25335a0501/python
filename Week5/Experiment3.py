#Factorial Of a Number Without Recursion
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"Factorial of number {n}={fact}")
num=int(input("enter the number:"))
fact(num)


#Factorial Of a Number With Recursion
def fact1(n):
    if n<=0 or n==1:
        return 1
    else:
        return n*fact1(n-1)
num=int(input("\nenter the number:"))
print(f"Factorial of number {num} ={fact1(num)}")
