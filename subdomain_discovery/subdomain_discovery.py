import dns.resolver
import sys
import socket

def is_domain_reachable(domain):
	try:
		socket.gethostbyname(domain)
	except KeyboardInterrupt:
		print("\nScan interrupted by user.")
		sys.exit()
	except socket.gaierror:
		print("===============================================================")
		print(f"[✗] Domain {domain} not reachable.")
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

def check_subdomain(domain, wordlist_path):
	wordlst = parse_wordlst(wordlist_path)
	print("===============================================================")
	print(f"[+] Domain:\t\t{domain}")
	print(f"[+] Wordlist:\t\t{wordlist_path}")
	is_domain_reachable(domain)
	print("===============================================================")
	print("Starting subdomain discovery...")
	print("===============================================================")

	found = False

	for i in wordlst:
		try:
			sub_domain = f"{i}.{domain}"
			dns.resolver.resolve(sub_domain, "A")
			print(f"[+] Found: {sub_domain}")
			found = True
		except KeyboardInterrupt:
			print("\nScan interrupted by user.")
			sys.exit()
		except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout):
			pass

	if not found:
		print("[-] No subdomains found.")

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: python subdomain_discovery.py <domain> <wordlist>")
	else:
		domain = sys.argv[1]
		wordlst = sys.argv[2]
		check_subdomain(domain, wordlst)
