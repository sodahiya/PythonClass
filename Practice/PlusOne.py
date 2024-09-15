digits = [9,9]
lst = []
carry = 0

digits = list(reversed(digits))

if (digits[0] + 1)>9:
    digits[0] = (digits[0] + 1)%10
    carry =1
else:
    digits[0] = digits[0] + 1
lst.insert(0,digits[0])
for i in digits[1:]:
    print(i)

    i += carry
    if i > 9 :
        carry = 1
        i = i % 10
    else :
        carry =0
    print("Carry is",carry,"i is",i)
    lst.insert(0,i)
if carry == 1:
    lst.insert(0,carry)
print(lst)