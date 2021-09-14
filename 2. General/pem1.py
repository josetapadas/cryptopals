import os
from Crypto.PublicKey import RSA

FILENAME = "privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem"

cwd = os.getcwd()
private_key = open(f'{cwd}/files/{FILENAME}', 'rb')

key = RSA.import_key(private_key.read())
print(key.d)

  

