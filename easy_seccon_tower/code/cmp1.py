import subprocess

number_of_images=3498; #分割してできた画像の数

check_list = [0 for x in range(number_of_images)] #すでに同じ種類のものが出現していたら1をいれる

for idx,val in enumerate(check_list): #インデックスと値を同時に取り出す
	if val == 1: #すでに同じものがでている
		continue
	for x in range(idx+1,number_of_images): #idx+1番目以降にidx番目と同じものがないか調べる
		if check_list[x] == 1:
			continue
		cmd = "cmp ../img/out/out-{}.png ../img/out/out-{}.png".format(idx,x)
		p=subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		out, err = p.communicate() #標準出力と標準エラー出力の取得
		if len(out) == 0: #比較結果が一致したら1をいれる
			check_list[x] = 1

#残ったものがわかるように別名で保存する
for idx,val in enumerate(check_list):
	if val == 0:
		cmd = "cp ../img/out/out-{0}.png ../img/extracted/extracted-{0}.png".format(idx)
		subprocess.call(cmd,shell=True)
