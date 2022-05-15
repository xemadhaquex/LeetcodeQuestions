class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # [1 2 3 3 3 3 3 3 3 4 5 ] target is 3 so ans is [2, 8]
        
        left = 0
        right = len(nums)-1
        middle=0
        
        index1= -1
        index2= -1
        
        if len(nums)==1:
            if target== nums[0]:
                return [0,0]
            else:
                return [-1,-1]
        
        while left<right:
            middle=left+(right-left)//2
            if nums[middle] == target:
                index1 = middle
                #got rid of m approach
                
                if nums[middle+1]==target:
                    index2=middle+1
                elif nums[middle-1]==target and (middle-1) !=-1:
                    index2=middle-1
                else:
                    return [index1, index1]
                print([index1,index2])
                if index1>index2:
                    return [index2,index1]
                else:
                    return[index1,index2]
            elif target>nums[middle]:
                left +=1
            else:
                right=right-1
        
        return [index1,index2]
