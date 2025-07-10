import re
import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_longest_words(text):
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return [], 0
    max_len = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_len]
    return longest, max_len

def main():
    while True:
        clear_screen()
        console.print(Panel("[bold cyan]🔍 LONGEST WORD FINDER[/bold cyan]", expand=False))

        text = Prompt.ask("📝 Enter a sentence or paragraph").strip()

        if not text:
            console.print("[bold yellow]\n⚠️  No input detected. Please enter some text.[/bold yellow]")
        else:
            longest_words, length = find_longest_words(text)
            if longest_words:
                console.print(f"\n📏 Longest word length: [bold green]{length}[/bold green] character(s)")
                console.print(f"💡 Longest word(s): [bold magenta]{', '.join(longest_words)}[/bold magenta]")
            else:
                console.print("\n❌ [bold red]No valid words found in the input.[/bold red]")

        again = Confirm.ask("\n🔁 Do you want to try again?")
        if not again:
            console.print("\n👋 Thank you for using Longest Word Finder. Goodbye!\n")
            break

if __name__ == "__main__":
    main()

