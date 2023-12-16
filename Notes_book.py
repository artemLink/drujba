from collections import UserList
from decorators import input_error
from Notes import NotesRecord,Tag

import json

class NotesBook(UserList):
    def __init__(self):
        self.data = []
        self.exiting_data = [] 
        self.json_file_name = 'Notes.json'
        

    
    def serialize_to_json(self,notes:NotesRecord):
        serialize_note_records = {
                            'ID':notes.id.get_id,
                            'Title':notes.title.get_title,
                            'Note':notes.note.get_note,
                            'Tags':[item.get_tag for item in notes.tag], 
                            'Addition Date':notes.date_add.get_date,                   
        }

        self.exiting_data.append(serialize_note_records)

    def deserialize(self,dict) -> NotesRecord:
        Notes_record = NotesRecord(id = dict['ID'],title=dict['Title'],note=dict['Note'],)
        [Notes_record.tag.append(Tag(item)) for item in dict['Tags']]
        return Notes_record
    
    def save(self):
         with open(self.json_file_name,'w') as fh:
            json.dump(self.exiting_data,fh,indent=1)


Test1  = NotesRecord(1,'Title1','Note111111111111111111','Tag1')
Test2  = NotesRecord(2,'Title2','Note222222222222222222','Tag2')
Test3  = NotesRecord(1,'Title3','Note333333333333333333','Tag3')
Test4  = NotesRecord(1,'Title4','Note444444444444444444','Tag4')
Test5  = NotesRecord(1,'Title5','Note555555555555555555','Tag5')

NoteBook = NotesBook()
NoteBook.append(Test1)
NoteBook.append(Test2)
NoteBook.append(Test3)
NoteBook.append(Test4)
NoteBook.append(Test5)

for item in NoteBook.data:
    NoteBook.serialize_to_json(item)

NoteBook.save()






         