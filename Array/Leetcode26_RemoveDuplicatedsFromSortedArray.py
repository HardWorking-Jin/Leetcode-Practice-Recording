class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        slowPointer = 0
        
        for fastPointer in range(0, size):
            if nums[fastPointer] != nums[slowPointer]:
                
                slowPointer = slowPointer+1
                nums[slowPointer] = nums[fastPointer]
        
        k = slowPointer+1
        
        return nums[0:k]

sol = Solution()

nums1 = [0,0,1,1,1,2,2,3,3,4]

# Test Case, answer should be [0, 1, 2, 3, 4]
ans1 = sol.removeDuplicates(nums1)
print(ans1)