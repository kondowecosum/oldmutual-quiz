import os
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
    console.print(Panel("👤 [bold green]ADD CLIENT[/bold green]", expand=False))
    client_id = Prompt.ask("Enter client ID")
    name = Prompt.ask("Enter client name")
    fund = Prompt.ask("Enter Fund")
    clients.append({"id": client_id, "name": name, "fund": fund})
    console.print("\n✅ Client added successfully!\n")
    Prompt.ask("Press Enter to return to the menu")

def view_clients():
    clear_screen()
    console.print(Panel("👥 [bold blue]CLIENT LIST[/bold blue]", expand=False))
    if not clients:
        console.print("[bold yellow]⚠️ No clients found.[/bold yellow]\n")
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
    console.print(Panel("🔍 [bold cyan]SEARCH CLIENT[/bold cyan]", expand=False))
    term = Prompt.ask("Enter search term").lower()
    found = [c for c in clients if term in c["name"].lower()]
    console.print(f"\n🔎 Found {len(found)} client(s):\n")

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
    console.print(Panel("✏️  [bold yellow]EDIT CLIENT[/bold yellow]", expand=False))
    client_id = Prompt.ask("Enter client ID to edit")
    for client in clients:
        if client["id"] == client_id:
            console.print(f"\nCurrent details:\nID: {client['id']} | Name: {client['name']} | Fund: {client['fund']}")
            new_name = Prompt.ask("Enter new name (press Enter to keep current)", default=client["name"])
            new_fund = Prompt.ask("Enter new Fund (press Enter to keep current)", default=client["fund"])
            client["name"] = new_name if new_name else client["name"]
            client["fund"] = new_fund if new_fund else client["fund"]
            console.print("\n✅ Client updated successfully!\n")
            Prompt.ask("Press Enter to return to the menu")
            return
    console.print("\n❌ Client not found.\n")
    Prompt.ask("Press Enter to return to the menu")

def delete_client():
    clear_screen()
    console.print(Panel("🗑️  [bold red]DELETE CLIENT[/bold red]", expand=False))
    client_id = Prompt.ask("Enter client ID to delete")
    for client in clients:
        if client["id"] == client_id:
            confirm = Confirm.ask(f"Are you sure you want to delete {client['name']}?")
            if confirm:
                clients.remove(client)
                console.print("\n🗑️  Client deleted successfully!\n")
            else:
                console.print("\n❌ Deletion cancelled.\n")
            Prompt.ask("Press Enter to return to the menu")
            return
    console.print("\n❌ Client not found.\n")
    Prompt.ask("Press Enter to return to the menu")

def menu():
    while True:
        clear_screen()
        console.print(Panel("[bold magenta]🧑‍💼 CLIENT MANAGEMENT SYSTEM[/bold magenta]", expand=False))
        console.print(
            "\n1. 👤 Add Client\n"
            "2. 👥 View All Clients\n"
            "3. 🔍 Search Client\n"
            "4. ✏️  Edit Client\n"
            "5. 🗑️  Delete Client\n"
            "6. 🚪 Exit\n"
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
            console.print("\n👋 Exiting program. Goodbye!\n")
            break
        else:
            console.print("[bold red]\n❌ Invalid choice. Try again.[/bold red]")
            Prompt.ask("Press Enter to continue...")

if __name__ == "__main__":
    menu()
