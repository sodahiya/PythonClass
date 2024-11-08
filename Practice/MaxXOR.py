nums = [0,1,1,3]
k =2
r = []
while len(nums) > 0:
    print(nums)
    res = 0
    for i in range(len(nums)):
        print(f"res = {res}, nums[{i}] = {nums[i]}")
        res = res ^ nums[i]

    print(res)
    max = 0
    v = 0
    for i in range(pow(2,k)):
        print(f"{res} XOR {i} = {res ^ i}")
        if (res ^ i) > max:
            max = res ^ i
            v = i
    r.append(v)
    nums.pop()
    print(r)