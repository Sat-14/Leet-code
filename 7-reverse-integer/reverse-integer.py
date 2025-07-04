class Solution:
    def reverse(self, x: int) -> int:
        INT32_MIN = -(2 ** 31)           # –2 147 483 648
        INT32_MAX =  (2 ** 31) - 1       #  2 147 483 647

        a = str(x)
        start = 1 if a[0] == '-' else 0
        k = a[start:][::-1]              # reverse the digits
        if start:                        # re‑attach minus sign
            k = '-' + k

        f = int(k)                       # reversed integer

        # ✅ Now check the *reversed* value
        if INT32_MIN <= f <= INT32_MAX:
            return f
        return 0
