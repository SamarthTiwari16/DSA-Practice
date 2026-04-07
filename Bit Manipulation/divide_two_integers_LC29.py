dividend = 10, divisor = 3 # Output = 3

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        neg = (dividend < 0) != (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        for i in range(31, -1, -1):
            if (b<<i) <= a:
                a -= (b << i)
                res += (1 << i)
        return -res if neg else res
