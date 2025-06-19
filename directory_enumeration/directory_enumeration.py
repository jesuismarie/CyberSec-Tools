import requests
import sys
from urllib.parse import urljoin

def dir_enumeration(url, wordlist_path):
	try:
		file = open(wordlist_path, 'r')
	except Exception as e:
		print(f"Wordlist {wordlist_path} not found")
		sys.exit(1)

	word_lst = file.readlines()
	file.close()
	print("===============================================================")
	print(f"[+] Url:\t\thttp://{url}")
	print(f"[+] Wordlist:\t\t{wordlist_path}")
	print("===============================================================")
	print("Starting directory enumeration...")
	print("===============================================================")
	for word in word_lst:
		try:
			test_url = urljoin(url, word)
			response = requests.get(test_url, timeout=5)
			if response.status_code == 200:
				print(f"[+] Found: {test_url} (200 OK)")
			elif response.status_code == 403:
				print(f"[-] Forbidden (403): {test_url}")
		except requests.RequestException as e:
			print(f"[!] Error requesting {test_url}: {e}")

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: python3 directory_enumeration.py <url> <wordlist.txt>")
	else:
		url = sys.argv[1]
		wordlist_path = sys.argv[2]
		dir_enumeration(url, wordlist_path)
