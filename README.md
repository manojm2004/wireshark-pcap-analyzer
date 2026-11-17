# 🔍 Wireshark PCAP Packet Inspector & Protocol Analyzer

A Python tool designed to automate PCAP traffic analysis for Network Operations Centers (NOC).

## 🚀 Features
- Identifies TCP 3-way handshake completion (`SYN`, `SYN-ACK`, `ACK`).
- Flags TCP Retransmissions and Duplicate ACKs (indicators of network congestion/packet loss).
- Summarizes bandwidth distribution by protocol (HTTP, DNS, TLS, ICMP).
