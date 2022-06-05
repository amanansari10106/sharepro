import socket
import subprocess

# cmd1 = "python manage.py runserver"
# a = subprocess.run(cmd1, shell=True, capture_output=True)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("go to ",s.getsockname()[0]+":800","to visit website")

s.close()