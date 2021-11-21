class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        leftPointer = 0
        rightPointer = len(nums)-1
        cur = len(nums)-1
        ans = [0]*len(nums)

        while leftPointer <= rightPointer:
            if abs(nums[leftPointer]) > abs(nums[rightPointer]):
                ans[cur] = nums[leftPointer]**2
                leftPointer = leftPointer+1
            else:
                ans[cur] = nums[rightPointer]**2
                rightPointer = rightPointer-1
            cur = cur-1

        return ans

sol = Solution()

#  Test Case, answer should be [0, 1, 9, 16, 100]
nums1 = [-6, -1, 2, 3, 10]
ans1 = sol.sortedSquares(nums1)
print(ans1)