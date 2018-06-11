import subprocess,pickle,base64,binascii

number_of_images=3498

encoded=""
mapping = {0:"G",1:"Q",2:"3",3:"T",4:"I",5:"O",6:"J",7:"U",9:"Y",10:"Z",13:"M",15:"X",22:"R",25:"A",27:"W",28:"E",30:"B",32:"H",35:"D",77:"N",79:"C",95:"S",113:"V",122:"4",140:"K",169:"F",174:"L",201:"5",314:"2"}

with open("number_list.pklt","rb") as f:
	l = pickle.load(f)

for x in l:
	encoded += mapping[x]

with open("QR_hash.gif","wb") as f:
	f.write(binascii.unhexlify(base64.b32decode(encoded+("="*(8-len(encoded)%8)))))
