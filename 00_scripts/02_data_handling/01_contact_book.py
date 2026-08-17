import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    with open(FILENAME, "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].strip().lower() == name.lower():
                print("Contact name already exists")
                return

    with open(FILENAME , "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added")

def view_contacts():
    with open(FILENAME, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 1:
            print("No contacts found")
            return

        print("\n Your contacts: \n")

        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()


def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True

    if not found:
        print("No matching contact found")

def update_contact():
    term = input("Enter contact name: ").lower()
    found = False
    updated_rows = []
    fieldnames = []

    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            if term in row["Name"].lower():
                field, updated_data = what_to_update()
                if field is None:
                    return
                
                row[field] = updated_data
                updated_rows.append(row)
                found = True
            else:
                updated_rows.append(row)

    if not found:
        print('Contact not found')
        return

    with open(FILENAME, 'w', newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)
        print("Contact updated...")

        
def what_to_update():
    print("\n What you want to update ?")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    print("4. Exit")

    while True:
        choice = input("Please enter your choice in between 1. to 4. : ").strip()
        match choice:
            case "1":
                new_name = input("Please Enter New Name: ")
                return ["Name", new_name]
            case "2":
                new_phone = input("Please Enter New Phone: ")
                return ["Phone", new_phone]
            case "3":
                new_email = input("Please Enter New Email: ")
                return ["Email", new_email]
            case "4":
                print("Update cancelled")
                return None
            case _ :
                print("Invalid choice")


def delete_contact():
    term = input("Enter Contact Name You Want to Delete: ").strip().lower()
    found = False
    updated_contacts = []
    fieldnames = []

    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            if term in row["Name"].lower():
                found = True
                continue
            else:
                updated_contacts.append(row)

    if not found:
        print("Contact Not Found!")
        return

    with open(FILENAME, 'w', newline="" ,encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_contacts)
        print("Contact Deleted")

        



def main():
    while True:
        print("\n Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thanks for using our software")
            break
        else:
            print("Invalid choice of number")


main()