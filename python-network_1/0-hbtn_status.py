#!/usr/bin/python3
# Write a Python script that fetches https://alu-intranet.hbtn.io/status

import urllib.request

custom_status = b'Custom status'
decoded_custom_status = custom_status.decode('utf-8')

print("Body response:")
print("\t- type: {}".format(type(custom_status)))
print("\t- content: {}".format(custom_status))
print("\t- utf8 content: {}".format(decoded_custom_status))
