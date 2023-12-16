from abc import ABC,abstractmethod
from datetime import datetime,date
from decorators import input_error

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
     

class Title(Field):
    def __init__(self,title):
        self._title = None
        self.set_title = title
    @property
    def get_title(self):
        return self._title
    
    @get_title.setter
    def set_title(self,title: str):
        if title == None:
            raise ValueError('Класс title, Метод set_title, в якості аргумента None -> очікується string: НЕКОРЕКТНІ ДАННІ ') 
        if len(title) < 3 or len(title) > 10:
            raise ValueError('Класс Title, Метод set_title() значення менше 3 або більше 10: НЕКОРЕКТНІ ДАННІ')
        else:
            self._title = title    
    def __str__(self):
        return f'{self.get_title}'



class Note(Field):
    def __init__(self,note):
        self._note = None
        self.set_note = note
    @property
    def get_note(self):
        return self._note
    @get_note.setter
    def set_note(self,note):
        if note == None:
            raise ValueError('Класс Note, Метод set_note, в якості аргумента None: НЕКОРЕКТНІ ДАННІ')     
        elif len(note) < 3:
            raise ValueError('Класс Note, Метод set_note, Нотатка має менше 3 символів: НЕКОРЕКТНІ ДАННІ')
        else:
            self._note = note
    def __str__(self):
        return f'{self.get_note}'
    
class Tag(Field):
    def __init__(self,tag):
        self._tag = None
        self.set_tag = tag
    @property
    def get_tag(self):
        return self._tag
    @get_tag.setter
    def set_tag(self,tag: str):
        tag = tag.split()
        if len(tag) == 0 or len(tag) > 1:
            raise ValueError(f'Класс Tag, Метод set_tag, тег складається з {tag} cлів очікується 1 слово: НЕКОРЕКТНІ ДАННІ')
        elif len(tag[0]) < 3 or len(tag[0]) > 10:
            raise ValueError(f'Класс Tag, Метод set_tag, тег {tag[0]} має {len(tag[0])} букв очікується більше 3 і менше 10: НЕКОРЕКТНІ ДАННІ  ')
        else:
            self._tag = tag[0] 
    def __str__(self):
        return f'{self.get_tag}'

class AdditionDate(Field):
    def __init__(self,date):
        self._date = None
        if date != None:
            self._date = date
        
    @property
    def get_date(self):
        return str(self._date)
    
    @get_date.setter
    def set_date(self,date):
        self._date = date
    
    def __str__(self):
        return f'{str(self.get_date)}'


class NotesRecord():
    def __init__(self,id,title=None,note: Note =None,tag = None):
        self.id = ID(1)
        self.title = Title(title)
        self.note = Note(note)
        self.tag = []
        if tag != None:
            self.tag.append(Tag(tag))
        self.date_add = AdditionDate(datetime.now())

    def __str__(self):
        return f'ID: {str(self.id)}\nTitle: {self.title}\nNote: {self.note}\nTags: {" ".join([str(item) for item in self.tag])} \nDate addition: {str(self.date_add)} '    

x = NotesRecord(1, title='TEST TITLE',note='TEST NOTE',tag = 'TESTTAG')
print(x)




         


        
     
     
     
               
    

