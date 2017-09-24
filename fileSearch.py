import os
import sys
from os.path import join

lookfor = "fileSearch.py"

for root, dirs, files in os.walk('C:\\'):
    print("searching"), root
    if lookfor in files:
        print "Found %s" % join(root, lookfor)
        break

