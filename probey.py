import sys
import requests


#function will check which domains are active or not
def urls(out_file):
	read_url = sys.stdin.read().splitlines()

	good_url = []
	bad_url = []


	for url in read_url:
		try:
			response = requests.head(url)

			if response.status_code == 200:
				good_url.append(url)

		except requests.exceptions.MissingSchema:
			bad_url.append(url)
			continue
		
		except requests.exceptions.ConnectionError:
			bad_url.append(url)
			continue

	with open(out_file, "w") as file:
		file.write('\n'.join(good_url))


	print(f"[*] Saved URLS {out_file}")

out_file = "filtered_urls.txt"
urls(out_file)
