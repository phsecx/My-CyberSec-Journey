#!/bin/bash

echo "===== Disk Usage Report ====="
df -h

echo ""
echo "⚠️ Checking partitions above 80% usage:"
df -h | awk '$5 >= 80 {print $0}'