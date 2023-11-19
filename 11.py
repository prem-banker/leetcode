from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights)-1
        maxvol = 0
        while (i < j):
            maxvol = max(maxvol, (j-i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                minh = heights[i]
                while (i < j):
                    i += 1
                    if (heights[i] > minh):
                        break 

            else:
                minh = heights[j]
                while (i < j):
                    j -= 1
                    if (heights[j] > minh):
                        break

        return maxvol
