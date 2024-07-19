'''QUES: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

class Solution(object):
 def twoSum(self, nums, target):
     """
     :type nums: List[int]
     :type target: int
     :rtype: List[int]
     """
     nums_index = {}
     for i, num1 in enumerate(nums):
         num2 = target - num1
         if num2 in nums_index:
             return [nums_index[num2], i]
         nums_index[num1] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
