#!/usr/bin/python3
# Write a Python script that fetches https://alu-intranet.hbtn.io/status

import urllib.request

with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    html = response.read()
    decoded_html = html.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content:\n\t  Custom Status\n{}\n\t  Custom Status".format(decoded_html))
    print("\t- utf8 content: {}".format(decoded_html))
