import re
import sys

HASH_PATTERNS = {
	'MD5':			r'^[a-f0-9]{32}$',
	'SHA-1':		r'^[a-f0-9]{40}$',
	'SHA-224':		r'^[a-f0-9]{56}$',
	'SHA-256':		r'^[a-f0-9]{64}$',
	'SHA-384':		r'^[a-f0-9]{96}$',
	'SHA-512':		r'^[a-f0-9]{128}$',
	'NTLM':			r'^[a-f0-9]{32}$',
	'MySQL5':		r'^\*[A-F0-9]{40}$',
	'bcrypt':		r'^\$2[aby]?\$\d{2}\$[A-Za-z0-9./]{53}$',
	'Base64':		r'^[A-Za-z0-9+/=]{20,}$',
	'RIPEMD-160':	r'^[a-f0-9]{40}$',
	'Whirlpool':	r'^[a-f0-9]{128}$',
	'LM':			r'^[a-f0-9]{32}$',
	'MD4':			r'^[a-f0-9]{32}$',
	'CRC32':		r'^[a-f0-9]{8}$',
	'Adler32':		r'^[a-f0-9]{8}$',
	'SHA-3 (224)':	r'^[a-f0-9]{56}$',
	'SHA-3 (256)':	r'^[a-f0-9]{64}$',
	'SHA-3 (384)':	r'^[a-f0-9]{96}$',
	'SHA-3 (512)':	r'^[a-f0-9]{128}$'
}

def is_valid_hex(s):
	return bool(re.match(r'^[0-9a-fA-F]+$', s))

def identify_hash(hash_string):
	hash_string = hash_string.strip()
	length = len(hash_string)
	results = []

	for hash_type, pattern in HASH_PATTERNS.items():
		if re.fullmatch(pattern, hash_string, re.IGNORECASE):
			results.append(hash_type)

	if length == 32:
		try:
			if all(hash_string[i] == '0' for i in range(16, 32)):
				results.append('LM (second half)')
				if 'LM' in results:
					results.remove('LM')
		except IndexError:
			pass

	if length == 40:
		results.sort()

	return results

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python hash_identifier.py <hash>")
	else:
		hash_input = sys.argv[1].strip()
		if not any(re.match(pattern, hash_input, re.IGNORECASE) for pattern in 
				[HASH_PATTERNS['MySQL5'], HASH_PATTERNS['bcrypt'], HASH_PATTERNS['Base64']]):
			if not is_valid_hex(hash_input):
				print("===============================================================")
				print("[✗] Hash is not valid.")
				print("===============================================================")
				sys.exit(1)
		
		results = identify_hash(hash_input)
		print("===============================================================")
		if results:
			print(f"[✓] Possible hash type(s): {', '.join(results)}")
		else:
			print("[✗] Could not identify the hash type.")
		print("===============================================================")