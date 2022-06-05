import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ur = s.getsockname()[0]+":800"
cmd1 = "start chrome "+ur
a = subprocess.run(cmd1, shell=True, capture_output=True)
s.close()
