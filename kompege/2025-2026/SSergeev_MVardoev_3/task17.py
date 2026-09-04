with open('17_25185.txt') as file:
    nums = file.readlines()

nums = [int(n) for n in nums]

min5 = min([n for n in nums if n % 10 == 5])
print(min5) # 15

res = []
for a, mid,  b in zip(nums, nums[1:], nums[2:]):
    if (a + b) % 2 == 1 and mid % min5 == 0:
        # print(a, mid, b)
        res.append(a + b)

print(len(res), min(res))
# 336 3549