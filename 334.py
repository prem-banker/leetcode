from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        c1 = nums[0]
        c2, p1, p2 = '', '',''

        for el in nums:
            if c2 == '':
                if el > c1:
                    c2 = el
                elif el < c1:
                    c1 = el
            elif c2 != '':
                if el < c1:
                    # it will go in potential array
                    if p1 == '':
                        p1 = el
                    else:
                        # check if it is even better than the current potential
                        if el < p1:
                            p1= el
                        # this means if we got a pair which are better
                        # suited than current contenders and potentials become
                        # contenders.
                        elif el > p1:
                            c1,c2 = p1,el
                            p1,p2 = '', ''

                elif c1 <=  el <= c2:
                    if p1 == '':
                        if el > c1:
                            c2 = el
                    else:
                        if el < p1:
                            p1 = el
                        elif el > p1:
                            c1, c2 = p1,el
                            p1,p2 = '', ''

                elif el > c2:
                    return True
        return False
