class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        maxInt = 2**31

        n = abs(dividend)
        d = abs(divisor)

        quo = 0
        while n >= d:
            q = 0
            while True:
                b = d << (q + 1)
                if n < b:
                    break;
                q += 1

            quo += 1 << q
            n = n - (d << q)

        if dividend < 0:
            quo = quo * -1

        if divisor < 0:
            quo = quo * -1

        quo = min(quo, maxInt - 1)
        quo = max(quo, -1 * maxInt)
        
        return quo
