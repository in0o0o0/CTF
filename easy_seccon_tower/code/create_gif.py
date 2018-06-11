import subprocess

with open("encoded.txt","r") as f:
	text = f.read()

cmd ="convert -delay 20 -loop 0 "

for x in text:
	cmd += "../img/split/{}.png ".format(x)

cmd +="result.gif"
subprocess.call(cmd.split())
