import socket
import time

startTime = time.time()

ip = input(str('[->] Hedef Ip Adresi: '))
print('[...] Hedef Taranıyor: ', ip)

for port in range(1, 64738):
    int(port)
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    baglanti = soket.connect_ex((ip, port))
    if (baglanti == 0):
        print('[+] Port %d: AÇIK' % (port,))
    soket.close()
print('Geçen süre:', time.time() - startTime)
