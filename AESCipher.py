import base64
from base64 import b16encode
from Crypto import Random
from Crypto.Cipher import AES
import sys

BS = 16
def u_ord(c):
    if sys.hexversion >= 0x03000000:
        return c
    else:
        return ord(c)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:- u_ord(s[-1])]


class AESCipher:

	def __init__(self):
		self.default=""

	def encrypt( self,raw,key):
		raw =pad(raw)
		iv=Random.new().read(AES.block_size)
		cipher=AES.new(key,AES.MODE_CBC,iv)
		return base64.b64encode(iv+cipher.encrypt(raw))

	def decrypt( self, enc,key ):
		enc=base64.b64decode(enc)
		iv=enc[:16]
		cipher=AES.new(key, AES.MODE_CBC, iv )
		return unpad(cipher.decrypt(enc[16:]))



