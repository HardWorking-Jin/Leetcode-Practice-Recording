class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        slowPointer = 0
        
        for fastPointer in range(length):
            if nums[fastPointer] != val:
                nums[slowPointer] = nums[fastPointer]
                slowPointer = slowPointer+1
        k = slowPointer                   
        return nums[0:k]


sol = Solution()

nums1 = [0,1,2,2,3,0,4,2]
val1 = 2

# Test Case, answer should be [0, 1, 3, 0, 4], elements in list can be in any sequence
ans1 = sol.removeElement(nums1, val1)
print(ans1)