import typer
from fscan.scanner import scan_directory
from fscan.analyzer import analyze_files
from fscan.output import print_files
from datetime import datetime
import pyfiglet
import tomllib
import sys
from rich import print

app = typer.Typer(add_completion=False)

pyproject = tomllib.load(open("pyproject.toml", "rb"))
version = pyproject["project"]["version"]

text = "fscan"
ascii_art = pyfiglet.figlet_format(text, font='dos_rebel')

@app.command()
def scan(path: str =  typer.Argument("./", help="Choose a path to scan."), sort_by: str = typer.Option("name", "--sort-by", help="Sort by field (e.g., size, name, date)"), reverse: bool = typer.Option(False, "--reverse", "-r", help="Revers the sort? (e.g., big-small/small-big)")):
    now = datetime.now()
    formatted = now.strftime("%d/%m/%Y %H:%M:%S")
    print("-----------------------------")
    print(f"Date and time: {formatted}")
    print(f"Sorted by: {sort_by} & Reverse: {reverse}")
    print("-----------------------------")
    files = scan_directory(path, sort_by=sort_by, reverse=reverse)
    rows = analyze_files(files)
    print_files(rows, sort_by=sort_by, reverse=reverse)
  
@app.callback(invoke_without_command=True)
def main():
    if len(sys.argv) == 1:
        print(ascii_art)
        print("[cyan]Welcome[/cyan] to fscan!")
        print(f"Version: {version}")
  
if __name__ == "__main__":
  app()