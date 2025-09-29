class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for digit in digits:
            num=num*10+digit
        num=num+1
        res=[]
        while num>0:
            d=num%10
            res.insert(0,d)
            num=num//10
        return res
        
