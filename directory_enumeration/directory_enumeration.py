import requests
import sys
from urllib.parse import urljoin

def is_host_reachable(url):
	try:
		test_response = requests.get(url, timeout=5)
		print(f"[✓] Server reachable:\t\t{url} (Status: {test_response.status_code})")
	except KeyboardInterrupt:
			print("\nScan interrupted by user.")
			sys.exit()
	except requests.RequestException:
		print(f"[✗] Server not reachable:\t{url}")
		print("===============================================================")
		sys.exit(1)

def parse_wordlst(wordlist_path):
	try:
		with open(wordlist_path, 'r') as file:
			word_lst = [line.strip() for line in file if line.strip()]
			return word_lst
	except Exception:
		print(f"Wordlist {wordlist_path} not found")
		sys.exit(1)

def dir_enumeration(url, wordlist_path):
	word_lst = parse_wordlst(wordlist_path)
	if not url.startswith('http'):
		url = 'http://' + url

	print("===============================================================")
	print(f"[+] Url:\t\t\thttp://{url}")
	print(f"[+] Wordlist:\t\t\t{wordlist_path}")
	is_host_reachable(url)
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
		except KeyboardInterrupt:
			print("\nScan interrupted by user.")
			sys.exit()
		except requests.RequestException:
			pass

	if not found:
		print("[-] No directories found.")

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: python directory_enumeration.py <url> <wordlist>")
	else:
		url = sys.argv[1]
		wordlist_path = sys.argv[2]
		dir_enumeration(url, wordlist_path)
