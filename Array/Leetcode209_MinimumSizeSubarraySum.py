class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = float('inf')
        size = len(nums)
        j = 0
        sum = 0
        
        for i in range(size):
            sum += nums[i]
            while sum >= target:
                res = min(res, i-j+1)
                sum -= nums[j]
                j += 1
                
        return 0 if res == float('inf') else res
        


sol = Solution()

# Test Case1, answer should be 2
nums1 = [2, 3, 1, 2, 4, 3]
target1 = 7
ans1 = sol.minSubArrayLen(target1, nums1)
print(ans1)

# Test Case2, answer should be 3
nums2 = [1, 2, 3, 4, 5]
target2 = 11
ans2 = sol.minSubArrayLen(target2, nums2)
print(ans2)