from pathlib import Path

def scan_directory(path: str, sort_by="size", reverse=False):
  p = Path(path)
  files = [x for x in p.iterdir() if x.is_file()]
  if sort_by == "name":
    return sorted(files, key=lambda f: f.name.lower(), reverse=reverse)
  elif sort_by == "size":
    return sorted(files, key=lambda f: f.stat().st_size, reverse=reverse)
  elif sort_by == "date":
    return sorted(files, key=lambda f: f.stat().st_mtime, reverse=reverse)