nums = [1,2,3,1]
nums2 = set(nums)
if len(nums2) < len(nums):
    print("True")
else:
    print("False")
############################
strs = ["eat","tea","tan","ate","nat","bat"]
diction = dict({})
lis = []
for x in strs:
    key = tuple(sorted(list(x)))
    if key not in diction:
        diction[key] = []
    diction[key].append(x)
           
diction = list(diction.values())
print(diction)
############################
nums = [2,7,11,15]
target = 9
for x in nums:
    for y in nums[nums.index(x):]:
        if x+y== target:
            print(f"[{nums.index(x)}, {nums.index(y)}]")