from PIL import Image
import string,base64,binascii,subprocess

width,height = 53,62
split_table = list(string.ascii_uppercase)+[x for x in range(1,11)]
extracted_table = [0,1,2,3,4,5,6,7,9,10,13,15,22,25,27,28,30,32,35,77,79,95,113,122,140,169,174,201,314]

correct_data = {}
mapping = {}

for x in split_table:
    img = Image.open("../img/split/{}.png".format(x)).convert("RGB")
    tmp = []
    for y in range(width):
        for z in range(height):
            tmp.append(img.getpixel((y,z)))
    correct_data[x] = tmp

for x in extracted_table:
    img = Image.open("../img/extracted/extracted-{}.png".format(x)).convert("RGB")
    tmp = []
    for y in range(width):
        for z in range(height):
            tmp.append(img.getpixel((y,z)))

    for b,c in correct_data.items():
        flag = 0
        for d,e in zip(tmp,c):
            if d != e:
                if abs(d[0]-e[0]) < 23:
                    continue
                else:
                    flag=1
                    break
        if flag == 0:
            mapping[str(x)] = b

print(mapping)

for x,y in mapping.items():
    cmd = "cp ../img/extracted/extracted-{0}.png ../img/correct/{1}.png".format(x,y)
    subprocess.call(cmd,shell=True)
