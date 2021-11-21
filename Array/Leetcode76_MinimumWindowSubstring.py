class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        size = len(s)
        new_s = {}
        new_t = {}
        formed = 0
        res = [float('inf'), 0, 0]
        
        for char in t:
            if char in new_t:
                new_t[char] += 1
            else:
                new_t[char] = 1    
            
        for right in range(size):
            char = s[right]
            
            if char in new_s:
                new_s[char] += 1
            else:
                new_s[char] = 1
            
            if char in new_t and new_s[char] == new_t[char] :
                    formed += 1                
                
            while formed == len(new_t) and left <= right:
                
                char = s[left]
                
                if right-left+1 < res[0]:
                    res[0] = right-left+1
                    res[1] = left
                    res[2] = right
                
                new_s[char] -= 1
                left += 1
                
                if char in new_t and new_s[char] < new_t[char]:
                    formed -= 1
                    
        return '' if res[0] == float('inf') else s[res[1]:res[2]+1]

sol = Solution()

s1 = 'ADOBECODEBANC'
t1 = 'ABC'
ans1 = sol.minWindow(s1, t1)
print(ans1)



     