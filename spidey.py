import requests
from bs4 import BeautifulSoup
import urllib 
from urllib.parse import urljoin


visited_urls = set() #it will remoev duplicates of url


def spidey(url, keyword):
	try:
		response = requests.get(url)	
	except:
		print(f"[!] Request Failed {url}")
		return

	#scraping all links from URL, <a href="">
	
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')
		a_tag = soup.find_all("a")
		url_list = []
		
		for tag in a_tag:
			href_tag = tag.get("href")
			if href_tag is not None and href_tag != "":
				url_list.append(href_tag)
		#print(url_list)

		#removing duplicate links
		for i in url_list:
			if i not in visited_urls:
				visited_urls.add(i)
				
				url_join = urllib.parse.urljoin(url, i) #making absolute URL
				
				if keyword in url_join:
					print(url_join)
					spidey(url_join, keyword)
			else:
				pass


url = input("[*] Enter URL You Want To Scrape: ")
keyword = input("[*] Enter The KeyWord To Search For: ")
spidey(url, keyword)



