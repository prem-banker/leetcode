class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0

        if len(s) == 0:
            return True



        for el in t:
            if el == s[s_index]:
                s_index += 1

            if s_index >= len(s):
                return True

        return False

