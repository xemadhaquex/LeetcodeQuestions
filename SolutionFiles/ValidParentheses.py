class Solution:
    def isValid(self, s: str) -> bool:
        #basically need to go through the whole string, count every number of "(" ")"
        #make sure when youre done you have the same number of each
        
        stack = []
        
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i]) 
            else:
                if stack == []:
                    return False
                    
                if (stack[-1] == "("  and s[i] == ")") or (stack[-1] == "[" and s[i] == "]") or (stack[-1] == "{" and s[i]=="}"):
                    stack.pop()
                else:
                    return False
        
        if stack == []:
            return True
        else:
            return False
