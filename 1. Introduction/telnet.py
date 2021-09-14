#!/usr/bin/env python3

import telnetlib
import json

HOSTNAME = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOSTNAME, PORT)

def readline():
  return tn.read_until(b"\n")

def send(json_object):
  request = json.dumps(json_object).encode()
  tn.write(request)

def recieve():
  line = readline()
  return json.loads(line.decode())

print(readline())
print(readline())
print(readline())
print(readline())

request = {
  "buy": "flag"
}

send(request)

response = recieve()
print(response)