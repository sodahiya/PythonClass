a= input("Enter the first string: ")
b= input("Enter the second string: ")

if len(a) == len(b):
    if sorted(a) == sorted(b):
        print("Anagram")
    else:
        print("Not an anagram")
else:
    print("Not an anagram")
