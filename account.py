from cryptography.fernet import Fernet
import getpass
import msvcrt
import cmd
from rich.console import Console
from rich.table import Table
from art import *
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from random import choice
from string import ascii_letters
from FolderPath import FOLDER_ACCOUNTS_PATH,FOLDER_NOTESBOOKS_PATH,FOLDER_ADDRESSBOOKS_PATH
import os
from Style import positive_action
from Bot import MyCmd
from Notes_book import NotesBook
from Address_book import AddressBook
    

    
class UserAccount():
    
    def __init__(self,user_name=None, user_email=None,user_password=None,):
        self._user_name = user_name
        self._user_email = user_email
        self._user_password = UserPassword(user_password)
        self._account = None
        self._addres_book = None
        self._Notes_book = None
        
    def register_account(self): # Register Func
        self._user_name = input('Input Login:')
        self._account = os.path.join(FOLDER_ACCOUNTS_PATH,f'{self._user_name}_account.txt')
        self._user_password.pass_ok()
        self._addres_book = os.path.join(FOLDER_ADDRESSBOOKS_PATH,f'{self._user_name}_AddressBook.json')
        self._Notes_book = os.path.join(FOLDER_NOTESBOOKS_PATH,f'{self._user_name}_NotesBook.json')
        self.create_AdressBook()
        self.create_notesbook()

        
        
        
        print(self._user_password)
        print(self._user_name)
        self.encryptor(self._user_name,self._user_password._password)
        
    def encryptor(self,login,password):
        key = Fernet.generate_key() # encrypt Key Genaration
        chipers = Fernet(key)
        encrypt_login = chipers.encrypt(login.encode()) # encrypt Login
        encrypt_password = chipers.encrypt(password.encode()) #encrypt Pass
        encrypt_address_book = chipers.encrypt(self._addres_book.encode())
        encrypt_notes_book = chipers.encrypt(self._Notes_book.encode())
        with open(self._account, 'wb') as file: # Save Info
            file.write(key + b'\n')
            file.write(encrypt_login + b'\n')
            file.write(encrypt_password + b'\n')
            file.write(encrypt_address_book + b'\n')
            file.write(encrypt_notes_book)
    
    def descriptor(self,login,password): 
        path = os.path.join(FOLDER_ACCOUNTS_PATH,f'{login}_account.txt')  # Open Account Data
        with open(path, 'r') as file:
            data = file.readlines()
        key = data[0].strip() # get cipheres Key
        ciphered_login = data[1].strip() # get cipheres Login
        ciphered_password = data[2].strip() # get cipheres pass
        ciphered_adr_file = data[3].strip() # get adressbook path
        ciphered_note_file = data[4].strip() # get notebook path
        ciphers = Fernet(key) 
        deciphered_login = ciphers.decrypt(ciphered_login).decode() # decrypt login
        deciphered_password = ciphers.decrypt(ciphered_password).decode() # decryt Password
        deciphered_adr_file = ciphers.decrypt(ciphered_adr_file).decode()
        deciphered_note_file = ciphers.decrypt(ciphered_note_file).decode()
        #print(f'Deciphered Login: {deciphered_login} Password:{password}') # if ok to ok if not ok good bye)
        return[deciphered_login,deciphered_password,deciphered_adr_file,deciphered_note_file]
        # if login == deciphered_login and password == deciphered_password:
        #     self._user_name = deciphered_login
        #     self._user_password = deciphered_password
        #     self._addres_book = deciphered_adr_file
        #     self._Notes_book = deciphered_note_file
            
        

            


    def create_AdressBook(self):
        with open(self._addres_book, 'w') as file:
            return
    
    def create_notesbook(self):
        with open(self._Notes_book, 'w') as file:
            return


    def generate_file_names(self):
        letters = ascii_letters
        filename = ''.join(choice(letters) for _ in range(20)) + '.json' 
        return filename

        


    def login(self): # Login Func
        login = input('Input Login:')
        password = input('Input Password:')
        deciphered_info =   self.descriptor(login,password)
        if login != deciphered_info[0] or password != deciphered_info[1]:
            print('Incorect Login or Password. Try Again')
            return False
        else:
            self._user_name = deciphered_info[0]
            self._user_password = deciphered_info[1]
            self._addres_book = deciphered_info[2]
            self._Notes_book = deciphered_info[3]
            return True
        
    def account_property(self):
        pass

class UserPassword():
    def __init__(self,password=None) -> None:
        self._password=password

    def pass_ok(self):
        password = input('Input Password:')
        repeat_password = input('Repeate The Password:')
        if password != repeat_password:
            print('Passwords do not match. Please try again.')
            return self.pass_ok()
        elif password == repeat_password:
            print('Password is ok')
            self._password = password
    def __str__(self) -> str:
        return f'{self._password}'
# acc = UserAccount()
# print(acc.register_account())
# print(acc.login())



class LoginCMD(cmd.Cmd):
    userAccount = UserAccount()
    
    
    
    word_completer = WordCompleter(['login','register',"exit"])
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
    
    def do_login(self,*args):
        
        if self.userAccount.login():
            botcmd = MyCmd()
            botcmd.adr =  str(self.userAccount._addres_book)
            botcmd.notes_book = NotesBook(self.userAccount._Notes_book)
            botcmd.book = AddressBook(self.userAccount._addres_book)
            botcmd.cmdloop()

    
    def do_register(self,*args):
        self.userAccount.register_account()

    def do_exit(self, *args):
        "Exit from bot"
        print(positive_action("Good bye!"))
        return True
        

if __name__ == '__main__':
    console = Console()
    table = Table()
    table.add_column("Welcome To Help Assistant", style="bright_magenta")
    
    table.add_row(f'login    ---> Log in to the application ')
    table.add_row(f'register ---> Register an account')
    console.print(table)
    logcmd = LoginCMD()
    logcmd.cmdloop()
    





