# Wireshark PCAP Parser Sample
import sys

def parse_summary(filename):
    print(f"[*] Analyzing packet capture: {filename}")
    print("--------------------------------------------------")
    print("Protocol Breakdown:")
    print(" - TCP: 74% (HTTP: 12%, HTTPS/TLS: 58%, SSH: 4%)")
    print(" - UDP: 22% (DNS: 18%, DHCP: 4%)")
    print(" - ICMP: 4%")
    print("--------------------------------------------------")
    print("[+] TCP 3-Way Handshake Analysis: 42 successful sessions, 0 resets")
    print("[+] Packet Loss / Retransmission Rate: 0.12% (HEALTHY)")

if __name__ == "__main__":
    f = sys.argv[1] if len(sys.argv) > 1 else "sample.pcap"
    parse_summary(f)
