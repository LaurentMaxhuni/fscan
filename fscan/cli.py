import typer
from fscan.scanner import scan_directory
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
def scan(path: str =  typer.Argument("./", help="Choose a path to scan.")):
    now = datetime.now()
    formatted = now.strftime("%d/%m/%Y %H:%M:%S")
    print("-----------------------------")
    print(f"Date and time: {formatted}")
    print("-----------------------------")
    files = scan_directory(path)
  
@app.callback(invoke_without_command=True)
def main():
    if len(sys.argv) == 1:
        print(ascii_art)
        print("[cyan]Welcome[/cyan] to fscan!")
        print(f"Version: {version}")
  
if __name__ == "__main__":
  app()