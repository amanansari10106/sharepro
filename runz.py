import socket
import subprocess
try:
    # pass
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("go to ",s.getsockname()[0]+":800"," to start shareing")
    # print("go to ",s.getsockname()[0]+":800","to start shareing")
    ur = s.getsockname()[0]+"800"

    import pyqrcode
    import png
    from pyqrcode import QRCode
    st = "http://" + s.getsockname()[0] +":800"      
    url = pyqrcode.create(st)
    url.png('./filesdir/images/urlqr.png', scale = 6)
    s.close()

except Exception as e:
    pass
    print("Connect Device to computer using wifi")
    print(e)

# qr part 
# import pyqrcode
# t = "dfsdreere"
# url = pyqrcode.create(t)
# url.svg('./filesdir/images/url-qr.svg', scale=8)
# print(url.terminal(quiet_zone=1))

# import qrcode
# img = qrcode.make('Some data here')
# img.save("./filesdir/images/qr-url.png")
#  end of qr part



cmd1 = ".\\envt2\\Scripts\\activate & python manage.py runserver 0.0.0.0:800"
print("Press CTRL + C to stop shareing")
a = subprocess.run(cmd1, shell=True, capture_output=True)
# a = subprocess.run(cmd1, shell=True, capture_output=True)



# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# print("go to ",s.getsockname()[0]+":800","to visit website")
