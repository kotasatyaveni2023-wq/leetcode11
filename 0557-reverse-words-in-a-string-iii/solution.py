class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        l=s.split()
        for word in l:
            res.append(word[::-1])
        return " ".join(res)
