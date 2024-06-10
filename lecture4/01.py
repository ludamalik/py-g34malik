contacts = [
    {
        'last_name': "Литвин",
        'first_name': "Володимир",
        "INN": "3492413574",
        "phone_number": "0960733150",
        "Account": "2620511812387",
    },
    {
        "last_name": "Волинець",
        "first_name": "Галина",
        "INN": "2070404787",
        "phone_number": "0970295266",
        "Account": "2620611196886"
    },
    {
        "last_name": "Матвіїв",
        "first_name": "Григорій",
        "INN": "2026502810",
        "phone_number": "0673076032",
        "Account": "2620311246094"
    },
    {
        "last_name": "Константинов",
        "first_name": "Артем",
        "INN": "3769905472",
        "phone_number": "0632404119",
        "Account": "262088716966"
    },
    {
        "last_name": "Косик",
        "first_name": "Степан",
        "INN": "2096811436",
        "phone_number": "0673941442",
        "Account": "2620211404141"
    }
]

TITLE = "Your phone book"

def hello():
    print(f"Hi! It's me, {TITLE.upper()}")

def bye():
    print(f"Thanks for using {TITLE}")

def make_your_choice():
    return (
        input(f"\nPlease make your choice (l, a, u, r, h, or q) here>>> ")
        .strip()
        .lower()
    )

def help_me():
    print(
        """
    All that you can do:
        l : List existing contacts
        a : Add new contact
        u : Update existing contact
        r : Remove existing contact
        h : Print this help
        q : Exit
    """
    )

def contact_list():
    if len(contacts) > 0:
        for contact in contacts:
            for key, value in contact.items():
                print(key, '=>', value)
    else:
        print("Your contact list is empty. Go back to menu to add a new contact.")

def is_unique(field, value, exclude_contact=None):
    for contact in contacts:
        if contact == exclude_contact:
            continue
        if contact[field] == value:
            return False
    return True

def validate_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

def validate_INN(INN):
    return len(INN) == 10 and INN.isdigit()

def validate_account(Account):
    return len(Account) == 12 and Account.startswith("2620") and Account.isdigit()

def input_with_validation(prompt, validate_fn, error_message):
    while True:
        value = input(prompt).strip()
        if validate_fn(value):
            return value
        else:
            print(error_message)

def add_contact():
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    phone_number = input_with_validation(
        "Enter phone number: ",
        validate_phone_number,
        "Sorry, phone number isn't right. Consider rewriting it."
    )
    INN = input_with_validation(
        "Enter INN: ",
        validate_INN,
        "Sorry, INN isn't right. Consider rewriting it."
    )
    Account = input_with_validation(
        "Enter Account: ",
        validate_account,
        "Sorry, Account isn't right. Consider rewriting it."
    )

    if not is_unique("phone_number", phone_number):
        print("Phone number already exists.")
        return None
    if not is_unique("INN", INN):
        print("INN already exists.")
        return None
    if not is_unique("Account", Account):
        print("Account already exists.")
        return None

    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "INN": INN,
        "Account": Account
    }
    return contact

def update_contact(contact):
    old_phone_number = contact["phone_number"]
    old_first_name = contact["first_name"]
    old_last_name = contact["last_name"]
    old_INN = contact["INN"]
    old_Account = contact["Account"]

    phone_number = (
        input(f"Edit phone number: ({old_phone_number}) => ").strip()
        or old_phone_number
    )
    if phone_number != old_phone_number:
        phone_number = input_with_validation(
            f"Edit phone number: ({old_phone_number}) => ",
            validate_phone_number,
            "Sorry, phone number isn't right. Consider rewriting it."
        )
        if not is_unique("phone_number", phone_number, contact):
            print("Phone number already exists.")
            return contact

    first_name = (
        input(f"Edit first name: ({old_first_name}) => ").strip() or old_first_name
    )
    last_name = input(f"Edit last name: ({old_last_name}) => ").strip() or old_last_name

    INN = input(f"Edit INN: ({old_INN}) => ").strip() or old_INN
    if INN != old_INN:
        INN = input_with_validation(
            f"Edit INN: ({old_INN}) => ",
            validate_INN,
            "Sorry, INN isn't right. Consider rewriting it."
        )
        if not is_unique("INN", INN, contact):
            print("INN already exists.")
            return contact

    Account = input(f"Edit Account: ({old_Account}) => ").strip() or old_Account
    if Account != old_Account:
        Account = input_with_validation(
            f"Edit Account: ({old_Account}) => ",
            validate_account,
            "Sorry, Account isn't right. Consider rewriting it."
        )
        if not is_unique("Account", Account, contact):
            print("Account already exists.")
            return contact

    return {
        "first_name": first_name.lower(),
        "last_name": last_name.lower(),
        "phone_number": phone_number,
        "INN": INN,
        "Account": Account
    }

def remove_contact(contact):
    index = contacts.index(contact)
    confirm = (
        input("Are you sure you want to delete this contact? (y/n): ").strip().lower()
    )
    if confirm in ("yes", "y"):
        contacts.pop(index)
        print("Contact removed successfully.")

def lookup_contact(name):
    words = name.split()
    if len(words) == 2:
        first_name, last_name = words
    elif len(words) == 1:
        first_name = words[0]
        last_name = ""
    else:
        return None

    for d in contacts:
        if (
            d["first_name"] == first_name.lower()
            and d["last_name"] == last_name.lower()
        ):
            return d
        elif d["first_name"] == first_name.lower() and not last_name:
            return d
    return None

def main():
    hello()
    help_me()

    while True:
        choice = make_your_choice()
        if choice == "a":
            new_contact = add_contact()
            if new_contact:
                contacts.append(new_contact)
                print("Contact added successfully.")
        elif choice == "l":
            contact_list()
        elif choice == "u":
            name = input("What name are you looking for: ").strip().lower()
            contact = lookup_contact(name)
            if contact:
                updated_contact = update_contact(contact)
                contact.update(updated_contact)
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
        elif choice == "r":
            name = input("What name are you looking for: ").strip().lower()
            contact = lookup_contact(name)
            if contact:
                remove_contact(contact)
            else:
                print("Contact not found.")
        elif choice == "q":
            bye()
            break
        else:
            help_me()

main()
