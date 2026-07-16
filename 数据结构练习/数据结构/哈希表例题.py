# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:22:11 2026

@author: 95451
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = dict()
    for i in range(len(nums)):
        num = target - nums[i]
        if num in seen:
            return [seen[num],i]
        else:
            seen[nums[i]] = i
    
    
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            j = seen[nums[i]]
            if i - j <= k:
                return True
        seen[nums[i]] = i
    return False

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    res = 0
    for num in num_set:
        if num - 1 in num_set:
            continue
        length = 1
        while num + length in num_set:
            length += 1
        res = max(res, length)
    return res
    
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count={}
    for c in s:
        count[c] = count.get(c,0) + 1
    for c in t:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] < 0:
            return False
    return True
        

