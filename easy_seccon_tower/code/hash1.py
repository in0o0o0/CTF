import subprocess,pickle
from collections import defaultdict

number_of_images = 3498

md5_dict = {}
number_list = [0 for x in range(number_of_images)] #前に出現したどの画像と同じかを記録する
check_list = [1 for x in range(number_of_images)]  #初めて出現したら0を入れる

for x in range(number_of_images):
  cmd = "md5 ../img/out/out-{}.png".format(x)
  p = subprocess.Popen(cmd.split(" "),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  out,err = p.communicate()
  hash = out.split(b" ")[-1]

  if md5_dict.get(hash) == None:
      check_list[x] = 0

  md5_dict.setdefault(hash,x)
  number_list[x] = md5_dict[hash]

with open("number_list.pklt","wb") as f:
    pickle.dump(number_list,f)

for idx,val in enumerate(check_list):
    if val == 0:
        cmd = "cp ../img/out/out-{0}.png ../img/extracted/extracted-{0}.png".format(idx)
        subprocess.call(cmd,shell=True)
