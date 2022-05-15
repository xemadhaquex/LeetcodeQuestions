class Solution:
    def longestCommonPrefixPair(self, a:str, b:str) -> str:
        LCP = ""
        
        for i in range(min([len(a),len(b)])):
            if(a[i] == b[i]):
                LCP=LCP+a[i]
            else:
                break
        
        return LCP
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==1):
            return strs[0]
        
        LCP = self.longestCommonPrefixPair(strs[0],strs[1])       
    
        for i in range(1,len(strs)):
           LCP = self.longestCommonPrefixPair(LCP,strs[i])
        
        return LCP
