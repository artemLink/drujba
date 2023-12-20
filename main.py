from Bot import Bot
from Style import command_message

if __name__ == '__main__':
    print(command_message("Hello! I'm ContactAssistant"))
    print(command_message('Type help for help'))
    bot = Bot()
    is_active_aplication = True
    while is_active_aplication:
        action = input(command_message('Command: ')).lower()
        if action == 'exit':
            is_active_aplication = False
        else:    
            bot.handle(action) 

