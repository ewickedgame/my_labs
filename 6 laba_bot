import telebot
import requests

bot = telebot.TeleBot('свой токен я свой не дам ')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Приветики!!!<3 Я могу отправить тебе фото котиков, если ты этого захочешь. Напиши /help, чтобы узнать мои команды:)')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Чтобы получить фото, напиши /maw')

@bot.message_handler(commands=['maw'])
def meow(message):
    r = requests.get('http://thecatapi.com/api/images/get?format=src')
    url = r.url
    bot.send_photo(message.chat.id, url)



@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id,"Приветики, напиши /help")
    else:
        bot.send_message(message.chat.id,"Напиши /help, чтобы узнать мои команды!!!")



bot.polling(none_stop=True)
