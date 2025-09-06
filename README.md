# Website_Dos_Attack_Script
This project is created **strictly for educational purposes**.
It demonstrates how multiple threads and sockets can be used to simulate high-traffic conditions on a server.  
**Do not use this tool on any system, server, or network without explicit authorization.**  
Misuse of this code may violate laws and result in severe consequences.  

---

## 📖 Overview
This Python script simulates a **Denial-of-Service (DoS) attack** scenario in a controlled environment.  
It helps students and developers understand:
- How TCP connections are established with sockets.
- How threading can generate concurrent network traffic.
- How servers may respond under simulated high load.

---

## ⚙️ Features
- Resolves a domain to its IP address.
- Sends repeated TCP connection requests to the specified target.
- Multithreaded execution for simulating concurrent traffic.
- Console messages to observe packet sending attempts.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Basic understanding of networking (IP, TCP, sockets).

### Installation
Clone the repository:
```bash
git clone https://github.com/uncle-joshi/Website_Dos_Attack_Script.git
cd Website_Dos_Attack_Script
```

```
Run
python dos_attack.py
```

You will be prompted to enter:
A target URL (domain).
The resolved IP address of the target.

🧪 Safe Testing

To safely test this tool:
Create a local web server (e.g., using Python’s http.server).
```
python -m http.server 8080
```
Run this script against localhost or your own server in a controlled lab environment.
Monitor how the server handles the connections.

📚 Learning Value

This project demonstrates:
Networking basics with Python’s socket library.
Multithreading using the threading module.
Real-world implications of denial-of-service conditions.

⚖️ Legal Notice

This software must only be used on systems you own or have explicit permission to test.
The author(s) and contributor(s) are not responsible for misuse.
