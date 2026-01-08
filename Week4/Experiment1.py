#To find the power of a number without built-in function
base=int(input("enter the base number:"))
exponent=int(input("enter the exponent value:"))
result=1
for i in range(exponent):
    result=result*base
print(result)
