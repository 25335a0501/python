#To count number of even and odd numbers in n numbers
n=int(input("enter the range of numbers:"))
ecount=0
ocount=0
for i in range(1,n+1):
    if i%2==0:
        ecount+=1
    else:
        ocount+=1
print(f"Number of odd numbers in first {n} numbers={ocount}")
print(f"Number of even numbers in first {n} numbers={ecount}")
