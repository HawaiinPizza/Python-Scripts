#!/bin/python
import os

abspath = os.path.abspath("/home/zaki/Projects/Programm/bookmarks/")
os.chdir(abspath)
print(os.getcwd())
from . import bookmarks
# import bookmarks
