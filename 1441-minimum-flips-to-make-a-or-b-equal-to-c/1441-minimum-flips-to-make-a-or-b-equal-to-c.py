class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        max_bits = max(a.bit_length(), b.bit_length(), c.bit_length())
        result = 0

        for i in range(max_bits):
            bit_a = (a >> i) & 1  
            bit_b = (b >> i) & 1  
            bit_c = (c >> i) & 1  

            if (bit_a | bit_b) != bit_c:  
                if bit_c == 1:
                    result += 1  
                else:
                    result += bit_a + bit_b  
        return result