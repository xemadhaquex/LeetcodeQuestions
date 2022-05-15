class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        xstr=str(x)
        negative=0
        
        if xstr[0]=="-":
            negative = 1
            xstr = xstr[1:]
            
        xstr = list(xstr)
        xstr=xstr[::-1]
        
        print(xstr)
        
        ans=""
        for element in xstr:
            ans += element
                
        ans=int(ans)
        
        if ans > 2147483648-1 or ans < -2147483648:
            return 0
        
        if negative ==1:
            ans=ans*-1
        
        return ans
