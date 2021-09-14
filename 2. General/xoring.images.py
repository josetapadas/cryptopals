from PIL import Image
from pwn import *
import os

cwd = os.getcwd()

flag_image = Image.open(f'{cwd}/files/flag.png')
lemur_image = Image.open(f'{cwd}/files/lemur.png')

xored_bytes = xor(flag_image.tobytes(), lemur_image.tobytes())
xored_picture = Image.frombytes(lemur_image.mode, lemur_image.size, xored_bytes)
xored_picture.save(f'{cwd}/files/result.png')
