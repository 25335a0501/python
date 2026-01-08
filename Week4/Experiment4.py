#minimum and maximum numbers
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
maxi=a
mini=a
if maxi<b:
    maxi=b
if maxi<c:
    maxi=c
if mini>b:
    mini=b
if mini>c:
    mini=c
print("Maximum Number=",maxi)
print("Minimum Number=",mini)
