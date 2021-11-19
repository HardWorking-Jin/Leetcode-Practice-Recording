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
        return k, nums


sol = Solution()

nums1 = [0,1,2,2,3,0,4,2]
val1 = 2

ans1 = sol.removeElement(nums1, val1)
print(ans1)