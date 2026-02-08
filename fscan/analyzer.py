from pathlib import Path
from datetime import datetime

def analyze_files(files: list[Path]) -> list[dict]:
  rows = []
  for f in files:
    stat = f.stat()
    rows.append({
        "name": f.name,
        "size": stat.st_size,
        "date": datetime.fromtimestamp(stat.st_mtime),
      })
  return rows