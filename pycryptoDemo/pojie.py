# Ghost使用自己的私钥对内容进行rsa 解密 
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import sys

encrypt_text = sys.argv[1] 
with open('master-private.pem') as f:
   random_generator = Random.new().read
   key = f.read()
   rsakey = RSA.importKey(key)
   cipher = Cipher_pkcs1_v1_5.new(rsakey)
   text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
   print(text.decode())

