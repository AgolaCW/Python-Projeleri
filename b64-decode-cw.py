import os, sys, colorama, pyfiglet, base64
from colorama import Fore, Back, Style
print(Fore.GREEN) 
result = pyfiglet.figlet_format("CW-AGOLA-BASE64-DECODE", font = "digital" )
print(result)
d=input(Fore.WHITE+"Dosya yolunu giriniz (örn:/root/base64.txt): "+"\n")
isl=int(input(Fore.WHITE+"\nBase64 decode işlemi kaç kere yapılsın: "))
b64 = open(d, "r")
b64r=b64.read()
read_bytes=b64r.encode("utf-8")
for i in range (0,isl):
	read_bytes = base64.b64decode(read_bytes)
	base64_string=read_bytes.decode("utf-8")	
b64.close()
print(Fore.RED) 	
print(base64_string)
print("\n")

