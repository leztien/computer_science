"""one-time pad encription with xor"""

import secrets
from typing import Tuple


def random_key(length:int) -> int:
    bt:bytes = secrets.token_bytes(length)
    i:int = int.from_bytes(bt, byteorder='big')
    return(i)

def encode(text:str) -> Tuple[int,int]:
    bt:bytes = text.encode(encoding='utf_8')
    i:int = int.from_bytes(bt, byteorder='big')
    dummy:int = random_key(length=len(bt))  #key
    encripted:int = i ^ dummy
    return(encripted, dummy)

def decode(encripted:int, key:int):
    i:int = encripted ^ key
    length = (i.bit_length() + 7) // 8  # add 7 to ensure no bits are croped off
    bt:bytes = i.to_bytes(length=length, byteorder="big")
    text:str = bt.decode(encoding="utf_8")
    return(text)


##################################
    
text = "This is a secret message!"

encripted, key = encode(text)
text = decode(encripted, key)
print(text)
