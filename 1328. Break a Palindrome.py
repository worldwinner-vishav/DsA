class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return ""
        n = len(s)
        i = 0
        Flag = False
        ans = ""
        while i< n//2:
            if s[i]!="a" and Flag == False:
                ans+= "a"
                Flag = True
            else:
                ans+=s[i]
            i+=1
            
        ans += s[i:]
        if Flag == False:
            ans = ans[:-1] + "b"
        return ans   
1
