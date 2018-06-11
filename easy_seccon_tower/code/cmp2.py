import subprocess,string,base64,binascii
import time

s = time.time()
#アルファベットはP以外が出現　数字は2~5が出現
table = list(string.ascii_uppercase.replace("P",""))+[str(x) for x in range(2,6)]
encoded = "" #作成した文字列を入れる
number_of_images = 3498 #画像の数


for x in range(number_of_images):
	for y in list(table):
		cmd = "cmp ../img/out/out-{}.png ../img/correct/{}.png".format(x,y)
		p = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		out, err = p.communicate()

		if len(out) == 0:
			encoded+=y
			break

with open("QR_cmp.gif","wb") as f:
	f.write(binascii.unhexlify(base64.b32decode(encoded+("="*(8-len(encoded)%8)))))
print (time.time()-s)
