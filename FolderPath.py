import os
current_directory = os.getcwd()

FOLDER_ACCOUNTS_PATH = os.path.join(current_directory,'Accounts')
if not os.path.exists(FOLDER_ACCOUNTS_PATH):
    os.makedirs(FOLDER_ACCOUNTS_PATH)


FOLDER_ADDRESSBOOKS_PATH = os.path.join(current_directory,'AddresBooksFolder')
if not os.path.exists(FOLDER_ADDRESSBOOKS_PATH):
    os.makedirs(FOLDER_ADDRESSBOOKS_PATH)

FOLDER_NOTESBOOKS_PATH = os.path.join(current_directory,'NotesBooksFolder')

if not os.path.exists(FOLDER_NOTESBOOKS_PATH):
    os.makedirs(FOLDER_NOTESBOOKS_PATH)


def create_folders():
    if not os.path.exists(FOLDER_ACCOUNTS_PATH):
        os.makedirs(FOLDER_ACCOUNTS_PATH)
    if not os.path.exists(FOLDER_ADDRESSBOOKS_PATH):
        os.makedirs(FOLDER_ADDRESSBOOKS_PATH)
    if not os.path.exists(FOLDER_NOTESBOOKS_PATH):
        os.makedirs(FOLDER_NOTESBOOKS_PATH)