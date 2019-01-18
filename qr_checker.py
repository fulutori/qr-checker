#!/usr/bin/env python3
import sys
import io
import cgi
import os
import zbarlight
from PIL import Image

codes = set()
width = 500
height = 500

with open('qr.png', 'rb') as f:
	data = f.read()
image= Image.open(io.BytesIO(data))
result= zbarlight.scan_codes('qrcode', image)

for code in result:
	print(code.decode())
