import json
from contact import Contact

FILE = "contacts.json"

def load_contacts():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return [Contact(c["name"], c["phone"], c["email"]) for c in data]
      except:
          return []

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump([c.to_dict() for c in contacts], f)

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append(Contact(name, phone, email))
    save_contacts(contacts)
    print("Contact added!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
for c in contacts:
    print(c)

def search_contact(contacts):
    name = input("Search name: ")
    results = [c for c in contacts if name.lower() in c.name.lower()]
    if not results:
        print("Not found!")
for c in results:
    print(c)

def delete_contact(contacts):
    name = input("Delete name: ")
    new_list = [c for c in contacts if c.name.lower() != name.lower()]
    if len(new_list) == len(contacts):
        print("Not found!")
    else:
        save_contacts(new_list)
        print("Deleted!")
return new_list
