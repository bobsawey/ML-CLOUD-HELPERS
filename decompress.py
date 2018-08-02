#decompress.py
#$ decompress filename.txz
import os
import sys

#process args
def untarxz(filename=sys.argv[1]):
  os.system(f"tar -xvJf{filename}")
