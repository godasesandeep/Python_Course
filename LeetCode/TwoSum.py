# By taking  Compliment
'''
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution,

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]


nums = [2,7,11,15]

target = 17

def two_sum(nums,target):

    num_dic={}
    i=0
    while i<len(nums):
        num=nums[i]
        compliment=target-num
        if compliment in num_dic:
            j=num_dic[compliment]
            return [i,j]
        num_dic[num]=i
        i +=1

ans=two_sum(nums,target)
print(ans)

def twoSum(nums: [int], target: int) ->[int]:
    seen = {}
    for i, value in enumerate(nums): #1
        remaining = target - value #2
        
        if remaining in seen: #3
            return [i, seen[remaining]]  #4
        else:
            seen[value] = i  #5


ans=twoSum(nums,target)
print(ans)

'''

def twoSum1(numbers:[int], target: int) -> [int]:
    
    #for left in range(len(numbers) -1): #1
    numbers.sort()
    left=0
    right = len(numbers) - 1 #2
    while left < right: #3
        temp_sum = numbers[left] + numbers[right] #4
        if temp_sum > target:  #5
            right -= 1 #6
        elif temp_sum < target: #7
            left +=1 #8
        else:
            return [left, right]  #9

nums=[3,4,5,6,7,8,9,10] # Should be sort
target=7
ans=twoSum1(nums,target)
print(ans)