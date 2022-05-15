class Solution:
    def longestPalindrome(self, s: str) -> str:
        #go through each letter left to right
        #if that letter is a palindrome, which it is, then do i+1 and i-1
        #test if those are equal, if they are then you palindrome got bigger
        #get final form of that palindrome and test if > than len(ans)
        #if yes then set ans = to that palindrome
        
        ans=s[0]
        for i in range(len(s)-1):
            
            n=0
            
            if s[i+1]==s[i-1]:
                n=0
                while i+n<len(s) and i-n>=0:
                    if s[i+n]==s[i-n]:
                        #print(s[i-n:i+n+1])
                        if len(s[i-n:i+n+1]) > len(ans):
                            ans=s[i-n:i+n+1]  
                    else:
                        break
                    n+=1    
            if s[i+1]==s[i]:
                n=0
                while i+n<len(s) and i-n>=0:
                    if i+n+1<len(s):
                        if s[i+n+1]==s[i-n]:
                            if len(s[i-n:i+n+2]) > len(ans):
                                ans=s[i-n:i+n+2]
                        else:
                            break
                    n+=1
                
        return ans    
            
