from pwn import xor
import re

xor_encrypted = bytes.fromhex('0e0b213f26041e')
crypto_hint   = bytes.fromhex('63727970746f7b')

