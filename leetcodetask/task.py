'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'{':'}','(':')','[':']'}
        for bracket in s:
            if bracket in dict:
                stack.append(bracket)
            elif stack and dict[stack[-1]] == bracket:
                stack.pop()
            else:
                return False
                break
        if not stack:
            return True
        else:
            return False

'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        a=set()        
        for i in range(n-3):
            for j in range(i+1,n-2):
                total = target-(nums[i] + nums[j]) 
                k = j+1
                l = n-1
                while (k<l):
                    p = nums[k] + nums[l]
                    if p == total:
                        a.add(tuple(sorted([nums[i], nums[j],nums[k], nums[l]])))
                        k+=1
                        l-=1
                    elif p>total:
                        l-=1
                    else:
                        k+=1
        return a

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op=[]
        for i in range(len(nums)):
            lo,hi=i+1,len(nums)-1
            while lo<hi:
                sumx=nums[i] + nums[lo] + nums[hi]
                if sumx == 0 and [nums[i], nums[lo], nums[hi]] not in op:
                    op.append([nums[i], nums[lo], nums[hi]])
                    
                if sumx<0:
                    lo+=1
                else:
                    hi-=1
            
        return op

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if strs == []:
            return res

        min_len = min(map(lambda x: len(x),strs))
        for i in range(min_len):
            temp = list(map(lambda x: x[:i+1], strs))
            if len(set(temp)) == 1:
                res = temp[0]
            else:
                continue
        return res

'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev  = 0
        new_val = x
        while x != 0:
            a = x %10
            rev = rev * 10 + a
            x = x // 10
        if rev == new_val:
            return True
        else:
            return False

'''

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
'''

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x!= 0:
            rev = rev*10 + x%10
            x = x // 10
        return rev

'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        start = max_length = 0
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_length = max(max_length, i - start +1)
            map[s[i]] = i
        return max_length

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, val in enumerate(nums):
            if target - val in lookup:
                return (lookup[target - val], i)
            lookup[val] = i
            