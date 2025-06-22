# 🛠️ CyberSec-Tools

A curated collection of offensive security tools written, developed for learning, testing, and practicing ethical hacking and penetration testing techniques. Each tool targets a specific phase of ethical hacking — from reconnaissance to exploitation and analysis.

Whether you're learning cybersecurity or building a personal toolkit, this repo provides practical, hands-on utilities to explore network scanning, brute-force attacks, enumeration, and more.

## Table of Content

- [🔍 Network Scanner](#-1-network-scanner)
- [📁 Directory Enumeration](#-2-directory-enumerator)
- [🌐 Subdomain Discovery](#-3-subdomain-discovery)
- [🔐 SSH Brute Forcer](#-4-ssh-brute-forcer)
- [🧾 Hash Identifier](#-5-hash-identifier)
- [🧨 Hash Cracker](#-6-hash-cracker)
- [📊 Log Analyzer](#-7-log-analyzer)
- [🎣 Email Phishing Detector](#-8-email-phishing-detector)
- [💣 Custom Metasploit Module](#-9-custom-metasploit-module)

---

## 🔍 1. Network Scanner

### 📄 Description

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
python network_scanner.py <ip-address>
```

#### Example:

```bash
python network_scanner.py 192.168.1.1
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

### 📄 Description

Performs brute-force directory and file discovery on a given web server using a user-provided wordlist. Helps identify hidden or restricted paths that may expose sensitive content during a web application penetration test.

### 📌 Features

* Validates if the target URL is reachable
* Scans for directories/files using a custom wordlist
* Detects `200 OK` (found) and `403 Forbidden` (restricted) resources
* Clean CLI output with real-time results

### 📦 Installation

Use a virtual environment and install dependencies from `requirements.txt`:

```bash
python -m venv venv
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
* `requests` library

> ⚠️ Ensure the wordlist file exists and is properly formatted (one path per line).

---

## 🌐 3. Subdomain Discovery

### 📄 Description

Performs subdomain brute-forcing for a given domain using a custom wordlist. Helps uncover hidden or unlisted subdomains during the reconnaissance phase of web application penetration testing.

### 📌 Features

* Validates if the base domain is reachable
* Uses DNS resolution to identify live subdomains
* Supports custom wordlists for flexible enumeration
* Clean, informative CLI output

### 📦 Installation

Use a virtual environment and install dependencies from `requirements.txt`:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🚀 Usage

```bash
python subdomain_discovery.py <domain> <wordlist>
```

#### Example:

```bash
python subdomain_discovery.py example.com subdomains.txt
```

#### Output:

```
===============================================================
[+] Domain:      example.com
[+] Wordlist:    subdomains.txt
===============================================================
Starting subdomain discovery...
===============================================================
[+] Found: admin.example.com
[+] Found: dev.example.com
...
[-] No subdomains found.
```

### ⚙️ How It Works

* Loads a list of potential subdomain prefixes from the wordlist.
* Appends each prefix to the base domain (e.g., `admin.example.com`).
* Uses `dns.resolver` to check for valid DNS A records.
* If the subdomain resolves, it is considered "found".

### 📦 Requirements

* Python 3.x
* `dnspython` library

> ⚠️ Ensure the wordlist contains one subdomain prefix per line (e.g., `admin`, `mail`, `test`). Do not include full domain names in the wordlist.

---

Here's the complete and consistent `README` for your **SSH Brute Forcer** tool, following the same style as the previous tools:

---

## 🔐 4. SSH Brute Forcer

### 📄 Description

Attempts to brute-force SSH login using a list of usernames and passwords. Intended for controlled environments such as CTFs or lab testing.

### 📌 Features

* Checks if the SSH service is reachable on the target
* Attempts to log in using a wordlist of passwords
* Displays successful login credentials (if found)
* Handles connection timeouts and interruptions gracefully

### 📦 Installation

Set up a virtual environment and install dependencies from `requirements.txt`:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🚀 Usage

```bash
python3 ssh_brute_force.py <target> <username> <passlist>
```

#### Example:

```bash
python3 ssh_brute_force.py 192.168.1.10 root passwords.txt
```

#### Output:

```
===============================================================
[+] Target:		192.168.1.10
[+] Username:		root
[+] Wordlist:		passwords.txt
[✔] Target 192.168.1.10:22 is reachable.
===============================================================
Starting SSH brute-force...
===============================================================
[~] Trying: root:123456
[~] Trying: root:toor
[~] Trying: root:letmein
...
===============================================================
[✔] Success! Username: root | Password: toor
===============================================================
```

### ⚙️ How It Works

* Verifies the SSH port (default `22`) is open using `socket.create_connection()`.
* Reads passwords from a wordlist file.
* Uses `paramiko` to attempt SSH login with each password.
* Stops upon successful login, or reports failure if no credentials work.

### 📦 Requirements

* Python 3.x
* `paramiko` library
