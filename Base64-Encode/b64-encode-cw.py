import os, sys, colorama, pyfiglet, base64
from colorama import Fore, Back, Style
print(Fore.GREEN) 
result = pyfiglet.figlet_format("CW-AGOLA-BASE64-ENCODE", font = "digital" )
print(result)
####################################
metin=input(Fore.WHITE+"Şifrelenmesini istediğiniz metni girin: "+"\n")
metin_bytes=metin.encode("utf-8")
isl=int(input(Fore.WHITE+"\nBase64 encode işlemi kaç kere yapılsın: "))

for i in range (0,isl):
	
	metin_bytes=base64.b64encode(metin_bytes)	
	base64_string=metin_bytes.decode("utf-8")
b64=open("base64_şifre.txt","w")
b64.write(base64_string)
b64.close()
