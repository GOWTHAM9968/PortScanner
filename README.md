
# 🔍 Python Port Scanner

## Overview

Python Port Scanner is a cybersecurity project that scans a specified range of ports on a target host and identifies open ports. The project demonstrates socket programming, network fundamentals, and Python development skills.

## Features

* Scan custom port ranges
* Supports IP addresses and hostnames
* Detects open ports
* Attempts service identification
* Colored terminal output
* Scan summary report
* Saves results to a text file
* Error handling and validation

## Technologies Used

* Python 3
* Socket Programming
* Colorama

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-port-scanner.git
cd python-port-scanner
```

Install dependencies:

```bash
pip install colorama
```

## Usage

Run the program:

```bash
python port_scanner.py
```

Example:

```text
Enter IP Address or Hostname: localhost
Enter Start Port: 1
Enter End Port: 100
```

## Sample Output

```text
==================================================
PORT SCANNER v1.0
Cybersecurity Project
==================================================
Target : localhost
IP     : 127.0.0.1
Ports  : 1 - 100
==================================================

Port 22 OPEN (ssh)
Port 80 OPEN (http)

==================================================
SCAN SUMMARY
==================================================
Open Ports Found : 2
Scan Time        : 3.15 seconds
==================================================
```

## Project Structure

```text
python-port-scanner/
│
├── port_scanner.py
├── results.txt
├── requirements.txt
└── README.md
```

## Learning Outcomes

This project helped develop skills in:

* Python Programming
* Socket Programming
* Network Fundamentals
* Error Handling
* File Operations
* Cybersecurity Concepts
* Git & GitHub

## Future Improvements

* Graphical User Interface (GUI)
* CSV Report Export
* JSON Report Export
* Improved Logging
* Better Visualization Dashboard

## Disclaimer

This project is intended for educational purposes and authorized testing only. Always obtain proper permission before interacting with systems or networks.

## Author

**Vaddi Gowtham**

Cybersecurity Student | Python Learner | Ethical Hacking Enthusiast

GitHub: https://github.com/GOWTHAM9968

LinkedIn: Add your LinkedIn profile link here
