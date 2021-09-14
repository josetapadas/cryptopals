import pwn
import json
import base64
import codecs
import random
from Crypto.Util import number

remote_server = pwn.remote('socket.cryptohack.org', 13377, level = 'debug')

def read_message():
  line = remote_server.recvline()
  return json.loads(line.decode())

def send_message(object):
  line = json.dumps(object).encode()
  remote_server.sendline(line)

def decode_challenge(message):
  encoding = message['type']
  encoded_message = message['encoded']
  decoded_message = ''

  if encoding == "base64":
      decoded_message = base64.b64decode(encoded_message).decode()
  elif encoding == "hex": 
      decoded_message = bytes.fromhex(encoded_message).decode()
  elif encoding == "rot13": 
      decoded_message = codecs.decode(encoded_message, 'rot_13')
  elif encoding == "bigint": 
      decoded_message = number.long_to_bytes(int(encoded_message, 16)).decode()
  elif encoding == "utf-8": 
      decoded_message = ''.join(list(map(lambda x : chr(x), encoded_message)))

  return {"decoded": decoded_message}

challange = {}
n = 0

while True:
  n += 1
  print(f'[+] Cracking challenge #{n}...')
  current_challenge = read_message()

  if 'flag' in current_challenge:
    break

  decoded_message = decode_challenge(current_challenge)

  send_message(decoded_message)

print(f"*** the solution is: {current_challenge}")