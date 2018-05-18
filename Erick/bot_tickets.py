import requests
import datetime
import handler
from response_modules import response_module

token = '584063714:AAGwFvuWu3GkbtRA3nZUJhOUbNygCWOHSlE' #Token del Bot
erick = handler.BotHandler(token)

def main():
    new_offset = 0
    print('Iniciando sistema...')

    while True:
    	#Se toma todos los valores presentes en el mensaje
        all_updates=erick.get_updates(new_offset)

        #Se comienza el proceso para contestar el mensaje
        if len(all_updates) > 0:
            for current_update in all_updates:

            	#Se imprimen los datos obtenidos
                print(current_update)
                first_update_id = current_update['update_id']

                #En esta parte toma el texto del mensaje recibido
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']

                #En esta parte se toma el nombre del usuario con el que se conversa
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                #Se procesa el mensaje
                
                if first_chat_text == "/start":
                    first_chat_text = "hola"
                
                response = response_module.process_message(first_chat_text)
                erick.send_message(first_chat_id, response)
                new_offset = first_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()