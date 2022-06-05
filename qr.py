import pyqrcode
t = "dfsdreere"
url = pyqrcode.create(t)
url.svg('./filesdir/images/url-qr.svg', scale=8)
url.png('./filesdir/images/url-r.png', scale=8)
print(url.terminal(quiet_zone=1))

import qrcode
img = qrcode.make('Some data here')
