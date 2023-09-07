# Network Packet Processor
A Python project with software verification, performance testing.

Project Overview
The project will simulate a "**Network Packet Processor**"

My verification tool will:
1. Conduct unit tests to verify the functionality of each packet processing function.
2. Perform performance benchmarks on these packet processing functions.
3. Include a GitHub Actions YAML configuration file for automated tests, build and test pipeline (demonstrating my knowledge in CI tools).


## Prerequisites
1. Python 3.x
2. Pytest: for testing
3. Pytest-benchmark: for performance testing
Install using pip:
```
pip install pytest pytest-benchmark
```

## Project Structure
1. 'packet_processor.py': Simulates a simple network packet processor.
2. 'test_packet_processor.py': Includes both functional and performance tests.
3. '.github/workflows/main.yml': GitHub Actions configuration for CI.


## General usage
1. Clone the project.
2. Add these files into the repository.
3. Push the code to GitHub.
4. Go to your GitHub repository, navigate to 'Actions', and see your tests running automatically


The code consists of two main parts: a module for processing network packets (packet_processor.py) and a set of unit tests for that module (test_packet_processor.py).

packet_processor.py
This file simulates some basic operations you might perform on network packets.

There are also performance tests (benchmarks) for the checksum, encrypt, and decrypt functions. These tests measure how long these functions take to process large packets.
