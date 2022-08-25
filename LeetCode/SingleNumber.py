from collections import defaultdict

def singleNumber(nums):
    counter = defaultdict(int)
    for letter in nums:
        counter[letter] += 1
    for key, value in counter.items():
        if value == 1:
            return key


print(singleNumber(nums = [1,2,1,3,2,5]))