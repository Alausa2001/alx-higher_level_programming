#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the responsE
curl -X GET -sL "$1" 
