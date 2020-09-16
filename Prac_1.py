import telepot
token = '1351770990:AAF_yiJYAEX-BWYBNrL38YxN9aPHY_tVAx8'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id.format(msg["text"]))

TelegramBot.message_loop(handle)
