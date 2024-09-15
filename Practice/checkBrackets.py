def isValid(s):

        stack =[]
        ls =0
        rs =0
        lm =0
        rm =0
        ll = 0
        rl = 0

        for i in s :
            if i == '(' :
                ls += 1
                stack.append(i)
            elif i ==')':
                rs += 1
                stack.append(i)

            elif i == '{':
                lm += 1
                stack.append(i)

            elif i == '}':
                rm += 1
                stack.append(i)
            elif i == '[':
                ll += 1
                stack.append(i)
            elif i == ']':
                rl += 1
                stack.append(i)

        a = 0
        matching_bracket = {
            ')': '(', 
            '}': '{',
            ']': '['}

        while(len(stack) > 0) :
            if (matching_bracket[stack[0]] == stack[-1]):
                stack.pop(0) 
                stack.pop

            else:
                print("A changed")
                a =1    
                break


        if (ls == rs and lm == rm and ll ==rl and a==0) :
            return True
        else:
            return False
print(isValid("()"))
        