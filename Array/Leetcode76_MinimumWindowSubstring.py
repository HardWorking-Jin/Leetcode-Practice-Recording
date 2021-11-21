class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        new_t = {}
        for char in t:
            if char in new_t:
                new_t[char] += 1
            else:
                new_t[char] = 1

        new_s = []
        for i, char in enumerate(s):
            if char in new_t:
                new_s.append([i, char])

        window = {}
        formed = 0
        left = 0
        res = [float('inf'), 0, 0]    
        for right in range(len(new_s)):
            char = new_s[right][1]
            
            if char in window:
                window[char] += 1
            else:
                window[char] = 1
            
            if window[char] == new_t[char] :
                    formed += 1                
                
            while formed == len(new_t) and left <= right:
                
                char = new_s[left][1]

                start = new_s[left][0]
                end = new_s[right][0]
                if end-start+1 < res[0]:
                    res[0] = end-start+1
                    res[1] = start
                    res[2] = end
                
                window[char] -= 1
                left += 1
                
                if window[char] < new_t[char]:
                    formed -= 1
                    
                    
        return '' if res[0] == float('inf') else s[res[1]:res[2]+1]

sol = Solution()

s1 = 'ADOBECODEBANC'
t1 = 'ABC'
ans1 = sol.minWindow(s1, t1)
print(ans1)



     