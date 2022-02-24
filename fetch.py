import requests
import re

moviename = input("Enter movie name: ").replace(" ","%20")

def fetch(movie):
    

    print(moviename)
    base_url = f"https://www.1377x.to/search/{moviename}/1/"
    print(base_url)
    html_torrent = requests.get(base_url).text
    
    torrent_page_link = re.search(r"(torrent\/[0-9]{7}\/[a-zA-Z0-9-]*\/)",html_torrent)
    torrent_link = torrent_page_link.group(0)
    print(torrent_link)

    base_for_magnet = f"https://1337x.to/{torrent_link}"
    html_magnet = requests.get(base_for_magnet).text
    magnet = re.search(r"(magnet:\?xt=urn:btih:[a-zA-Z0-9]*)",html_magnet)
    magnet_link = magnet.group(0)
    print(magnet_link)


fetch(moviename
      
#  hello anki
