import base64
import os

VAULT_FILE = "vault.txt"


def encode(text=''):
    return base64.b64encode(text.encode()).decode()

def decode(text=''):
    return base64.b64decode(text.encode()).decode()

def password_strength(password=''):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    # has_lower = any(c.islower() for c in password)
    has_special = any(c in '!@#$%^&*()<>.,' for c in password)

    score = sum([length >= 8, has_digit, has_special, has_upper])
    return ["Weak", "Medium", "Strong" , "Very Strong"][min(score, 3)]

def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = password_strength(password)

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding='utf-8') as f:
        f.write(encoded_line + "\n" )

    print("✅ Credential saved")

def old_update_password():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return

    website = input("Enter website: ")
    username = input("Enter your username: ")
    updated_lines = []

    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            decoded_row = decode(line)

            # print(f"{decoded_row.find(website)} {decoded_row.find(username)}")
            
            if website in decoded_row and username in decoded_row:
                website, username, password = decoded_row.split("||")

                new_password = input('\nPlease Enter Your New Password: ').strip()
                new_line = line.replace(password.strip(), new_password.strip())
                updated_lines.append(encode(new_line))
            else:
                updated_lines.append(line)

    print(updated_lines, "This is update lines")

    with open(VAULT_FILE, 'w', newline='', encoding='utf-8') as f:
        f.writelines(updated_lines)

def update_password():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return

    website = input("Enter website: ").strip()
    username = input("Enter your username: ").strip()
    updated_lines = []
    found = False

    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue

            # 1. Row ko Decode karo
            decoded_row = decode(clean_line)
            
            # 2. Match check karo using 'in'
            if website in decoded_row and username in decoded_row:
                parts = decoded_row.split("||")
                
                # Verify exact website and username match
                if len(parts) == 3 and parts[0] == website and parts[1] == username:
                    new_password = input('\nPlease Enter Your New Password: ').strip()
                    
                    # 3. Purane fields se NAYA decoded text banao
                    new_decoded_row = f"{website}||{username}||{new_password}"
                    
                    # 4. Sirf NAYE text ko Single-Encode karke add karo
                    updated_lines.append(encode(new_decoded_row) + "\n")
                    found = True
                else:
                    updated_lines.append(clean_line + "\n")
            else:
                # 5. Unchanged line ko BINA dubara encode kiye add karo
                updated_lines.append(clean_line + "\n")

    if found:
        with open(VAULT_FILE, 'w', encoding='utf-8') as f:
            f.writelines(updated_lines)
        print("✅ Password updated successfully!")
    else:
        print("❌ Matching website and username not found.")

def view_credentials():

    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return

    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")

            hidden_password = '*' * len(password)
            print(f"{website} | {username} | {password}")


def main():
    while True:
        print("\n Credential Manager")
        print("1. Add credential")
        print("2. View credential")
        print("3. Update credential")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1': add_credential()
            case '2': view_credentials()
            case '3': update_password()
            case '4': break
            case _ : print('Inalid choice')

if __name__ == "__main__":
    main()
