import requests
import re
from fetcher import __fetcher__


moviename = input("Enter movie name: ").strip().replace(" ","%20")

def fetch(movie):
    
    base_url = f"https://www.1377x.to/search/{moviename}/1/"

    html_torrent = requests.get(base_url).text
    
    torrent_page_link = re.search(r"(torrent\/[0-9]{7}\/[a-zA-Z0-9-]*\/)",html_torrent)
    torrent_link = torrent_page_link.group(0)

    base_for_magnet = f"https://1337x.to/{torrent_link}"
    html_magnet = requests.get(base_for_magnet).text
    magnet = re.search(r"(magnet:\?xt=urn:btih:[a-zA-Z0-9]*)",html_magnet)
    magnet_link = magnet.group(0)
    print(magnet_link)
    return magnet_link
   

magnet_link = fetch(moviename)
__fetcher__(magnet_link)


