n = int(input())
for i in range(n):
    s = input()
    print(s)

    flag = 0
    for j in range(len(s)-1):
        for k in range(j+1, len(s)):
            print(f"{j},{k}")
            str_list = list(s)
            str_list[j], str_list[k] = str_list[k], str_list[j]

            if "".join(str_list) < s:
                flag = 1
                break
# What is the output of the following code?