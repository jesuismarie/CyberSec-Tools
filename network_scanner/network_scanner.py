import sys
import socket
import os

def is_host_reachable(ip):
	try:
		response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
		if response != 0:
			print("---------------------------------------------------------------")
			print(f"Host not {ip} reachable.")
			print("---------------------------------------------------------------")
			sys.exit(1)
	except KeyboardInterrupt:
		print("\nScan interrupted by user.")
		sys.exit()

def network_scanner(ip):
	print("---------------------------------------------------------------")
	print(f"Scan report for {ip}")
	is_host_reachable(ip)
	print("---------------------------------------------------------------")
	print("Starting port scan...")
	print("---------------------------------------------------------------")
	print("PORT\t\tSTATE\t\tSERVICE")

	found = False

	for port in range(1, 65536):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(0.5)
			result = sock.connect_ex((ip, port))

			if result == 0:
				try:
					service = socket.getservbyport(port)
				except:
					service = "unknown"
				found = True
				print(f"{port}\t\topen\t\t{service}")
			sock.close()
		except KeyboardInterrupt:
			print("\nScan interrupted by user.")
			sys.exit()
		except Exception:
			continue

	if not found:
		print("No ports found.")
	print("---------------------------------------------------------------")
	print("Scan complete.")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 network_scanner.py <ip>")
	else:
		ip = sys.argv[1]
		network_scanner(ip)