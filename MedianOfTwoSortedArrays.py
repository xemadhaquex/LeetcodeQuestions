class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L1 = len(nums1)
        L2 = len(nums2)
        
        L3 = L1 + L2
        if L3 %2 == 1:
            L3 = math.ceil(L3/2)
            print(L3)
        else:
            L3 = (L3/2) + 1
        
        
        p1 = 0 
        p2 = 0
        
        newlist = []
        
        while p1 != L1 and p2 != L2: #while we arent at the end of list1 or list 2
            if nums1[p1]< nums2[p2]:
                newlist.append(nums1[p1])
                p1 +=1
            else:
                newlist.append(nums2[p2])
                p2 +=1
            
            if len(newlist) == L3:
                break
        
        while len(newlist) < L3:
            if p1 == L1:
                newlist.append(nums2[p2])
                p2 +=1
            else:
                newlist.append(nums1[p1])
                p1+=1
                
            
        
        if (L1+L2)%2 ==1:
            return newlist[-1]
        else:
            return (newlist[-1] + newlist[-2])/2
