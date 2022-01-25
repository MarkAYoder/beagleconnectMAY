#!/usr/bin/env python3
import socket
import sys
import struct
import time

import re

# print ("Opening socket")
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# print ("binding...")
sock.bind(('', 9999))
# print ("Setting opt")
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_LOOP, True)
mreq = struct.pack("16s15s".encode('utf-8'), socket.inet_pton(socket.AF_INET6, "ff02::1"), (chr(0) * 16).encode('utf-8'))
# print ("JOIN_GROUP")
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

# print ("Entering while True")
while True:
  # print ("In while True")
  data, sender = sock.recvfrom(1024)
  print (str(sender) + '  ' + repr(data))
  # print(data)
  # print(str(data))

  # Check for brightness
  r1 = re.findall(r"l:([\d\.]+)", str(data))
  if len(r1) > 0:
    lux = float(r1[0])
    print(float(lux))

  # Check for humidity
  r1 = re.findall(r"h:([\d\.]+)", str(data))
  if len(r1) > 0:
    hum = float(r1[0])
    print(float(hum))

  # Check for temp
  r1 = re.findall(r"t:([\d\.]+)", str(data))
  if len(r1) > 0:
    temp = float(r1[0])
    print(float(temp))

