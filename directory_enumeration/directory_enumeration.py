import requests
import sys
from urllib.parse import urljoin

def dir_enumeration(url, wordlist_path):
	try:
		with open(wordlist_path, 'r') as file:
			word_lst = [line.strip() for line in file if line.strip()]
	except Exception:
		print(f"Wordlist {wordlist_path} not found")
		sys.exit(1)

	if not url.startswith('http'):
		url = 'http://' + url

	print("===============================================================")
	print(f"[+] Url:\t\t\thttp://{url}")
	print(f"[+] Wordlist:\t\t\t{wordlist_path}")

	try:
		test_response = requests.get(url, timeout=5)
		print(f"[✓] Server reachable:\t\t{url} (Status: {test_response.status_code})")
	except requests.RequestException:
		print(f"[✗] Server not reachable:\t{url}")
		print("===============================================================")
		sys.exit(1)

	print("===============================================================")
	print("Starting directory enumeration...")
	print("===============================================================")

	found = False
	for word in word_lst:
		test_url = urljoin(url.rstrip('/') + '/', word)
		try:
			response = requests.get(test_url, timeout=5)
			if response.status_code == 200:
				print(f"[+] Found: {test_url} (200 OK)")
				found = True
			elif response.status_code == 403:
				print(f"[-] Forbidden (403): {test_url}")
				found = True
		except requests.RequestException:
			continue

	if not found:
		print("[-] No directories found.")

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: python3 directory_enumeration.py <url> <wordlist>")
	else:
		url = sys.argv[1]
		wordlist_path = sys.argv[2]
		dir_enumeration(url, wordlist_path)
