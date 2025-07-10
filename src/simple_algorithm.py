import time
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        console.print(f"[bold cyan]Pass {i + 1}:[/bold cyan] {arr}")
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return comparisons, swaps

def main():
    while True:
        clear_screen()
        console.print(Panel("[bold blue]🔵 BUBBLE SORT ALGORITHM[/bold blue]", expand=False))

        user_input = Prompt.ask("📝 Enter numbers separated by spaces", default="")

        if not user_input.strip():
            console.print("[bold red]⚠️  No input detected. Please enter some numbers.[/bold red]")
            Prompt.ask("Press Enter to try again")
            continue

        try:
            nums = list(map(int, user_input.split()))
        except ValueError:
            console.print("[bold red]❌ Invalid input. Please enter integers only.[/bold red]")
            Prompt.ask("Press Enter to try again")
            continue

        console.print(f"\n[bold]Original array:[/bold] {nums}\n")

        start_time = time.time()
        comparisons, swaps = bubble_sort(nums.copy())
        end_time = time.time()
        bubble_sort_time = end_time - start_time

        # Performance Table
        table = Table(title="📊 Performance Analysis", show_header=True, header_style="bold magenta")
        table.add_column("Metric", style="dim")
        table.add_column("Value", justify="right")

        table.add_row("Array size", str(len(nums)))
        table.add_row("Total comparisons", str(comparisons))
        table.add_row("Total swaps", str(swaps))
        table.add_row("Time taken (seconds)", f"{bubble_sort_time:.5f}")

        console.print(table)

        start_builtin = time.time()
        sorted_builtin = sorted(nums)
        end_builtin = time.time()
        builtin_sort_time = end_builtin - start_builtin

        ratio = bubble_sort_time / builtin_sort_time if builtin_sort_time > 0 else float('inf')

        console.print(Panel(f"""⚡ [bold]Comparison with Python's built-in sort()[/bold]:
- Built-in sort time: {builtin_sort_time:.5f} seconds
- Bubble sort is approximately [bold yellow]{int(ratio)}x[/bold yellow] slower than built-in sort
""", title="Comparison", expand=False))

        again = Confirm.ask("🔁 Would you like to sort another list?")
        if not again:
            console.print("\n👋 Thank you for using the Bubble Sort program. Goodbye!")
            break

if __name__ == "__main__":
    main()
