#!/usr/bin/env python3

"""
Classic Computer Science Problems in Python
page 12
"""


from math import log2, ceil


class Compressor:
    def __init__(self, chars: str):
        self._compress(chars)
    
    def _compress(self, chars):
        self.d = {c:i for i,c in enumerate(sorted(set(chars)))}
        self.n = ceil(log2(len(self.d)))
        self.bits = 0b1
        for c in chars:
            self.bits <<= self.n
            self.bits |= self.d[c]
    
    def decompress(self):
        d = {v:k for k,v in self.d.items()}
        chars = ""
        for rightshift in range(0, self.bits.bit_length() - 1, self.n):
            chars += d[(self.bits >> rightshift) & (2 ** self.n - 1)]
        return chars[::-1]
            
            

if __name__ == '__main__':
    s = "ABBA_ABCXYZ"
    compressed = Compressor(s)
    print(compressed.decompress())


