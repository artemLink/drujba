from Address_book import AddressBook
from Style import command_message, error_message, positive_action
from Notes_book import NotesBook
import cmd
from rich.console import Console
from rich.table import Table
from art import *
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter


class MyCmd(cmd.Cmd):
    book = AddressBook()
    notes_book = NotesBook()
    console = Console()
    word_completer = WordCompleter(
        ['help', 'make_note', 'make_tag', 'find_note', 'find_tag', 'edit_note', 'edit_title', "del", "show_all", "exit"])
    intro = tprint("designed  by  DRUJBA  team")

    def cmdloop(self, intro=None):
        self.preloop()
        if self.intro:
            self.console.print(self.intro)
        stop = None
        while not stop:
            try:
                session = PromptSession()
                user_input = session.prompt(
                    "Input command>>> ", completer=self.word_completer)
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

    def do_help(self, *args):
        table = Table()
        table.add_column("COMMAND", style="bright_magenta")
        table.add_column("DESCRIPTION", style="bright_blue", no_wrap=True)
        table.add_row("make_note", "Make a note")
        table.add_row("make_tag", "Make a tag")
        table.add_row("find_note", "Search by title and notes")
        table.add_row("find_tag", "Search by tags")
        table.add_row(
            "edit_note", "Edits notes by ID (use search before use)")
        table.add_row(
            "edit_title", "Edits titles by ID (use search before use)")
        table.add_row(
            "del", "Deletes record by ID (use search before use)")
        table.add_row(
            "show_all", "Shows all records")
        table.add_row(
            "help", "Shows a description of the commands")
        self.console.print(table)

    ### ------------ NotesBook part-------------###

    def do_make_note(self, *args):
        "Make a note"
        title = input(command_message("Input title>>> "))
        note = input(command_message("Input note>>> "))
        self.notes_book.add_note(title, note)
        question = input(command_message("Do you want to enter a tag?>> "))
        if question.lower() == 'yes':
            tag = input(command_message("Input tag>>> "))
            self.notes_book.add_tag(tag)
        self.notes_book.save_note()
        print(positive_action("Note added"))

    def do_make_tag(self, *args):
        "Make a tag"
        inp_id = input(command_message(
            "Input ID of the record that changes>>> "))
        tag = input(command_message("Input tag>>> "))
        self.notes_book.add_tag(tag, inp_id)
        self.notes_book.save_note()
        print(positive_action("Tag added"))

    def do_find_note(self, *args):
        "Search by title and notes"
        question = input(command_message("Input your request>>> "))
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
                        f"{sh.note_id.get_id}", f"{sh.addition_date.get_date}", f"{' '.join([str(item) for item in sh.tag])}", f"{sh.title.get_title}", f"{sh.note.get_note}")
            self.console.print(table)
        else:
            print(error_message("No notes found."))

    def do_find_tag(self, *args):
        "Search by tags"
        question = input(command_message("Input your request>>> "))
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
                        f"{sh.note_id.get_id}", f"{sh.addition_date.get_date}", f"{' '.join([str(item) for item in sh.tag])}", f"{sh.title.get_title}", f"{sh.note.get_note}")

            self.console.print(table)
        else:
            print(error_message("No notes found."))

    def do_edit_note(self, *args):
        "Edits notes"
        inp_id = input(command_message(
            "Input ID of the record that changes>>> "))
        note = input(command_message("Input new note>>> "))
        self.notes_book.edit_note(inp_id, note)
        self.notes_book.save_note()
        print(positive_action("Note has been edited"))

    def do_edit_title(self, *args):
        "Edits titles"
        inp_id = input(command_message(
            "Input ID of the record that changes>>> "))
        title = input(command_message("Input new title>>> "))
        self.notes_book.edit_title(inp_id, title)
        self.notes_book.save_note()
        print(positive_action("Title has been edited"))

    def do_del(self, *args):
        "Deletes record"
        inp_id = input(command_message(
            "Input ID of the record that delete>>> "))
        self.notes_book.delete_note(inp_id)
        self.notes_book.save_note()
        print(positive_action("Record deleted successfully"))

    def do_show_all(self, *args):
        "Shows all records"
        table = Table()
        table.add_column("ID", style="bright_magenta")
        table.add_column("Date", style="magenta")
        table.add_column("Tag", style="cyan")
        table.add_column("Title", style="bright_cyan")
        table.add_column("Note", style="blue")
        for sh in self.notes_book:
            if isinstance(sh.tag, list):
                table.add_row(f"{sh.note_id.get_id}", f"{sh.addition_date.get_date}",
                              f"{' '.join([str(item) for item in sh.tag])}", f"{sh.title.get_title}", f"{sh.note.get_note}")
        self.console.print(table)


if __name__ == "__main__":
    my_cmd = MyCmd()
    my_cmd.cmdloop()
