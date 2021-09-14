from pwn import *
from Crypto.Util import number
import os
import zlib
cwd = os.getcwd()

def group_pixels(pixels, number_of_bytes_per_pixel):
  for index in range(0, len(pixels), number_of_bytes_per_pixel):
      yield pixels[index:index+number_of_bytes_per_pixel]

def read_chunk(file):
  chunk_length = number.bytes_to_long(file.read(4))
  chunk_type = file.read(4)
  chunk_data = file.read(chunk_length)
  chunk_crc = file.read(4)

  return chunk_type.decode(), chunk_data, chunk_length, chunk_crc

def read_file(filename):
  current_image = open(f'{cwd}/files/{filename}', 'rb')
  
  # reading the PNG header and ignoring it
  current_image.read(8)

  chunks = []
  while True:
    chunk_type, chunk_data, chunk_length, chunk_crc = read_chunk(current_image)
    chunks.append({ 'type': chunk_type, 'data': chunk_data, 'size': chunk_length })

    if chunk_type == 'IEND':
      break

  header_chunk = chunks[0]
  header_data = header_chunk['data']

  image_width = number.bytes_to_long(header_data[0:4])
  image_height = number.bytes_to_long(header_data[4:8])
  bit_depth = number.bytes_to_long(header_data[8:9])
  color_type = number.bytes_to_long(header_data[9:10])
  filter_method = number.bytes_to_long(header_data[10:11])
  interlace_method = number.bytes_to_long(header_data[11:12])

  print(f"[*] header info for {filename}:\n")
  print(f"\twidth: {image_width} pixels")
  print(f"\theight: {image_height} pixels")
  print(f"\tbit depth: {bit_depth}")
  print(f"\tcolor type: {color_type}")
  print(f"\tfilter method: {filter_method}")
  print(f"\tinterlace method: {interlace_method}\n")

  data_chunks = list(filter(lambda elm: elm['type'] == 'IDAT', chunks))
  image_data = zlib.decompress(b"".join(map(lambda elm: elm['data'], data_chunks)))

  current_image.close()

  return image_data

flag_image_data = read_file('flag.png')
lemur_flag_data  = read_file('lemur.png')
