from Address_book import AddressBook
from Style import command_message, error_message, positive_action
from Notes_book import NotesBook
from sort_files import sort_by_type
import cmd
from rich.console import Console
from rich.table import Table
from art import *
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter



class MyCmd(cmd.Cmd):
    book = AddressBook('Contacts.json')
    notes_book = NotesBook('Notes.json')
    console = Console()
    # випадаючі команди
    word_completer = WordCompleter(
        ['help',
         "exit",
         'make_note',
         'make_tag',
         'find_note',
         'find_tag',
         'edit_note',
         'edit_title',
         "del_note",
         "show_notes",
         "sort_by_type",
         "show_rec",
         "make_rec",
         "find_rec",
         "del_rec",
         #  "del_comp_rec",
         "edit_ph_rec",
         "edit_tag_rec",
         "cong_rec",
         # "exp_tag",
         # "add_comp_rec",
         ])
    intro = tprint("designed  by  DRUJBA  team")

    def cmdloop(self, intro=None):
        self.preloop()
        if self.intro:
            self.console.print(self.intro)
            self.do_help()
        stop = None
        while not stop:
            try:
                session = PromptSession()
                user_input = session.prompt(
                    "Enter command>>> ", completer=self.word_completer)
                stop = self.onecmd(user_input)
            except KeyboardInterrupt:
                print("^C")
        self.postloop()

    def do_hello(self, *args):
        "Say hello"
        print(command_message("How can I help you?"))

    def do_exit(self, *args):
        "Exit from bot"
        print(positive_action("Good bye!"))
        return True

    # таблиця help
    def do_help(self, *args):
        table = Table()
        table.add_column("COMMAND", style="bright_magenta")
        table.add_column("DESCRIPTION", style="bright_blue", no_wrap=True)
        table.add_row("help",
                      "Shows a description of the commands")
        table.add_row("exit",
                      "To exit the session")
        table.add_row("----",
                      "-----------------------------------")
        table.add_row("make_note",
                      "Make a note")
        table.add_row("make_tag",
                      "Make a tag")
        table.add_row("find_note",
                      "Search by title and notes")
        table.add_row("find_tag",
                      "Search by tags")
        table.add_row("edit_note",
                      "Edits notes by ID (use search before use)")
        table.add_row("edit_title",
                      "Edits titles to note by ID (use search before use)")
        table.add_row("del_note",
                      "Deletes note by ID (use search before use)")
        table.add_row("show_notes",
                      "Shows all notes")
        table.add_row("----",
                      "-----------------------------------")
        table.add_row("show_rec",
                      "Shows all book records")
        table.add_row("make_rec",
                      "Make a record to addressbook")
        table.add_row("find_rec",
                      "Search in addressbook")
        table.add_row("del_rec",
                      "Deletes record in addressbook by name (use search before use)")
        table.add_row("edit_ph_rec",
                      "Edites phone to record in addressbook by name (use search before use)")
        table.add_row("edit_tag_rec",
                      "Edites tag to record in addressbook by name (use search before use)")
        table.add_row("cong_rec",
                      "Search contacts by birthday")
        # table.add_row("exp_tag",
        #               "Exports contacts by tag to a JSON file (use search before use)")
        # table.add_row("add_comp_rec",
        #               "Adds a company to a record in the address book by name (use search before use)")
        # table.add_row("del_comp_rec",
        #               "Deletes company in addressbook by name (use search before use)")
        table.add_row("----",
                      "-----------------------------------")
        table.add_row("sort_by_type",
                      "Sorts files by type (images, videos, documents, music, archives)")

        self.console.print(table)

    ### ------------ NotesBook part-------------###

    def do_make_note(self, *args):
        "Make a note"
        title = input(command_message("Enter title>>> "))
        note = input(command_message("Enter note>>> "))
        self.notes_book.add_note(title, note)
        question = input(command_message("Do you want to enter a tag?>> "))
        if question.lower() == 'yes':
            tag = input(command_message("Enter tag>>> "))
            self.notes_book.add_tag(tag)
        self.notes_book.save_note()
        print(positive_action("Note added"))

    def do_make_tag(self, *args):
        "Make a tag"
        inp_id = input(command_message(
            "Enter ID of the record that changes>>> "))
        tag = input(command_message("Enter tag>>> "))
        self.notes_book.add_tag(tag, inp_id)
        self.notes_book.save_note()
        print(positive_action("Tag added"))

    def do_find_note(self, *args):
        "Search by title and notes"
        question = input(command_message("Enter your request>>> "))
        table = Table()
        table.add_column("ID", style="bright_magenta")
        table.add_column("Date", style="magenta")
        table.add_column("Tag", style="cyan")
        table.add_column("Title", style="bright_cyan")
        table.add_column("Note", style="blue")
        if len(self.notes_book.find_note(question)) > 0:
            for sh in self.notes_book.find_note(question):
                if isinstance(sh.tag, list):
                    table.add_row(
                        f"{sh.note_id.get_id}", f"{sh.addition_date.get_date}",
                        f"{' '.join([str(item) for item in sh.tag])}", f"{sh.title.get_title}", f"{sh.note.get_note}")
            self.console.print(table)
        else:
            print(error_message("No notes found."))

    def do_find_tag(self, *args):
        "Search by tags"
        question = input(command_message("Enter your request>>> "))
        table = Table()
        table.add_column("ID", style="bright_magenta", no_wrap=True)
        table.add_column("Date", style="magenta")
        table.add_column("Tag", style="cyan")
        table.add_column("Title", style="bright_cyan")
        table.add_column("Note", style="blue")
        if len(self.notes_book.find_tag(question)) > 0:
            for sh in self.notes_book.find_tag(question):
                if isinstance(sh.tag, list):
                    table.add_row(
                        f"{sh.note_id.get_id}", f"{sh.addition_date.get_date}",
                        f"{' '.join([str(item) for item in sh.tag])}", f"{sh.title.get_title}", f"{sh.note.get_note}")

            self.console.print(table)
        else:
            print(error_message("No notes found."))

    def do_edit_note(self, *args):
        "Edits notes"
        inp_id = input(command_message(
            "Enter ID of the record that changes>>> "))
        note = input(command_message("Enter new note>>> "))
        self.notes_book.edit_note(inp_id, note)
        self.notes_book.save_note()
        print(positive_action("Note has been edited"))

    def do_edit_title(self, *args):
        "Edits titles"
        inp_id = input(command_message(
            "Enter ID of the record that changes>>> "))
        title = input(command_message("Enter new title>>> "))
        self.notes_book.edit_title(inp_id, title)
        self.notes_book.save_note()
        print(positive_action("Title has been edited"))

    def do_del_note(self, *args):
        "Deletes note"
        inp_id = input(command_message(
            "Enter ID of the record that delete>>> "))
        self.notes_book.delete_note(inp_id)
        self.notes_book.save_note()
        print(positive_action("Record deleted successfully"))

    def do_show_notes(self, *args):
        "Shows all notes records"
        table = Table()
        table.add_column("ID", style="bright_magenta")
        table.add_column("Date", style="magenta")
        table.add_column("Tag", style="cyan")
        table.add_column("Title", style="bright_cyan")
        table.add_column("Note", style="blue")
        for sh in self.notes_book:
            if isinstance(sh.tag, list):
                table.add_row(f"{sh.note_id.get_id}", f"{sh.addition_date.get_date}",
                              f"{' '.join([str(item) for item in sh.tag])}", f"{sh.title.get_title}",
                              f"{sh.note.get_note}")
        self.console.print(table)

    ### ------------ Sort_by_type part-------------###

    def do_sort_by_type(self, *args):
        "Sorts files by type (images, videos, documents, music, archives)"
        input_path = input(command_message(
            "Enter full path to the folder>>> "))
        if input_path != "":
            sort_by_type(input_path)
        else:
            print(error_message("File path not found"))

    ### ------------ Addressbook part-------------###

    def do_show_rec(self, *args):
        "Shows all book records"
        table = Table()
        table.add_column("ID", style="bright_magenta")
        table.add_column("Tag", style="magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Phone", style="bright_cyan")
        table.add_column("Email", style="blue")
        table.add_column("Address", style="magenta")
        table.add_column("Birthday", style="cyan")
        table.add_column("Company", style="bright_cyan")
        table.add_column("Comment", style="blue")
        for sh in self.book:
            table.add_row(f"{sh.id.get_id}",
                          f"{' '.join([str(item) for item in sh.tags])}",
                          f"{sh.name.get_name}",
                          f"{' '.join([str(item) for item in sh.phones])}",
                          f"{sh.email.get_email}",
                          f"{sh.address.get_address}",
                          f"{sh.birthday.get_birthday}",
                          f"{sh.company.get_company}",
                          f"{sh.comment.get_comment}",
                          )
        self.console.print(table)

    def do_make_rec(self, *args):
        "Make a record to addressbook"
        input_name = input("Enter name>>> ")
        print(self.book.add_full_record(input_name))
    

    def do_find_rec(self, *args):
        "Search in addressbook"
        question = input(command_message("Enter your request>>> "))
        table = Table()
        table.add_column("ID", style="bright_magenta")
        table.add_column("Tag", style="magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Phone", style="bright_cyan")
        table.add_column("Email", style="blue")
        table.add_column("Address", style="magenta")
        table.add_column("Birthday", style="cyan")
        table.add_column("Company", style="bright_cyan")
        table.add_column("Comment", style="blue")
        if len(self.book.find(question)) > 0:
            for sh in self.book.find(question):
                table.add_row(f"{sh.id.get_id}",
                              f"{' '.join([str(item) for item in sh.tags])}",
                              f"{sh.name.get_name}",
                              f"{' '.join([str(item) for item in sh.phones])}",
                              f"{sh.email.get_email}",
                              f"{sh.address.get_address}",
                              f"{sh.birthday.get_birthday}",
                              f"{sh.company.get_company}",
                              f"{sh.comment.get_comment}",
                              )
            self.console.print(table)
        else:
            print(error_message("No record found."))

    def do_del_rec(self, *args):
        "Deletes record in addressbook"
        question = input(command_message("Enter name to detete>>> "))
        print(self.book.remove_record(question))

    def do_edit_ph_rec(self, *args):
        "Edites phone to record in addressbook by name"
        question_name = input(command_message(
            "Enter the name of the record to edit>>> "))
        if question_name != "":
            record_to_edit = self.book.find_record(question_name)
            if record_to_edit:
                edit_old_ph = input(command_message(
                    "Enter the old phone number>>> "))
                edit_new_ph = input(command_message(
                    "Enter the new phone number>>> "))
                if edit_old_ph and edit_new_ph:
                    try:
                        exiting_record_str = self.book.find_exiting_record(
                            record_to_edit.name.get_name)
                        self.book.edit_phone(
                            record_to_edit, exiting_record_str, edit_old_ph, edit_new_ph)
                        print(positive_action("Phone edit successful"))
                    except Exception as ve:
                        print(error_message("No changes made to the phone number."))
                else:
                    print(error_message("No changes made to the phone number."))
        else:
            print(error_message(
                f"No record found with the name: {question_name}"))

    def do_edit_tag_rec(self, *args):
        "Edits tag to record in addressbook by name"
        question_name = input(command_message(
            "Enter the name of the record to edit>>> "))
        if question_name != "":
            record_to_edit = self.book.find_record(question_name)
            if record_to_edit:
                old_tag = input(command_message("Enter the old tag>>> "))
                new_tag = input(command_message("Enter the new tag>>> "))
                if new_tag:
                    try:
                        exiting_record_str = self.book.find_exiting_record(
                            record_to_edit.name.get_name)
                        self.book.edit_teg(
                            record_to_edit, exiting_record_str, old_tag, new_tag)
                        print(positive_action("Tag edit successful"))
                    except Exception as ve:
                        print(error_message("No changes made to the tag."))
                else:
                    print(error_message("No changes made to the tag."))
        else:
            print(error_message(
                f"No record found with the name: {question_name}"))

    def do_cong_rec(self, *args):
        "Search contacts by birthday"
        question = input(command_message("Enter days>>> "))
        table = Table()
        table.add_column("ID", style="bright_magenta")
        table.add_column("Tag", style="magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Phone", style="bright_cyan")
        table.add_column("Email", style="blue")
        table.add_column("Address", style="magenta")
        table.add_column("Birthday", style="cyan")
        table.add_column("Company", style="bright_cyan")
        table.add_column("Comment", style="blue")
        if len(self.book.congratulation(question)) > 0:
            for sh in self.book.congratulation(question):
                table.add_row(f"{sh.id.get_id}",
                              f"{' '.join([str(item) for item in sh.tags])}",
                              f"{sh.name.get_name}",
                              f"{' '.join([str(item) for item in sh.phones])}",
                              f"{sh.email.get_email}",
                              f"{sh.address.get_address}",
                              f"{sh.birthday.get_birthday}",
                              f"{sh.company.get_company}",
                              f"{sh.comment.get_comment}",
                              )
            self.console.print(table)
        else:
            print(error_message("No record found."))

    def do_import(self, *args):
        "Import file in contacts"
        file = input(command_message("Enter filename>>> "))
        self.book.import_files(file)
    
    def do_info(self, *args):
      #####################################  
        print(self.user_info._email)
    def do_set_up_email(self, *args):
      #####################################  
        self.book.set_up_email()
    def do_sm(self, *args):
        self.book.message_sender([self.book.data[0]])
    def do_send(self, *args):
        self.book.send_message()
    def do_edit_email(self,*args):
        email = input('Enter Email:')
        password = input('Enter Password')
        self.book.user_info.add_email(email,password)
    # не працює
    # def do_exp_tag(self, *args):
    #     "Exports contacts by tag to a JSON file"
    #     tag_to_export = input(command_message(
    #         "Enter the tag to export contacts: "))

    #     if tag_to_export != "":
    #         try:
    #             self.book.export_contacts_by_tag(tag_to_export)
    #             print(positive_action(
    #                 f'Contacts with tag "{tag_to_export}" exported successfully!'))
    #         except Exception as e:
    #             print(error_message(f'Error exporting contacts: {str(e)}'))
    #     else:
    #         print(error_message("Tag cannot be empty."))

    # def do_add_comp_rec(self, *args):
    #     "Adds a company to a record in the address book by name"
    #     # record_name = input(command_message("Enter the name of the record to add a company: "))
    #     pass

    # def do_del_comp_rec(self, *args):
    #     "Deletes company in addressbook"
    #     pass


if __name__ == "__main__":
    my_cmd = MyCmd()
    my_cmd.do_help()
    my_cmd.cmdloop()
