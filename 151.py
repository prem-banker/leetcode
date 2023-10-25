class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ans = ''
        word=''
        for el in s.strip():

            if el != ' ':
                word+=el
            else:
                if word != '':
                    ans= f' {word}' + ans
                    word = ''


        return word + ans
