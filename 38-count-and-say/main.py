class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return "1"

        previous = self.countAndSay(n - 1)

        if len(previous) == 1:
            return "1" + previous[0]

        i = 1
        k = previous[0]
        count = 1
        res = ""

        while i < len(previous):
            while k == previous[i]:
                i += 1
                count += 1

                if i >= len(previous):
                    break;
            
            res += str(count) + k
            if i < len(previous):
                k = previous[i]
                count = 0

        return res
