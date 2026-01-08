#Multiplication Table
num=int(input("enter the number for which you want multiplication table:"))
m=int(input("enter the range up to which you want multiplication table:"))
print(f"\n        MULTIPLICATION TABLE OF {num}     ")
for i in range(1,m+1):
    res=num*i
    print(f"          {num}*{i}={res}                  ")
