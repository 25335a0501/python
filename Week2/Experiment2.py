#Compound Interest Calculation
p=int(input("enter the principal amount:"))
t=int(input("enter the time:"))
r=float(input("enter the rate of interest:"))
ca=p*(1+r/100)**t
ci=ca-p
print("Compound Interest=",ci)
