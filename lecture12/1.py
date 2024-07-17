import json

class Contact:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def to_json(self):
        '''Serialize the object custom object'''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# ��������� ���������� ����� Contact
c1 = Contact("Lucy Smile", '7777', '1, Smile st.')
c2 = Contact("Thomas Cook", '1123', '2, Cook avn.')

# ��������� ������ ��������
contacts = [c1, c2]

# ���������� ������ ��������
serialized_contacts = [contact.to_json() for contact in contacts]

# ����� ������������ ����� � ����
filename = "contact.json"
with open(filename, 'w') as f:
    json.dump(serialized_contacts, f)

# ������������ � �����
with open(filename, 'r') as f:
    loaded_contacts = json.load(f)

# ������������ ������� �������� � ������
result = [json.loads(contact) for contact in loaded_contacts]

print(result)

