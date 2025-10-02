import csv
from pathlib import Path

FILE = Path("contacts.csv")

def add_contact(name, phone):
    exists = FILE.exists()
    with FILE.open("a", newline="") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["name", "phone"])
        writer.writerow([name, phone])
    print("Saved.")

def list_contacts():
    if not FILE.exists():
        print("No contacts.")
        return
    with FILE.open() as f:
        reader = csv.DictReader(f)
        for r in reader:
            print(f"{r['name']} - {r['phone']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python contacts.py add|list <args>")
    elif sys.argv[1] == "add":
        add_contact(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "list":
        list_contacts()
