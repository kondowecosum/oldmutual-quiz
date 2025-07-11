
import os
import re
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm

console = Console()
clients = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_client():
    clear_screen()
    console.print(Panel("[bold green]ADD CLIENT[/bold green]", expand=False))

    if len(clients) >= 999:
        console.print("[bold red]Client limit reached (C999). Cannot add more clients.[/bold red]")
        Prompt.ask("Press Enter to return to the menu")
        return

    # Input and validate client ID
    while True:
        client_id = Prompt.ask("Enter client ID (format C001 to C999)").upper()
        if not re.match(r"^C\d{3}$", client_id):
            console.print("[bold red]Invalid format. Use 'C' followed by 3 digits (e.g., C001).[/bold red]")
            continue

        num = int(client_id[1:])
        if num < 1 or num > 999:
            console.print("[bold red]Number must be between 001 and 999.[/bold red]")
            continue

        if any(c["id"] == client_id for c in clients):
            console.print(f"[bold red]Client ID '{client_id}' already exists.[/bold red]")
            continue
        break

    # Input and validate name (letters and spaces only)
    while True:
        name = Prompt.ask("Enter client name (letters and spaces only)")
        if not re.match(r"^[A-Za-z ]+$", name):
            console.print("[bold red]Invalid name. Use letters and spaces only.[/bold red]")
            continue
        name = name.strip()
        if not name:
            console.print("[bold red]Name cannot be empty.[/bold red]")
            continue
        break

    fund = Prompt.ask("Enter Fund")
    clients.append({"id": client_id, "name": name, "fund": fund})
    console.print("\n[bold green]Client added successfully![/bold green]\n")
    Prompt.ask("Press Enter to return to the menu")

def view_clients():
    clear_screen()
    console.print(Panel("[bold blue]CLIENT LIST[/bold blue]", expand=False))
    if not clients:
        console.print("[bold yellow]No clients found.[/bold yellow]\n")
    else:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=10)
        table.add_column("Name", min_width=20)
        table.add_column("Fund", min_width=15)

        for client in clients:
            table.add_row(client["id"], client["name"], client["fund"])
        console.print(table)
        console.print(f"\nTotal clients: {len(clients)}\n")

    Prompt.ask("Press Enter to return to the menu")

def search_client():
    clear_screen()
    console.print(Panel("[bold cyan]SEARCH CLIENT[/bold cyan]", expand=False))
    term = Prompt.ask("Enter search term (ID, Name or Fund)").lower()

    found = [c for c in clients if
             term in c["id"].lower() or
             term in c["name"].lower() or
             term in c["fund"].lower()]

    console.print(f"\nFound {len(found)} client(s):\n")

    if found:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=10)
        table.add_column("Name", min_width=20)
        table.add_column("Fund", min_width=15)

        for client in found:
            table.add_row(client["id"], client["name"], client["fund"])
        console.print(table)
    else:
        console.print("[bold yellow]No matching clients found.[/bold yellow]")

    Prompt.ask("\nPress Enter to return to the menu")

def edit_client():
    clear_screen()
    console.print(Panel("[bold yellow]EDIT CLIENT[/bold yellow]", expand=False))
    client_id = Prompt.ask("Enter client ID to edit").upper()
    for client in clients:
        if client["id"] == client_id:
            console.print(f"\nCurrent details:\nID: {client['id']} | Name: {client['name']} | Fund: {client['fund']}")
            new_name = Prompt.ask("Enter new name (letters and spaces only, press Enter to keep current)", default=client["name"])

            if new_name != client["name"]:
                if not re.match(r"^[A-Za-z ]+$", new_name):
                    console.print("[bold red]Invalid name. Keeping current name.[/bold red]")
                    new_name = client["name"]
                else:
                    new_name = new_name.strip() or client["name"]

            new_fund = Prompt.ask("Enter new Fund (press Enter to keep current)", default=client["fund"])
            client["name"] = new_name
            client["fund"] = new_fund if new_fund else client["fund"]
            console.print("\n[bold green]Client updated successfully![/bold green]\n")
            Prompt.ask("Press Enter to return to the menu")
            return
    console.print("\n[bold red]Client not found.[/bold red]\n")
    Prompt.ask("Press Enter to return to the menu")

def delete_client():
    clear_screen()
    console.print(Panel("[bold red]DELETE CLIENT[/bold red]", expand=False))
    client_id = Prompt.ask("Enter client ID to delete").upper()
    for client in clients:
        if client["id"] == client_id:
            confirm = Confirm.ask(f"Are you sure you want to delete {client['name']}?")
            if confirm:
                clients.remove(client)
                console.print("\n[bold green]Client deleted successfully![/bold green]\n")
            else:
                console.print("\n[bold yellow]Deletion cancelled.[/bold yellow]\n")
            Prompt.ask("Press Enter to return to the menu")
            return
    console.print("\n[bold red]Client not found.[/bold red]\n")
    Prompt.ask("Press Enter to return to the menu")

def menu():
    while True:
        clear_screen()
        console.print(Panel("[bold magenta]CLIENT MANAGEMENT SYSTEM[/bold magenta]", expand=False))
        console.print(
            "\n1. Add Client\n"
            "2. View All Clients\n"
            "3. Search Client\n"
            "4. Edit Client\n"
            "5. Delete Client\n"
            "6. Exit\n"
        )
        choice = Prompt.ask("Enter choice (1-6)")
        

        if choice == "1":
            add_client()
        elif choice == "2":
            view_clients()
        elif choice == "3":
            search_client()
        elif choice == "4":
            edit_client()
        elif choice == "5":
            delete_client()
        elif choice == "6":
            console.print("\n[bold cyan]Exiting program. Goodbye![/bold cyan]\n")
            break
        else:
            console.print("[bold red]Invalid choice. Try again.[/bold red]")
            Prompt.ask("Press Enter to continue...")

if __name__ == "__main__":
    menu()

