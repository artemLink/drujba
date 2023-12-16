from collections import UserList
from decorators import input_error
from Notes import NotesRecord,Tag
import os
import json

class NotesBook(UserList):
    def __init__(self):
        self.data = []
        self.exiting_data = [] 
        self.json_file_name = 'Notes.json'
        

    
    def serialize_to_json(self,notes:NotesRecord):
        serialize_note_records = {
                            'ID':notes.note_id.get_id,
                            'Title':notes.title.get_title,
                            'Note':notes.note.get_note,
                            'Tags':[item.get_tag for item in notes.tag], 
                            'Addition Date':notes.addition_date.get_date,                   
        }
        self.exiting_data.append(serialize_note_records)

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

    def deserialize(self,dict) -> NotesRecord:
        Notes_record = NotesRecord(id = dict['ID'],title=dict['Title'],note=dict['Note'],)
        [Notes_record.tag.append(Tag(item)) for item in dict['Tags']]
        return Notes_record
    
    def save(self):
         with open(self.json_file_name,'w') as fh:
            json.dump(self.exiting_data,fh,indent=1)
    def load_notes(self):
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






         