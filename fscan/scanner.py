from os import scandir
from os.path import islink

def scan_directory(path: str, indent=0):
  with scandir(path) as entries:
    
    for entry in entries:
      print(" " * indent + entry.name)
      if entry.is_dir():
        scan_directory(entry.path, indent + 4)