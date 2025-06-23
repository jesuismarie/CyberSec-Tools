import re
import sys

LOG_PATTERN = re.compile(
	r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+'
	r'\S+\s+\S+\s+'
	r'\[(?P<datetime>[^\]]+)\]\s+'
	r'"(?P<method>\w+)\s+(?P<url>[^\s]+)\s+\S+"\s+'
	r'(?P<status>\d{3})\s+(?P<size>\d+|-)'
)

def parse_log_line(line):
	match = LOG_PATTERN.match(line)
	return match.groupdict() if match else None

def add_to_dict(d, key):
	if key in d:
		d[key] += 1
	else:
		d[key] = 1

def sort_dict_by_value(d):
	return sorted(d.items(), key=lambda x: x[1], reverse=True)

def parse_file(file_path):
	try:
		with open(file_path, 'r') as f:
			lines = f.readlines()
			if not lines:
				print("===============================================================")
				print(f"[!] Log file {file_path} is empty.")
				print("===============================================================")
				sys.exit(1)
			return lines
	except FileNotFoundError:
		print("===============================================================")
		print(f"[✗] Log file {file_path} not found.")
		print("===============================================================")
		sys.exit(1)

def analyze_log(file_path):
	print("===============================================================")
	print(f"[~] Log file:\t{file_path}")
	lines = parse_file(file_path)
	print("===============================================================")

	ip_counts = {}
	url_counts = {}
	status_counts = {}

	for line in lines:
		parsed = parse_log_line(line)
		if not parsed:
			continue
		add_to_dict(ip_counts, parsed['ip'])
		add_to_dict(url_counts, parsed['url'])
		add_to_dict(status_counts, parsed['status'])

	print("\n📊 Top 5 IPs:")
	for ip, count in sort_dict_by_value(ip_counts)[:5]:
		print(f"{ip:15s} {count} requests")
	print("===============================================================")

	print("\n📄 Top 5 Requested URLs:")
	for url, count in sort_dict_by_value(url_counts)[:5]:
		print(f"{url:30s} {count} hits")
	print("===============================================================")

	print("\n📡 Status Code Summary:")
	for code, count in sorted(status_counts.items()):
		print(f"{code}: {count}")
	print("===============================================================")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python log_analyzer.py <access_log_file>")
	else:
		analyze_log(sys.argv[1])
