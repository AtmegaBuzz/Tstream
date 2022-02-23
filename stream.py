from bs4 import BeautifulSoup
import requests
from fetcher import __fetcher__

moviename = input("movie: ").replace(" ","+")
search_url = "https://www1.thepiratebay3.to/s/?q=" + moviename.replace(" ","+")


page = requests.get(search_url)
soup = BeautifulSoup(page.text,'html.parser')
link = soup.find_all('a',{'class':'detLink'})[0]['href']

movie_page = requests.get("https://www1.thepiratebay3.to/"+link)
soup = BeautifulSoup(movie_page.text,'html.parser')

magnet_div = soup.find_all('div',{'class':'download'})[0]

magnetlink = magnet_div.find('a')['href'].split("&")[0]

__fetcher__(magnetlink)


