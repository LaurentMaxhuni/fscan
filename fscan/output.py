from rich import print
from rich.table import Table

def print_files(rows: list[dict], sort_by: str, reverse: bool) -> None:
  direction = "desc" if reverse else "asc"
  table = Table(title="Scan Results")
  table.add_column("File Name")
  table.add_column(f"{sort_by.title()} ({direction})")
  
  for row in rows:
    value = row[sort_by]
    if sort_by == "size":
      value = f"{value:,} B"
    elif sort_by == "date":
      value = value.strftime("%Y/%m/%d %H:%M:%S")
    table.add_row(row["name"], str(value))
  print(table)