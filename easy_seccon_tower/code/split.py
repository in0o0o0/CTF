from PIL import Image
import string

img = Image.open('../img/semaphore.png')
w,h = img.size
table=list(string.ascii_uppercase.replace("J",""))+["J"]+[x for x in range(1,11)]
index=0

for y in range(6):
	for x in range(6):
		tmp=img.crop((w/6*x,h/6*y,w/6*(x+1),h/6*(y+1)-24)) #画像の一部を切り出す
		bg = Image.new(mode='RGB', size=(int(w/6),int(h/6-24)),color=(255, 255, 255)) #白画像の生成
		bg.paste(tmp, (0, 0),tmp) #(0,0)の位置に画像を貼り付ける
		bg.save('../img/split/{}.png'.format(table[index]))
		index+=1
