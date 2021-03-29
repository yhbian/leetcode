class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # regularize data
        sign = 1
        if dividend < 0 and divisor > 0:
            dividend = -dividend
            sign = -1
        if dividend > 0 and divisor < 0:
            divisor = -divisor
            sign = -1
        if dividend < 0 and divisor < 0:
            dividend, divisor = -dividend, -divisor
        
        if dividend < divisor:
            return 0

        # init 
        res, ret = dividend, 0
        divisors = [divisor]
        multiples = [1]
        i = 0

        # updates
        while i >= 0 and res >= divisor:
            cur_divisor, cur_multiple = divisors[i], multiples[i]
            if res >= cur_divisor:
                res -= cur_divisor
                ret += cur_multiple
                cur_divisor += cur_divisor
                cur_multiple += cur_multiple
                if cur_divisor > divisors[-1]:
                    divisors.append(cur_divisor)
                    multiples.append(cur_multiple)
                    i += 1
            else:
                i -= 1
        
        if sign < 0:
            ret = -ret
        if ret < -2 ** 31:
            return -2 ** 31
        elif ret > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return ret