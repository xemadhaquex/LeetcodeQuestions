class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #make a loop to go through each letter see if it exists in an array
        #if it does not exits in the array, then add 1 to counter
        #if it does exist in array, add the counter value to ans[]
        #return the max(ans)
        
        array=[]
        ans=[]
        counter=0
        
        for index in range(len(s)):
            isValid = 1
            while isValid==1:        
                if s[index] in array:
                    ans.append(counter) #ans = [2]
                    counter=0
                    array.clear()
                    isValid=0
                    
                else:
                    array.append(s[index])#array = [p w]
                    counter = counter + 1 #counter = 2
                    index+=1
                    if index >= len(s):
                        break
        
        ans.append(counter)
        print("ans is "+str(ans))
        print("array is "+ str(array))
        return max(ans)
