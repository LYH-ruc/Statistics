# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:47:10 2026

@author: 95451
"""
#快慢指针
def removeElement(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow

def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
            
def removeDuplicates(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1    
#对撞指针
def reverseString(s):
    left,right = 0,len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
def isPalindrome(s):
    left,right = 0,len(s)-1
    while left < right:
        if not s[left].isalnum(): 
            left += 1
            continue
        elif not s[right].isalnum():
            right -= 1
            continue
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True
            
def twoSum(numbers, target):
    left,right = 0,len(numbers)-1
    while left < right :
        s = numbers[left] +numbers[right]
        if s == target :
            return [left+1, right+1]
        elif s < target:
            left += 1
        elif s > target:
            right -= 1
            
def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1 
        while left < right:
            if nums[left]+nums[right] == -nums[i]:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[left]+nums[right] < -nums[i]:
                left += 1
            else:
                right -= 1
    return result
#滑动窗口
def min_window_k_chars(s: str, c: str, k: int) -> int:
    left = 0
    count = 0
    min_length = float('inf')
    for right in range(len(s)):
        if s[right] == c:
            count += 1
        while count >= k:
            min_length = min(min_length, right - left + 1)
            if s[left] == c:
                count -= 1
            left += 1
    return min_length if min_length != float('inf') else -1




























