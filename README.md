# NetScopePro – Advanced Network & Web Scanner

## Overview
NetScopePro is a Python-based advanced network and web reconnaissance tool.  
It performs multithreaded TCP port scanning, banner grabbing, service detection, basic OS fingerprinting, and risk scoring.  
All scan reports and logs are automatically saved in the `output/` folder.

---

## Features

- Full-range TCP port scanning (1–65535 ports)
- Multithreaded for faster scanning
- Banner grabbing for open ports
- Extended service detection using port database
- Basic OS fingerprinting (Windows / Linux / Web server)
- Risk scoring engine with security recommendations
- Detailed scan logging
- Reports automatically saved in `output/` folder
- Ethical scanning notice

---

## Installation

1. Make sure Python 3.x is installed on your system.
2. Download or clone this repository.
3. Install required Python packages (if any):

```bash
pip install -r requirements.txt
