from abc import ABC, abstractmethod
import json
import datetime
from Style import book_style, positive_action
from decorators import input_error
import re
import calendar


class Field(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Comment(Field):  # новий клас
    def __init__(self, comment: str):
        self._comment = None
        self.set_comment = comment

    @property
    def get_comment(self):
        return self._comment

    @get_comment.setter
    def set_comment(self, value: str):
        if value is None :
            self._comment = value
        elif value.strip():
            self._comment = value
        else:
            raise ValueError("Comment cannot be empty or consist only of spaces.")

    def __str__(self):
        return f"{self.get_comment}"


class ID(Field):
    def __init__(self, id) -> None:
        self._id = None
        self.set_id = id

    # GETTER
    @property
    def get_id(self):
        return self._id

    # SETTER
    @get_id.setter
    def set_id(self, value):

        if type(value) is int:
            self._id = value
        else:
            print('Incrorrect ID')

    def __str__(self):
        return f'{self.get_id}'


class Name(Field):
    def __init__(self, name) -> None:
        self._name = None
        self.set_name = name.capitalize()

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, value: str):

        name = value.split()

        chars_count = 0
        for letter in name:
            if letter.isalpha():
                chars_count += len(letter)
            else:
                raise ValueError(
                    'ValueError: The name should consist only of letters and spaces. Minimum length is 3 characters, '
                    'maximum is 20. Please try again.')
        chars_count += len(name)
        if chars_count >= 3 and chars_count <= 20:
            self._name = value
        else:
            raise ValueError(
                'ValueError: The name should consist only of letters and spaces. Minimum length is 3 characters, '
                'maximum is 20. Please try again.')

    def __str__(self):
        return f'{self.get_name}'


class Phone(Field):
    def __init__(self, phone):
        self._phone = None
        self.set_phone = phone

    @property
    def get_phone(self):
        return self._phone

    @get_phone.setter
    def set_phone(self, phone: str):
        if phone.isdigit() and len(phone) == 10:
            self._phone = phone
        #        elif phone == None:
        #              self._phone = None
        else:
            raise ValueError('ValueError: Phone Number have 10 numbers ex: 0501952343')

    def __str__(self):
        return f'{self.get_phone}'


class Birthday(Field):
    def __init__(self, birthday) -> None:
        self._birthday = None
        self.set_birthday = birthday

    @property
    def get_birthday(self):
        return self._birthday

    @get_birthday.setter
    def set_birthday(self, birthday):

        if isinstance(birthday, str):
            birthday_date = birthday.split('-')
            if len(birthday_date) != 3:
                raise ValueError("Invalid birthday date. Please enter the date in 'YYYY-MM-DD' format, for example, '2000-01-01'.")
            year = birthday_date[0]
            mounth = birthday_date[1]
            day = birthday_date[2]
            if not year.isdigit() or len(year) != 4:
                raise ValueError('Рік складається тільки з цифр і має 4 символи.')
            if not mounth.isdigit() or len(mounth) > 2:
                raise ValueError('Місяць складається тільки з цифр і містить 2 символи.')
            if int(mounth) > 12:
                raise ValueError('Місяць може мати значення від 1 до 12.')
            if not day.isdigit():
                raise ValueError('день складається тільки з цифр.')
            days_in_mounth = calendar.monthrange(int(year),int(mounth))[1]
            if int(day) > days_in_mounth:
                raise ValueError(f'Некоректно введений день, вказаний місяць має тільки {days_in_mounth} днів.')
            self._birthday = datetime.date(int(year),int(mounth),int(day))    

        elif birthday == None:
            self._birthday = None

                
            

    

    def __str__(self):
        return f'{str(self._birthday)}'


class Email(Field):
    def __init__(self, email) -> None:
        self._email = None
        self.set_email = email

    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def set_email(self, email):
        self._email = email

    def __str__(self):
        return f'{self.get_email}'


class Record:
    def __init__(self, name, id, birthday=None, email=None, comment=None):
        self.name = Name(name)
        self.id = ID(int(id))
        self.phones = []
        self.birthday = Birthday(birthday)
        self.email = Email(email)
        self.comment = Comment(comment)  # Додав новий класс як поле

    def __str__(self):
        return f'{positive_action("ID:")} {book_style(self.id.get_id)} {positive_action("Name:")} {book_style(self.name.get_name)} {positive_action("Phones: ")} {book_style(" ".join([str(item) for item in self.phones]))} {positive_action("Birthday: ")} {book_style(self.birthday.get_birthday)} {positive_action("Email:")} {book_style(self.email.get_email)}'
