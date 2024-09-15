name =input("Enter your name: ")
if name.endswith("Grummy"):
    if name.startswith("Mr."):
        print("Hello Mr. Grummy")
    elif name.startswith("Mrs."):
        print("Hello Mrs. Grummy")
elif name.endswith("Smith"):
    if name.startswith("Mr."):
        print("Hello Mr. Smith")
    elif name.startswith("Mrs."):
        print("Hello Mrs. Smith")

else:
    print("Hello stranger")

