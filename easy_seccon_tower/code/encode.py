import binascii
import base64

with open("QRcode.gif","rb") as f:
  with open("encoded.txt","wb") as g:
      g.write(base64.b32encode( binascii.hexlify(f.read())).replace(b"=",b""))
