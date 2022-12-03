#!/usr/bin/env python3

from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import shutil
import sys


if len(sys.argv) > 1:
    day = str(sys.argv[1])
else:
    day = str(date.today().day)

if len(day) == 1:
    path = f'day0{day}'
else:
    path = f'day{day}'

try:
    os.mkdir(path)
except OSError:
    print (f'Creation of directory {path} failed')

shutil.copy('template.py', f'{path}/program.py')

with open(f'{path}/test.txt', 'w') as f:
    pass
with open(f'{path}/input.txt', 'w') as f:
    pass
