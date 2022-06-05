# import pyqrcode
# import png
# from pyqrcode import QRCode
# s = "www.geeksforgeeks.org"
# url = pyqrcode.create(s)
# url.png('./filesdir/images/urlqr.png', scale = 6)



import socket
import subprocess

# pass
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("go to ",s.getsockname()[0]+":800"," to start shareing")
# print("go to ",s.getsockname()[0]+":800","to start shareing")
ur = s.getsockname()[0]+"800"
s.close()

import pyqrcode
import png
from pyqrcode import QRCode
s = "http://" + s.getsockname()[0] +":800"      
url = pyqrcode.create(s)
url.png('./filesdir/images/urlqr.png', scale = 6)

