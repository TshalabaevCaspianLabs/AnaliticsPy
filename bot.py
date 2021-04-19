from telebot import TeleBot



api = '1722995619:AAFD3SqWOCp2ZCjlUhkkYCYp6MvZfJeVPu8'
bot = TeleBot(api, parse_mode='html')




@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет, ты попал в бота для получения данных'
                                      ' с сервера в виде exele файлов\n\n'
                                      'Напиши боту команду /info он пришлет тебе все файлы с статистикой')




@bot.message_handler(commands=['info'])
def send_exele(message):
    chat_id = message.chat.id

    rekshop = open('rekshop.xls', 'rb')
    bot.send_document(chat_id, rekshop)

    voltiq = open('voltiq.xls', 'rb')
    bot.send_document(chat_id, voltiq)

    roboshop = open('roboshop.xls', 'rb')
    bot.send_document(chat_id, roboshop)

    arduinopro = open('arduinopro.xls', 'rb')
    bot.send_document(chat_id, arduinopro)

    bot.send_message(chat_id, text='Для завершения анализа обратитесь к программисту')







bot.polling(none_stop=True)