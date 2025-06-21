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
