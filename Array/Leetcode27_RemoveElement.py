class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        k = length
        
        for i in range(length):
            if nums[i] == val:
                for j in range(i, length):
                    if nums[j] > val:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        
        for n in range(length):
            if nums[n] == val:
                nums[n] = '_'
                k = k-1
                
                    
        
        return k, nums


sol = Solution()

nums1 = [0,1,2,2,3,0,4,2]
val1 = 2

ans1 = sol.removeElement(nums1, val1)
print(ans1)