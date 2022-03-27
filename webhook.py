import requests
from discord import Webhook, RequestsWebhookAdapter
import colorama
from colorama import Fore
import threading
# import brain 
# import haram
# import halal




colorama.init()
def WebHook():
 url = input("Webhook Url>>")
 message = input("Message>>")
 threading.Thread(target=WebHook).start()
 while True:
  webhook = Webhook.from_url(f"{url}", adapter=RequestsWebhookAdapter())
  webhook.send(f"{message}")
  print(f"{Fore.GREEN}[+] Sent {message}")
print(f"""
                        \x1b[38;5;213m╔═╦╦══╦══╦╗╔╦══╗╔╦╦══╦╗╔╗╔═╦═╗
                        \033[90m║║║╠║║╣╔═╣╚╝╠╗╔╝║╔╩║║╣║║║║╦╣╬║
                        \033[37m║║║╠║║╣╚╗║╔╗║║║─║╚╦║║╣╚╣╚╣╩╣╗╣
                        \033[37m╚╩═╩══╩══╩╝╚╝╚╝─╚╩╩══╩═╩═╩═╩╩╝ 
                        By ¡nfinity#7700 
                        [1] WebHook Spammer
                                                                """)
allah = input("Select>>")
if allah == '1': 
 WebHook()