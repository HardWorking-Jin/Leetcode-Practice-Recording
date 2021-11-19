class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        slowPointer = 0
        
        for fastPointer in range(size):
            if nums[fastPointer] != 0:
                temp = nums[fastPointer]
                nums[fastPointer] = nums[slowPointer]
                nums[slowPointer] = temp
                slowPointer = slowPointer+1
        
        return nums

sol = Solution()

# Test Case1, answer should be [1,3,12,0,0]
nums1 = [0,1,0,3,12]
ans1 = sol.moveZeroes(nums1)
print(ans1)

# Test Case2, answer should be [1]
nums2 = [1]
ans2 = sol.moveZeroes(nums2)
print(ans2)

# Test Case3, answer should be [0]
nums3 = [0]
ans3 = sol.moveZeroes(nums3)
print(ans3)

