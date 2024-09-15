#Demonstrate various way of string
#Taking a variable
a="This is a random String"
b = "Coders"
#by using indexing(Both positive and negative
print(a[1])
print(a[4])
#here string index out of range for this reason error through
'''
     # print(a[19])
'''
#By using slice operator
print(a[::])
print(a[0:7:1])
print(a[0:10:2])
print(a[0:-1:3])

# operator % is used to concat 2 strings

print("%s %s" % (a,b))