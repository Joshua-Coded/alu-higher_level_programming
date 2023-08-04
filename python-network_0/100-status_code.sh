#!/bin/bash
# status code
echo $(curl -s -I "$1" | grep -oE 'HTTP/1\.[0-9] [0-9]{3}')

