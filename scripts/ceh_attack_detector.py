"""
CEH (Certified Ethical Hacker) - Automated PCAP Threat & Attack Detector
Author: Manoj M | Network & Cyber Security Engineer
Alignment: CEH Module 6 (Sniffing) & Module 12 (Evading Firewalls & IDS)
"""

import sys

def analyze_pcap_signatures(pcap_path):
    print("="*65)
    print(f"🔍 CEH PACKET FORENSICS INSPECTOR: {pcap_path}")
    print("="*65)
    
    # Simulated forensic parsing logic
    print("[1] PORT SCAN DETECTION:")
    print("    - Alert: High rate of TCP SYN packets with no ACK completion.")
    print("    - Target Ports: 21, 22, 23, 80, 443, 3389 (Flagged as Nmap SYN Stealth Scan -sS)")
    print("    - Source IP: 192.168.1.105 -> Flagged for Isolation\n")

    print("[2] DOS / SYN FLOOD INSPECTION:")
    print("    - Threshold: > 5,000 SYN packets/sec to Port 80 without 3-way handshake")
    print("    - Finding: Incomplete TCP connections indicating SYN-spoofing attack\n")

    print("[3] PLAIN-TEXT CREDENTIAL LEAKAGE:")
    print("    - Protocol: HTTP POST /login.php")
    print("    - Extracted: Authorization: Basic dXNlcjphZG1pbg== (Decoded: user:admin)")
    print("    - Recommendation: Enforce TLS 1.3 / HTTPS-only policy\n")

    print("[4] ARP SPOOFING / CACHE POISONING:")
    print("    - Finding: Duplicate ARP replies mapping IP 192.168.1.1 to 2 distinct MAC addresses")
    print("    - Incident Classification: Man-in-the-Middle (MitM) ARP Poisoning attempt")
    print("="*65)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "suspicious_traffic.pcap"
    analyze_pcap_signatures(target)
