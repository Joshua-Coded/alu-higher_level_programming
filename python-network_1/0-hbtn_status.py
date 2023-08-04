#!/usr/bin/python3
"""Python script that fetches https://alu-intranet.hbtn.io/status"""


import urllib.request


if _name_ == '_main_':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
