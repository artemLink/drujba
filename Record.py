from abc import ABC,abstractmethod
import json
import datetime
from Style import book_style,positive_action
from decorators import input_error
import re
class Field(ABC):
     @abstractmethod
     def __str__(self):
          pass


class ID(Field):
     def __init__(self,id) -> None:
          self._id = None
          self.set_id = id
     #GETTER   
     @property
     def get_id(self):
          return self._id
     #SETTER
     @get_id.setter
     def set_id(self,value):
          
         
          if type(value) is int:
               self._id = value
          else:
               print('Incrorrect ID')
               

     def __str__(self):
          return f'{self.get_id}'
 
class Name(Field):
     def __init__(self,name) -> None:
          self._name = None
          self.set_name = name.capitalize()
     
     @property
     def get_name(self):
          return self._name
     
     @get_name.setter
     def set_name(self,value: str):
          
          name = value.split()
          
          chars_count = 0
          for letter in name:
               if letter.isalpha():
                    chars_count += len(letter)
               else:
                    raise ValueError('ValueError: The name should consist only of letters and spaces. Minimum length is 3 characters, maximum is 20. Please try again.')
          chars_count += len(name)
          if chars_count >= 3 and chars_count <= 20:
               self._name = value
          else:
               raise ValueError('ValueError: The name should consist only of letters and spaces. Minimum length is 3 characters, maximum is 20. Please try again.')
          
     def __str__(self):
          return f'{self.get_name}'

class Phone(Field):
     def __init__(self,phone):
          self._phone = None
          self.set_phone = phone

     @property
     def get_phone(self):
          return self._phone
     
     @get_phone.setter
     def set_phone(self,phone : str):
          if phone.isdigit() and len(phone) == 10:
               self._phone = phone
#        elif phone == None:
#              self._phone = None
          else:
               raise ValueError('ValueError: Phone Number have 10 numbers ex: 0501952343')
     def __str__(self):
          return f'{self.get_phone}'
   
class Birthday(Field):
     def __init__(self,birthday) -> None:
          self._birthday = None
          self.set_birthday = birthday
     @property
     def get_birthday(self):
          return self._birthday
     
     @get_birthday.setter
     def set_birthday(self,birthday):
          

          if isinstance(birthday,str):
               #print(birthday)
               if self.validate_date_format(birthday):
                    birthday = datetime.datetime.strptime(birthday,"%Y-%m-%d").date()
                    self._birthday = birthday         
               else:
                    raise ValueError("Invalid birthday date. Please enter the date in 'dd mm yyyy' format, for example, '10 10 1994'.")
          elif isinstance(birthday, datetime.date):
               self._birthday = birthday
          elif birthday == None:
               self._birthday = None
          else:
               raise ValueError("Invalid birthday date. Please enter the date in 'dd mm yyyy' format, for example, '10 10 1994'.")
          
               
     def validate_date_format(self,date_string):
          regex_pattern = r'^\d{4}-\d{2}-\d{2}$'
          return re.match(regex_pattern, date_string) is not None
     def __str__(self):
          return f'{str(self._birthday)}'
     
class Email(Field):
     def __init__(self,email) -> None:
          self._email = None
          self.set_email = email
     @property
     def get_email(self):
          return self._email
     @get_email.setter
     def set_email(self,email):
          self._email = email
     def __str__(self):
          return f'{self.get_email}' 

class Record():
     def __init__(self,name, id, birthday=None,email = None):
          self.name = Name(name)
          self.id = ID(int(id))
          self.phones = []
          self.birthday = Birthday(birthday)
          self.email = Email(email)

     
     def __str__(self):
          return f'{positive_action("ID:")} {book_style(self.id.get_id)} {positive_action("Name:")} {book_style(self.name.get_name)} {positive_action("Phones: ")} {book_style(" ".join([str(item) for item in self.phones]))} {positive_action("Birthday: ")} {book_style(self.birthday.get_birthday)} {positive_action("Email:")} {book_style(self.email.get_email)} '


