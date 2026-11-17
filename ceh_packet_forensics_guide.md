# 🕵️ CEH Wireshark Filters & Packet Forensics Cheat Sheet

Production Wireshark display filters used by Ethical Hackers and SOC Analysts to pinpoint malicious network activities.

## 1. Reconnaissance & Port Scanning Detection
```wireshark
# Detect Nmap TCP SYN Stealth Scans (-sS)
tcp.flags.syn == 1 and tcp.flags.ack == 0 and tcp.window_size <= 1024

# Detect Nmap TCP Null Scans (-sN - no flags set)
tcp.flags == 0

# Detect Nmap TCP XMAS Scans (-sX - FIN, PSH, URG set)
tcp.flags.fin == 1 and tcp.flags.push == 1 and tcp.flags.urg == 1
```

## 2. Denial of Service (DoS) & Flooding
```wireshark
# Identify high-frequency TCP SYN floods
tcp.flags.syn == 1 and tcp.flags.ack == 0

# Identify ICMP Echo (Ping) flood attacks
icmp.type == 8
```

## 3. Clear-Text Credential & Data Exfiltration
```wireshark
# Filter HTTP POST requests transmitting login credentials
http.request.method == "POST"

# Filter FTP authentication attempts
ftp.request.command == "USER" or ftp.request.command == "PASS"

# Filter Telnet command sessions
telnet
```

## 4. Man-in-the-Middle (MitM) & ARP Spoofing
```wireshark
# Filter duplicate ARP replies for the same IP address
arp.duplicate-address-frame or arp.opcode == 2
```
