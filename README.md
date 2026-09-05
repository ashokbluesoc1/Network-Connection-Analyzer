\# Network Connection Analyzer



A Python-based cybersecurity tool that analyzes network connection logs and identifies potentially suspicious network activity.



\## How It Works



The program reads network connection events from a log file and extracts:



\- Source IP address

\- Source port

\- Destination IP address

\- Destination port

\- Protocol



The analyzer then applies detection rules to identify connections that may require investigation.



\## Detection Rules



\### 1. Suspicious Port Detection



The program checks whether a connection is made to ports included in a predefined list of interesting ports.



Current ports monitored:



\- 4444

\- 1337

\- 31337



A connection to one of these ports is flagged for investigation.



\### 2. Repeated Connection Detection



The program tracks communication between a source IP and destination IP.



If the same source communicates with the same destination 5 times, the program generates a repeated connection alert.



\## Example Network Event



SRC\_IP=192.168.1.10 | SRC\_PORT=50001 | DST\_IP=10.10.10.10 | DST\_PORT=443 | PROTOCOL=TCP



\## Example Alerts



\### Suspicious Port Alert



⚠️ Connection to suspicious port



Source IP: 192.168.1.20  

Destination IP: 185.220.101.1  

Action: Investigate communication



\### Repeated Connection Alert



⚠️ REPEATED CONNECTION ALERT



Source IP: 192.168.1.30  

Destination IP: 10.10.10.10  

Connection count: 5  

Action: Investigate repeated communication



\## Concepts Used



\- Python file handling

\- String parsing

\- Dictionaries

\- Sets

\- Conditional statements

\- Connection tracking

\- Threshold-based detection



\## Disclaimer



This project is a learning-focused network analysis tool. A connection to an unusual port or repeated communication alone does not prove malicious activity. Alerts should be investigated using additional context.

