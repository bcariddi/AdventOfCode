#!/usr/bin/env python3

from datetime import date
import os
import shutil
import sys
from bs4 import BeautifulSoup
import requests


# Determine day to set up
if len(sys.argv) > 1:
    day = str(sys.argv[1])
else:
    day = str(date.today().day)

path = f'day{str(day).zfill(2)}'

# Create new directory
try:
    os.mkdir(path)
    print(f'✅ Created directory {path}') 
except OSError:
    print(f'❌ Creation of directory {path} failed, exiting')
    exit(1)
    
# Copy template program into directory
try:
    shutil.copy('template.py', f'{path}/program.py')
    print(f'✅ Copied template program to {path}/program.py')
except Exception:
    print(f'❌ Failed to copy template program')

# Create test input file
with open(f'{path}/test.txt', 'w') as f:
    print(f'✅ Created test input file {path}/test.txt')
    try:
        response = requests.get(f'https://adventofcode.com/2023/day/{day}')
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        test_input = soup.find('pre').text.strip()
        f.write(test_input)
        print(f'✅ Wrote test input to {path}/test.txt')
    except Exception:
        print(f'❌ Could not find test input, you will need to manually copy it')

# Create input file
with open(f'{path}/input.txt', 'w') as f:
    print(f'✅ Created empty input file {path}/input.txt')

