class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[::-1][:-2:]
        for i in range(32 - len(bin(n)[::-1][:-2:])):
            b += "0"
        return int(b, 2)