lst = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]

print("The values from the 4 th position to 7 th position are",lst[3:7])
print("All the even values are",lst[1::2])
print("All the odd values are",list(reversed(lst[::2])))
print("All the odd values in reverse are",lst[-2::-2])
