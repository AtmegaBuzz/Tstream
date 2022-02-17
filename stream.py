#!/usr/bin/env python3

import re
import os


inputname = input("Enter the name of movie, series or magnetlink to search:")
name = inputname.replace(" ","+")
print("Looking for: ",name)
if re.search("magnet:\?xt=urn:btih:[a-zA-Z0-9]*",name):
	peerflixcommand1 = "peerflix --mpv "+"\""+name+"\""
	os.system(peerflixcommand1)

x = " https://1337x.to/search/"
greptorrentlink = ('curl -s https://1337x.to/search/%s/1/ | grep -Eo "torrent\/[0-9]{7}\/[a-zA-Z0-9-]*\/" | head -n 1' %name)
link = os.popen(greptorrentlink).read()
print("Found it! \n",link)
fulllink = ('curl -s https://1337x.to/%s | grep -Po "magnet:\?xt=urn:btih:[a-zA-Z0-9]*" | head -n 1' %link)
fl = fulllink.replace("\n"," ")

magnetlink = os.popen(fl).read()
print (magnetlink)


peerflixcommand2 = "peerflix --mpv "+magnetlink+" -a"
os.system(peerflixcommand2)
