from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        onezero = False
        prod = 1
        for id, el in enumerate(nums):
            if el == 0:
                if onezero:
                    return [0] * len(nums)
                else:
                    index = id
                    onezero=True
            else:
                prod = prod*el

        if onezero:
            return [ (prod if x == index else 0 ) for x in range(len(nums)) ]
        else:
            return [prod//el for el in nums]

