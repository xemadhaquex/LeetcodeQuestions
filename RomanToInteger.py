class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        
        mydict={'I': 1, 'V' : 5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        extra = 0
        for i in range(l):
            t = mydict[s[i]]
            x=t
            try:
                tt = mydict[s[i +1]]
            
                if t < tt:
                    x = tt - t
                    extra = extra + tt
                else:
                    x = t
            except:
                print("An exception occurred")

            total = total + x
        return (total - extra)
