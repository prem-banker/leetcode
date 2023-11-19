from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = dict()
        ans = 0
        for num in nums:
            if num in dic:
                dic[num]-=1
                ans+=1
                if dic[num] == 0:
                    del dic[num]
            elif k - num in dic:
                dic[k-num]+=1
            else: 
                dic[k-num]=1
        return ans
