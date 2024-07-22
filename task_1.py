from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be 10 digits long")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError("Old phone number not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str if phones_str else 'No phone numbers'}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

 

book = AddressBook()


john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print("Address Book:")
print(book)

john = book.find("John")
if john:
    john.edit_phone("1234567890", "1112223333")

print("\nUpdated John record:")
print(john)  


found_phone = john.find_phone("5555555555")
print(f"\nPhone found in John's record: {found_phone}")  
book.delete("Jane")

print("\nAddress Book after deleting Jane:")
print(book)
