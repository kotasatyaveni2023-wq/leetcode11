class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while num > 0:
            d = num % 10
            if d != 0 and temp % d == 0:
                count += 1
            num //= 10
        return count

