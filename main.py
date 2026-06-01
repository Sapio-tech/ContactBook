from manager import *

contacts = load_contacts()

while True:
print("\n=== Contact Book ===")
print("1. Add contact")
print("2. View all contacts")
print("3. Search contact")
print("4. Delete contact")
print("0. Exit")

choice = input("Choose:")

if choice == "1":
     add_contact(contacts)
elif choice == "2":
    view_contacts(contacts)
elif choice == "3":
    search_contact(contacts)
elif choice == "4":
    contacts = delete_contact(contacts)
elif choice == "0":
    print("Goodbye!")
    break
else:
    print("Invalid option!")
