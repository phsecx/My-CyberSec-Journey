#!/bin/bash

echo "===== System Information ====="
echo "Hostname: $(hostname)"
echo "OS: $(uname -o)"
echo "Kernel Version: $(uname -r)"
echo "Architecture: $(uname -m)"
echo "Uptime:"
uptime