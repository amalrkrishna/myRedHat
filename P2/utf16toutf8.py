#!/usr/bin/env python

"""utf16toutf8.py: Write a program in Python to convert UTF-16 to UTF-8 for values in range of U+0000 to U+07FF.
User will input UTF-16 (a2) and output will be UTF-8 bytes. (c2 a2)
UTF-16 to UTF-8 conversion happens in following way."""

__author__      = "Amal Krishna R"
__date__      = "05/07/2016"

#loop to check the input format and range.
while True:
	utf16 = input("UTF-16 code point: ")
	if utf16[:3] == "U+0" and (len(utf16)) == 6 and 0 <= int(utf16[2:], 16) < 2048:
		break
	else:
		print("Format ex: 'U+00A2' in the range of U+0000 to U+07FF.")

#convert utf16 to integer and binary code point.
utf16 = utf16[2:]
utf16int = int(utf16,16)
utf16bin = bin(int(utf16, 16))[2:]

#add necessary bits to 7 bits and 11 bits code point.
if(0<= utf16int <= 127):
	utf8bin="0"+utf16bin
elif(128<= utf16int <= 2047):
	utf8bin = "110"+utf16bin[-5:]+"10"+utf16bin[-6:]

#convert utf8bin to utf8int and uft8hex code point.
utf8int = int(utf8bin,2)
utf8hex = hex(utf8int)[2:]

#display the final UTF-8 value.
print (("UTF-8 code point: %s") % utf8hex)
