#!/bin/bash
sudo apt install -r python3.10 python3-pip python3-tk
pip install -r requirements.txt
python3.10 src/Checker.py
