from Address_book import AddressBook
from Style import command_message,error_message,help_message,positive_action,help1_message
class Bot():
    def __init__(self) -> None:
        self.book = AddressBook()


    
    def handle(self,action: str):
        action = action.split()
        
        if action[0] == 'find' and len(action) == 1:
            print(self.book.find(input(command_message('Enter search string:'))))
        if action[0] == 'find' and len(action) > 1:
            print(self.book.find(' '.join(action[1:])))
        if action[0] == 'help' and len(action) == 1:
            self.help()
        if action[0] == 'help' and len(action) > 1:
            self.help(action[1])
        if action[0] == 'hello' or action[0] == 'hi':
            print(command_message("Hello i'm Conatact Assistant"))
        if action[0] == 'add' and len(action) == 1:
            print(self.book.add_full_record(input(command_message('Enter Contact Name: '))))
        if action[0] == 'add' and len(action) > 1:
            name = ' '.join(action[1:])
            print(self.book.add_record(name))
        if action[0] == 'remove' and len(action) == 1:
            print(self.book.remove_record(input(command_message('Enter Contact Name: '))))
        if action[0] == 'remove' and len(action) > 1:
            name = ' '.join(action[1:]).capitalize()
            print(self.book.remove_record(name))
        if action[0] == 'show' and len(action) == 1:
            self.book.show_records()
        if action[0] == 'show' and len(action) > 1:
            name = ' '.join(action[1:]).capitalize()
            self.book.show_records(name)
        if action[0] == 'edit':
            if len(action) == 1:    
                name = input(command_message('Enter Contact Name: ')).capitalize()
            elif len(action) > 1:
                name = ' '.join(action[1:]).capitalize()
            try:
                record = self.book.find_record(name)
                
                exitinig_record = self.book.find_exiting_record(name)
            except ValueError as val_error_message:
                print(error_message(val_error_message))
            else:
                while True:
                    edit_command = input(command_message('edit command: ')).lower()
                    edit_command = edit_command.split()
                    if edit_command[0] == 'help' and len(edit_command) == 1:
                        self.help()
                        continue
                    if edit_command[0] == 'help' and len(edit_command) > 1:
                        self.help(edit_command[1])
                        continue
                    if len(edit_command) == 2 and edit_command[0] == 'add' and edit_command[1] == 'phone':
                       print(self.book.add_phone(record,exitinig_record,input(command_message('Enter Phone Number: '))))
                    elif len(edit_command) > 2 and edit_command[0] == 'add' and edit_command[1] == 'phone':
                       print(self.book.add_phone(record,exitinig_record,edit_command[2])) 
                    elif edit_command[0] == 'back':
                        return
                    elif len(edit_command) == 2 and edit_command[0] == 'edit' and edit_command[1] == 'phone':
                        print(self.book.edit_phone(record,exitinig_record,input(command_message('Enter Old Phone Number: ')),input(command_message('Enter New Phone Number'))))
                    elif len(edit_command) > 2 and edit_command[0] == 'edit' and edit_command[1] == 'phone':
                        print(self.book.edit_phone(record,exitinig_record,edit_command[2],edit_command[3]))
                    elif len(edit_command) == 2 and edit_command[0] == 'remove' and edit_command[1] == 'phone':
                        print(self.book.remove_phone(record,exitinig_record,input(command_message('Enter Phone Number: '))))
                    elif len(edit_command) > 2 and edit_command[0] == 'remove' and edit_command[1] == 'phone':
                        print(self.book.remove_phone(record,exitinig_record,edit_command[2]))
                    elif len(edit_command) == 2 and edit_command[0] == 'add' and edit_command[1] == 'birthday':    
                        
                        birthday = (input(command_message('Enter Birthday: ')))
                        
                        print(self.book.add_birthday(record,exitinig_record,birthday))
                    elif len(edit_command) > 2 and edit_command[0] == 'add' and edit_command[1] == 'birthday':
                         birthday = edit_command[2]
                         print(self.book.add_birthday(record,exitinig_record,birthday))
                    elif len(edit_command) == 2 and edit_command[0] == 'remove' and edit_command[1] == 'birthday':
                        print(self.book.remove_birthday(record,exitinig_record))
                    elif len(edit_command) == 2 and edit_command[0] == 'add' and edit_command[1] == 'email':
                        print(self.book.add_email(record,exitinig_record,input(command_message('Enter email: '))))
                    elif len(edit_command) > 2 and edit_command[0] == 'add' and edit_command[1] == 'email':
                        print(self.book.add_email(record,exitinig_record,edit_command[2]))
                    elif len(edit_command) == 2 and edit_command[0] == 'remove' and edit_command[1] == 'email':
                        print(self.book.remove_email(record,exitinig_record))
                    elif edit_command[0] == 'rename' and len(edit_command) == 1:
                        print(self.book.rename(record,exitinig_record,input(command_message('Enter new name: ').capitalize())))
                    elif edit_command[0] == 'rename' and len(edit_command) > 1:
                        print(self.book.rename(record,exitinig_record,' '.join(edit_command[1:]).capitalize()))
                    else:
                        print(error_message('Non-Command.'))
            
                    

    def help(self, command = None):
        exit = [(help_message("- 'exit' - exit the program"))]
        
        
        find = [(help_message("The 'find' command is designed to find contacts in the phone book based on a specific phrase entered by the user.")),
                (help_message("         Usage:")),
                (help_message("             'find' - prompts the user to enter a phrase for searching contacts")),
                (help_message("             'find [phrase]' - finds contacts that match the entered phrase and displays the result"))]
        
        add = [(help_message("- 'add' - add a new entry to the address book")),
               (help_message("         Usage:")),
               (help_message("             'add' - prompts to enter name, phone number, birth year, and email")),
               (help_message("             'add [name]' - adds a new entry with only the specified name"))]
        
        remove = [(help_message("- 'remove' - remove an item from the list")),
            (help_message("         Usage:")),
            (help_message("             'remove' - prompts to enter the name to remove")),
            (help_message("             'remove [name]' - removes an entry with the specified name"))]
        
        show = [(help_message("- 'show' - display entries from the address book")),
            (help_message("         Usage:")),
            (help_message("             'show' - shows all entries")),
            (help_message("             'show [name]' - shows entries with the specified name"))]
        
        edit = [(help_message("- 'edit' - edit a user's details")),
               (help_message("         Usage:")),
               (help_message("             'edit' - prompts to enter the user's name to edit details")),
               (help_message("             'edit [name]' - opens commands to edit specific user's details")),
               (help_message("                 Usage after 'edit [name]':")),
               (help1_message("   edit command: 'rename' or 'rename [name]' - allows renaming the user")),
               (help1_message("   edit command: 'add phone' or 'add phone [phone]' - allows adding a phone number for the user")),
               (help1_message("   edit command: 'edit phone' or 'edit phone [old] [new phone]' - allows editing the user's phone number")),
               (help1_message("   edit command: 'remove phone' or 'remove phone [phone]' - allows removing the user's phone number")),
               (help1_message("   edit command: 'add birthday' or 'add birthday dd mm YYYY' - allows adding a birthday for the user")),
               (help1_message("   edit command: 'remove birthday' - allows removing the user's birthday")),
               (help1_message("   edit command: 'add email' or 'add email [email]' - allows adding an email for the user")),
               (help1_message("   edit command: 'remove email' - allows removing the user's email")),
               (help1_message("   edit command: 'back' - returns to the main command menu"))]
        commands = [exit, find, add, remove, show, edit, ] # Додаю нові команди
        if command == None:
            
            for item_1 in commands:
                print(positive_action('=' * 100))
                for item_2 in item_1 :
                   print(item_2)
        if command == 'exit':
            print(positive_action('=' * 100))
            for item in exit:   
                print(item)
        if command == 'find':
            print(positive_action('=' * 100))
            for item in find:
                print(item)
        if command == 'add':
            print(positive_action('=' * 100))
            for item in add:
                print(item)
        if command == 'remove':
            print(positive_action('=' * 100))
            for item in remove:
                print(item)
        if command == 'show':
            print(positive_action('=' * 100))
            for item in show:
                print(item)
        if command == 'edit':
            print(positive_action('=' * 100))
            for item in edit:
                print(item)
        print(positive_action('=' * 100))
        
            
            
