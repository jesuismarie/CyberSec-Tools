import hashlib
import sys

def parse_wordlist(passlst_path):
	try:
		with open(passlst_path, 'r', encoding='utf-8', errors='ignore') as f:
			return [line.strip() for line in f if line.strip()]
	except FileNotFoundError:
		print(f"[✗] Wordlist file not found: {passlst_path}")
		print("===============================================================")
		sys.exit(1)

def hash_word(word, algorithm):
	try:
		hash_func = getattr(hashlib, algorithm.lower())
	except KeyboardInterrupt:
		print("\nScan interrupted by user.")
		sys.exit(1)
	except AttributeError:
		print(f"[✗] Unsupported hash algorithm: {algorithm}")
		print("===============================================================")
		sys.exit(1)

	return hash_func(word.encode('utf-8')).hexdigest()

def crack_hash(target_hash, algorithm, passlst_path):
	print("===============================================================")
	print(f"[~] Hash:\t{target_hash}")
	print(f"[~] Algorithm:\t{algorithm}")
	print(f"[~] Passlist:\t{passlst_path}")
	print("===============================================================")

	words = parse_wordlist(passlst_path)
	for word in words:
		if hash_word(word, algorithm) == target_hash.lower():
			print("===============================================================")
			print(f"[✓] Hash cracked! {word}")
			print("===============================================================")
			return

	print("===============================================================")
	print("[✗] Password not found in passlist.")
	print("===============================================================")

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("Usage: python hash_cracker.py <hash> <algorithm> <passlist>")
	else:
		hash = sys.argv[1]
		algorithm = sys.argv[2]
		passlst_path = sys.argv[3]
		crack_hash(hash, algorithm, passlst_path)
