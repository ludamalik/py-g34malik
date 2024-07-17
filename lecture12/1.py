import json

class Contact:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def to_json(self):
        '''Serialize the object custom object'''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# Створення екземплярів класу Contact
c1 = Contact("Lucy Smile", '7777', '1, Smile st.')
c2 = Contact("Thomas Cook", '1123', '2, Cook avn.')

# Створення списку контактів
contacts = [c1, c2]

# Серіалізація списку контактів
serialized_contacts = [contact.to_json() for contact in contacts]

# Запис серіалізованих даних у файл
filename = "contact.json"
with open(filename, 'w') as f:
    json.dump(serialized_contacts, f)

# Десеріалізація з файлу
with open(filename, 'r') as f:
    loaded_contacts = json.load(f)

# Десеріалізація кожного контакту зі списку
result = [json.loads(contact) for contact in loaded_contacts]

print(result)

