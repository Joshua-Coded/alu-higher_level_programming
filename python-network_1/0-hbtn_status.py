#!/usr/bin/python3
# Write a Python script that fetches https://alu-intranet.hbtn.io/status

import urllib.request

custom_status = b'Custom status'

with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    html = response.read()
    decoded_html = html.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(custom_status))
    print("\t- utf8 content: {}".format(decoded_html))
