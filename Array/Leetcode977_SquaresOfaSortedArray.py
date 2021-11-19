class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        for n in nums:
            ans.append(n**2)
        
        ans.sort()
        
        return ans

sol = Solution()

#  Test Case, answer should be [0, 1, 9, 16, 100]
nums1 = [-4, -1, 0, 3, 10]
ans1 = sol.sortedSquares(nums1)
print(ans1)