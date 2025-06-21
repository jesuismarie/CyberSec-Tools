# 🛠️ CyberSec-Tools

A curated collection of offensive security tools written, developed for learning, testing, and practicing ethical hacking and penetration testing techniques. Each tool targets a specific phase of ethical hacking — from reconnaissance to exploitation and analysis.

Whether you're learning cybersecurity or building a personal toolkit, this repo provides practical, hands-on utilities to explore network scanning, brute-force attacks, enumeration, and more.

---

## 🔍 1. Network Scanner

Scans a target IP for open TCP ports and attempts to identify the services running on them. Useful for basic reconnaissance and enumeration during penetration testing.

### 📌 Features

* Pings the host to check if it's reachable
* Scans ports from `1` to `65535`
* Displays:

  * Open ports
  * Service names (where available)
* Clean and informative CLI output

### 🚀 Usage

```bash
python3 network_scanner.py <ip-address>
```

#### Example:

```bash
python3 network_scanner.py 192.168.1.1
```

#### Output:

```
---------------------------------------------------------------
Scan report for 192.168.1.1
---------------------------------------------------------------
Starting port scan...
---------------------------------------------------------------
PORT            STATE           SERVICE
22              open            ssh
80              open            http
443             open            https
...
---------------------------------------------------------------
Scan complete.
```

### ⚙️ How It Works

* Sends an ICMP ping to check if the host is reachable.
* Iterates through ports 1–65535 using `socket.connect_ex()`.
* Uses `socket.getservbyport()` to identify common services.

### 📦 Requirements

* Python 3.x
* Linux/macOS (uses `ping -c` and redirects with `> /dev/null`)

> ⚠️ This script may not work properly on Windows due to differences in the `ping` command syntax.

---

## 📁 2. Directory Enumerator

Performs brute-force directory and file discovery on a given web server using a user-provided wordlist. Helps identify hidden or restricted paths that may expose sensitive content during a web application penetration test.

### 📌 Features

* Validates if the target URL is reachable
* Scans for directories/files using a custom wordlist
* Detects `200 OK` (found) and `403 Forbidden` (restricted) resources
* Clean CLI output with real-time results

### 📦 Installation

Use a virtual environment and install dependencies from `requirements.txt`:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🚀 Usage

```bash
python directory_enumeration.py <url> <wordlist>
```

#### Example:

```bash
python directory_enumeration.py http://example.com common.txt
```

#### Output:

```
===============================================================
[+] Url:                    http://example.com
[+] Wordlist:               common.txt
[✓] Server reachable:       http://example.com (Status: 200)
===============================================================
Starting directory enumeration...
===============================================================
[+] Found: http://example.com/admin (200 OK)
[-] Forbidden (403): http://example.com/hidden
...
[-] No directories found.
```

### ⚙️ How It Works

* Loads a list of directory names from the given wordlist.
* Sends a GET request to each potential path using the base URL.
* Checks HTTP response status codes:

  * `200 OK` indicates the path exists.
  * `403 Forbidden` indicates the path exists but is restricted.
* Gracefully handles unreachable hosts or keyboard interrupts.

### 📦 Requirements

* Python 3.x
* [`requests`](https://pypi.org/project/requests/)

> ⚠️ Ensure the wordlist file exists and is properly formatted (one path per line).
