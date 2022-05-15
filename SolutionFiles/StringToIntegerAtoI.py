class Solution:
    def myAtoi(self, s: str) -> int:
        
        newstr=""
        neg=False
        n=0
        pos=False
        
        i=0
        if s == "":
            return 0
        while s[i] == " ":
            i+=1
            if i > len(s)-1:
                break
            
        if i > len(s)-1:
            return 0
        if s[i] == "-":
            neg = True
            i +=1
            
        elif s[i] == "+":
            pos == True
            i +=1
        if i > len(s)-1:
                return 0
        
        while ord(s[i])>=48 and ord(s[i])<=57 :
            newstr += s[i]
            i+=1
            if i > len(s)-1:
                break
    
        if newstr != "":
            n=int(newstr)
        
        if neg==True:
            n *= -1
        
        if n < -2147483648:
            n = -2147483648
        elif n > 2147483647:
            n = 2147483647
        
        return n
