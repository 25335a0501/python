#Checking Prime Number or not without recursion
def prime_number1(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("prime number")
    else:
        print("composite")
num=int(input("enter the number:"))
prime_number1(num)


#Checking Prime Number or not without recursion
def pr_number(n,i,count):
    if i>n:
        return count
    if n%i==0:
        return pr_number(n,i+1,count+1)
    else:
        return pr_number(n,i+1,count)
num=int(input("enter the number:"))
c=pr_number(num,1,0)
if c==2:
    print("Prime Number")
else:
    print("composite Number")
