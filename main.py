import telepot
import time

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'  # Buraya kendi bot tokenını koy

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg.get('text', '')

    if command == '/start':
        bot.sendMessage(chat_id, 'Selam! Bot aktif.')
    else:
        bot.sendMessage(chat_id, 'Mesajını aldım!')

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Bot çalışıyor...')

while True:
    time.sleep(10)
