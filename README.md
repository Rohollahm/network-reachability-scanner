# Network Reachability Scanner

## Description
This project is a multi-threaded network reachability scanner written in Python.
It scans a user-defined IP range and detects which hosts are reachable using ICMP echo requests.

## Why this project matters
In real network environments, quickly identifying active hosts is essential for:
- Network troubleshooting
- Inventory building
- Detecting unauthorized devices

This tool is designed for small to medium networks and ISP environments.

## Features
- Concurrent scanning using ThreadPoolExecutor
- Timeout handling for unresponsive hosts
- Cross-platform support (Windows / Linux)
- Clean and readable output

## Usage
```bash
python reachability_scanner.py
