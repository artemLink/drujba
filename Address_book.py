from Record import Record, Phone
from collections import UserList
from datetime import datetime, date
from Style import positive_action, command_message, book_style, error_message
from decorators import input_error
import json
import os


class AddressBook(UserList):
    def __init__(self):
        self.data = []
        self.exiting_data = []
        self.json_file_name = 'Contacts.json'
        self.load_contacts()

    def set_id(self):

        if len(self.exiting_data) == 0:
            id = 1
            return id
        else:
            id_values = []
            for item in self.exiting_data:
                id_values.append(item['ID'])
            max_id = max(id_values)

            for id in range(1, max_id):
                if id in id_values:
                    continue
                else:
                    return id
        return max_id + 1

    @input_error
    def add_full_record(self, name):
        record = Record(name, int(self.set_id()))
        record.phones.append(Phone(input(command_message('Enter Phone: '))))
        birthday = input(command_message('Enter Birthday: '))
        birthday = birthday.split()[::-1]
        record.birthday.set_birthday = input(command_message('Enter Birthday: '))
        record.email.set_email = input(command_message('Enter Email: '))
        record.comment.set_comment = input(command_message('Enter comment: '))  # Додав нове поле
        self.data.append(record)
        self.serialize_to_json(record)
        self.save_contacts()
        return (positive_action(f'{record.name.get_name} added'))

    @input_error
    def add_record(self, name):

        record = Record(name, int(self.set_id()))
        self.data.append(record)
        self.serialize_to_json(record)
        self.save_contacts()
        return (positive_action(f'{record.name.get_name} added'))

    @input_error
    def remove_record(self, name):
        record = self.find_record(name)
        ex_record = self.find_exiting_record(name)
        self.data.remove(record)
        self.exiting_data.remove(ex_record)
        self.save_contacts()
        return positive_action(f'{record.name.get_name} removed.')

    def serialize_to_json(self, record: Record):
        serialize_record = {'Name': record.name.get_name,
                            'ID': record.id.get_id,
                            'Phones': [item.get_phone for item in record.phones],
                            'Birthday': record.birthday.get_birthday.strftime('%Y-%m-%d') if isinstance(record.birthday.get_birthday, date) else None,
                            'Email': record.email.get_email,
                            'Comment': record.comment.get_comment}  # Додав нове поле
        self.exiting_data.append(serialize_record)

    @input_error
    def deserialize(self, dict) -> Record:
        record = Record(dict['Name'], dict['ID'])

        record.birthday.set_birthday = dict['Birthday']
        [record.phones.append(Phone(item)) for item in dict['Phones']]
        record.email.set_email = dict['Email']
        record.comment.set_comment = dict['Comment'] # Нове поле

        return record

    @input_error
    def add_comment(self, record: Record, serialize_record, comment):  # Додавання або зміна все існуючого коментаря
        record.comment.set_comment = comment
        serialize_record['Comment'] = comment
        self.save_contacts()
        return f'{positive_action("Comment")} {book_style(record.comment.get_comment)} {positive_action("added.")}'


    @input_error
    def remove_comment(self, record: Record, serialize_record):  # Видалення
        record.comment.set_comment = None
        serialize_record['Comment'] = None
        self.save_contacts()
        return f'{positive_action("Comment")} {book_style(record.email.get_comment)} {positive_action("removed.")}'



    @input_error
    def add_phone(self, record: Record, serialize_record, phone) -> Record:

        record.phones.append(Phone(phone))
        serialize_record['Phones'].append(phone)
        self.save_contacts()
        return f'{positive_action(f"Phone:")} {book_style(f"{phone}")} {positive_action("added.")}'

    def edit_phone(self, record: Record, serialize_record: {}, old_phone: str, new_phone: str) -> Record:

        for item in record.phones:
            if item.get_phone == old_phone:
                item.set_phone = new_phone
                break
        for index, item in enumerate(serialize_record['Phones']):
            if item == old_phone:
                serialize_record['Phones'][index] = new_phone
                break
        self.save_contacts()

    @input_error
    def remove_phone(self, record: Record, serialize_record, phone):
        for item in record.phones:
            if item.get_phone == phone:
                item.set_phone = None
            else:
                raise ValueError('ValueError: Phone number not found.')
        for item in serialize_record['Phones']:
            if item == phone:
                serialize_record['Phones'].remove(phone)
        self.save_contacts()

    @input_error
    def add_birthday(self, record: Record, serialize_record, birthday):
        print(birthday)
        record.birthday.set_birthday = birthday
        serialize_record['Birthday'] = str(record.birthday.get_birthday)
        self.save_contacts()
        return f'{positive_action("Birthday")} {book_style(record.birthday.get_birthday)} {positive_action("added.")}'

    @input_error
    def remove_birthday(self, record: Record, serialize_record):
        record.birthday.set_birthday = None
        serialize_record['Birthday'] = None
        self.save_contacts()
        return f'{positive_action("Birthday")} {book_style(record.birthday.get_birthday)} {positive_action("removed.")}'

    @input_error
    def add_email(self, record: Record, serialize_record, email):
        record.email.set_email = email
        serialize_record['Email'] = email
        self.save_contacts()
        return f'{positive_action("Email")} {book_style(record.email.get_email)} {positive_action("added.")}'

    @input_error
    def remove_email(self, record: Record, serialize_record):
        record.email.set_email = None
        serialize_record['Email'] = None
        self.save_contacts()
        return f'{positive_action("Email")} {book_style(record.email.get_email)} {positive_action("removed.")}'

    @input_error
    def rename(self, record: Record, serialize_record, name):
        old_name = str(record.name.get_name)
        record.name.set_name = name
        serialize_record['Name'] = name
        self.save_contacts()

        return f'{book_style(old_name)} {positive_action("changed")} {book_style(record.name.get_name)}.'

    def find_record(self, name) -> Record:
        records = []
        for item in self.data:
            if item.name.get_name == name:
                records.append(item)
        if len(records) > 1:
            self.show_records(records)
            return self.find_record_id(int(input(command_message('Enter Contact ID: '))))
        elif len(records) == 0:
            raise ValueError(f'{name} Not found!')
        else:
            return records[0]

    def find_record_id(self, id) -> Record:
        for item in self.data:
            if item.id.get_id == id:
                return item

    def find_exiting_record(self, name):
        for item in self.exiting_data:
            if item['Name'] == name:
                return item

    @input_error
    def show_records(self, name=None):
        page = 1
        if name == None:

            for item in self.iterator(50):
                print(positive_action(f'Page: {page} ------------------------------------------------'))
                print(item)
                page += 1

            # for item in self.data:
            #     print(item)
        elif isinstance(name, list):
            [print(item) for item in name]
        else:
            record = self.find_record(name)
            print(record)

    def load_contacts(self):
        if os.path.exists(self.json_file_name):

            with open(self.json_file_name, 'r') as fh:
                try:
                    self.exiting_data = json.load(fh)
                except json.JSONDecodeError:
                    print(json.JSONDecodeError)
                    return
                for item in self.exiting_data:
                    self.data.append(self.deserialize(item))
        else:
            print(f'{self.json_file_name} Not Found!')

    def save_contacts(self):
        with open(self.json_file_name, 'w') as fh:
            json.dump(self.exiting_data, fh, indent=1)

    def iterator(self, item_number):
        counter = 0
        result = ''
        for item in self.data:
            result += f'{item}\n'
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ''
        if result != '':
            yield result

    def find(self, search_string):
        find_contacts = []
        for item in self.data:
            name = item.name.get_name
            phone_numbers = [phone.get_phone for phone in item.phones]
            birthday = str(item.birthday.get_birthday)
            email = item.email.get_email

            if name != None and search_string.lower() in name.lower():
                find_contacts.append(item)
                continue
            if len(phone_numbers) > 0:
                for phone in phone_numbers:
                    if search_string in phone:
                        find_contacts.append(item)
                        continue
            if birthday != None and search_string in birthday:
                find_contacts.append(item)
                continue
            if email != None and search_string in email:
                find_contacts.append(item)
                continue

        return ''.join([str(item) + '\n' for item in find_contacts])
