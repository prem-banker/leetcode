class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        currcount = 0
        for letter in s[0:k]:
            if letter in vowels:
                currcount+=1
        maxcount = currcount
        
        for i in range(k, len(s)): 
            if s[i] in vowels:
                if not (s[i-k] in vowels):
                    currcount+=1
            else:
                if s[i-k] in vowels:
                    currcount-=1
            
            maxcount = max(maxcount, currcount)
        return maxcount


