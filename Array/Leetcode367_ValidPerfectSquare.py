class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num+1
        
        while left < right:
            mid = (left+right)//2
            if mid*mid < num:
                left = mid+1
            elif mid*mid > num:
                right = mid
            else:
                return True
        
        return False

sol = Solution()

# Test Case1, the answer should be True
nums1 = 16
answer1 = sol.isPerfectSquare(nums1)
print(answer1)

# Test Case2, the answer should be True
nums2 = 1
answer2 = sol.isPerfectSquare(nums2)
print(answer2)

# Test Case3, the answer should be True
nums3 = 0
answer3 = sol.isPerfectSquare(nums3)
print(answer3)

# Test Case4, the answer should be False
nums4 = 5
answer4 = sol.isPerfectSquare(nums4)
print(answer4)






