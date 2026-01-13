class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for c in s:
            if c.isalnum():
                s2 += c.lower()
        
        l, r = 0, len(s2)-1
        while l < r:
            if s2[l] == s2[r]:
                l+=1
                r-=1
            else:
                return False
        return True