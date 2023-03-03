import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types

tocken="5755216407:AAFR19FaCAgdLme_UjpKFYo8m9b8WzR59Vg"

bot=telebot.TeleBot(tocken)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message,"Welcome to talk!")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # print(message)
    # print(message.chat.id)
    bot.send_message(message.chat.id,"Welcome to talk!")

@bot.message_handler(commands=['help'])
def send_infoHelp(message):
    text_msg=f'/siteITStep - перехід на сайт ITStep \n/pogoda - погода в Рівному'
    bot.send_message(message.chat.id, text_msg)

@bot.message_handler(commands=['siteITStep'])
def send_infoUrlItStep(message):
    urlStep="https://rivne.itstep.org/"
    text=f'Сайт академії ШАГ доступний за посиланням: <a href={urlStep}>Сайт IT STEP</a>'
    bot.send_message(message.chat.id,text,parse_mode='html')


@bot.message_handler(commands=['pogoda'])
def send_infoPogoda(message):
    text_msg=f'Погода в Рівному. Температура зараз: {pogodaInRivne()}'
    bot.send_message(message.chat.id, text_msg)


@bot.message_handler(commands=["menu"])
def send_menu(message):
    murkup=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton("Погода в Рівному",callback_data="pogodaInRivne")
    btn2=types.InlineKeyboardButton("Інфо автор",callback_data="infoOwner")
    murkup.add(btn1,btn2)
    bot.send_message(message.chat.id,"Виберіть пункт меню:",parse_mode='html',reply_markup=murkup)


@bot.callback_query_handler(func=lambda call:True)
def callback_woker(call):
    text=""
    if call.data=="pogodaInRivne":
        text=pogodaInRivne()
    elif call.data=="infoOwner":
        text=infoOwner()
    bot.send_message(call.message.chat.id,text)    



def infoOwner():
    return "About info ..."

def pogodaInRivne():
    url="https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%80%D1%96%D0%B2%D0%BD%D0%B5"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    #<p class="today-temp">+4°C</p>
    temp_now=soup.find("p",class_="today-temp")
    # print(temp_now)
    # print(temp_now.get_text())
    return temp_now.get_text()

bot.polling()

