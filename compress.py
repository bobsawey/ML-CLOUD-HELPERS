#compress.py
import os
import sys
import uuid

#process args
def tarxz(sys.argv[1]):
  filename = generate_filename()
  os.system(f"tar -vcf - {sys.argv[1]} | xz -v9e --threads=8 -c - > {filename}")
def generate_filename(ext="txz"):
  return f"{uuid.uuid4()}.txz"
