def si(p,r,t):
    return (p*r*t)/100

def ci(p,r,t):
    return p*(1+r/100)**t

n = int(input("Eneter the type of interest you want to calculate: 1. Simple Interest 2. Compound Interest"))

if n ==1:
    p = float(input("Enter the principal amount"))
    r = float(input("Enter the rate of interest"))
    t = float(input("Enter the time"))
    print("The simple interest is",si(p,r,t))

elif n ==2:
    p = float(input("Enter the principal amount"))
    r = float(input("Enter the rate of interest"))
    t = float(input("Enter the time"))
    print("The compound interest is",ci(p,r,t))

