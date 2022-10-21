#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -I -s "$1" | grep Allow | cut -b 8-
