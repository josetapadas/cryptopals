from pwn import xor
import re

xor_encrypted = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for current_byte in range(0, 256):
  binary_byte = chr(current_byte).encode('UTF-8').strip()
  xor_challenge = xor(xor_encrypted, binary_byte).decode('UTF-8')
  
  if re.match(r'crypto', xor_challenge) != None:
    print(f'[!] found flag {xor_challenge} (XORed with byte: {binary_byte})')
    break