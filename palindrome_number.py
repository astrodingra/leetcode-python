# QUES: Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(objects):
  def isPalindrome(self,x):
    if x<0:
      return False
    x_ = str(x)
    x_rev = x_[::-1]
    return x_== x_rev

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(23))
