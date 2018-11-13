import telebot
import os
import urllib.request as urllib2

bot = telebot.TeleBot("746612461:AAHHnGHEFbyBzIWnte6rG40vZWFmqmnb1Pg")

@bot.message_handler(commands = ['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("/start", "/stop")
    user_markup.row("Lab 01")
    bot.send_message(message.from_user.id, "Добро пожаловать...", reply_markup = user_markup)

@bot.message_handler(content_types = ['Lab 01'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row("Back")
    user_markup.row("Lab 01/Variant 01")
    user_markup.row("Lab 01/Variant 02")
    user_markup.row("Lab 01/Variant 03")
    user_markup.row("Lab 01/Variant 04")
    user_markup.row("Lab 01/Variant 05")
    user_markup.row("Lab 01/Variant 06")
    user_markup.row("Lab 01/Variant 07")
    user_markup.row("Lab 01/Variant 08")
    user_markup.row("Lab 01/Variant 09")
    user_markup.row("Lab 01/Variant 10")
    user_markup.row("Lab 01/Variant 11")
    user_markup.row("Lab 01/Variant 12")
    user_markup.row("Lab 01/Variant 13")
    user_markup.row("Lab 01/Variant 14")
    user_markup.row("Lab 01/Variant 15")
    user_markup.row("Lab 01/Variant 16")

@bot.message_handler(content_types = ['Back'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("/start", "/stop")
    user_markup.row("Lab 01")

#@bot.message_handler(commands = ['stop'])
#def handle_text(message):
    #hide_markup = telebot.types.ReplyKeyboardHide() # Нет такой функции
    #bot.send_message(message.from_user.id, "...", reply_markup = hide_markup)

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    # Lab 01/Variant 01
    if message.text == "Lab 01/Variant 01":
        url = 'https://drive.google.com/uc?export=download&id=1sd1snZ8-1IW9baKh6nL_1F1UQlvOB-sb'
        urllib2.urlretrieve(url, "Lab 01 variant 01.rar")
        document = open("Lab 01 variant 01.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 02
    elif message.text == "Lab 01/Variant 02":
        url = 'https://drive.google.com/uc?export=download&id=188aI7rh1lOWN5p7ouU0CvS_2wSbx5dPu'
        urllib2.urlretrieve(url, "Lab 01 variant 02.rar")
        document = open("Lab 01 variant 02.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 03
    elif message.text == "Lab 01/Variant 03":
        url = 'https://drive.google.com/uc?export=download&id=1ZJpEGukVXwEXOHznV68FZ12sVW-IAWF7'
        urllib2.urlretrieve(url, "Lab 01 variant 03.rar")
        document = open("Lab 01 variant 03.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 04
    elif message.text == "Lab 01/Variant 04":
        url = 'https://drive.google.com/uc?export=download&id=1TPPDnjGRqqOUXoHLhS1xQQVc5qWAXUlK'
        urllib2.urlretrieve(url, "Lab 01 variant 04.rar")
        document = open("Lab 01 variant 04.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 05
    elif message.text == "Lab 01/Variant 05":
        url = 'https://drive.google.com/uc?export=download&id=1cKjD758MgPB23X_I3E0SHAJdW9cRqTSK'
        urllib2.urlretrieve(url, "Lab 01 variant 05.rar")
        document = open("Lab 01 variant 05.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 06
    elif message.text == "Lab 01/Variant 06":
        url = 'https://drive.google.com/uc?export=download&id=14ySKjBfEdlNpQQd1FO-j5CcyTg4911v3'
        urllib2.urlretrieve(url, "Lab 01 variant 06.rar")
        document = open("Lab 01 variant 06.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 07
    elif message.text == "Lab 01/Variant 07":
        url = 'https://drive.google.com/uc?export=download&id=15MUW7gwWtnvzs-ziKcDf-Kkwz5NexdZZ'
        urllib2.urlretrieve(url, "Lab 01 variant 07.rar")
        document = open("Lab 01 variant 07.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 08
    elif message.text == "Lab 01/Variant 08":
        url = 'https://drive.google.com/uc?export=download&id=1SBeSDrFF_u8JQzatCq-3GSau5v4rgfIp'
        urllib2.urlretrieve(url, "Lab 01 variant 08.rar")
        document = open("Lab 01 variant 08.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 09
    elif message.text == "Lab 01/Variant 09":
        url = 'https://drive.google.com/uc?export=download&id=1rVXB6a8E2l6NLPUekwFSUmqN-mFZ-vI1'
        urllib2.urlretrieve(url, "Lab 01 variant 09.rar")
        document = open("Lab 01 variant 09.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 10
    elif message.text == "Lab 01/Variant 10":
        url = 'https://drive.google.com/uc?export=download&id=1ZqE9-wvT3vR4y7qQ2XgRKlmZGgfkM6Rv'
        urllib2.urlretrieve(url, "Lab 01 variant 10.rar")
        document = open("Lab 01 variant 10.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 11
    elif message.text == "Lab 01/Variant 11":
        url = 'https://drive.google.com/uc?export=download&id=1Sh7GhCNDNuWeM37apZZesSMVGOvKe8Al'
        urllib2.urlretrieve(url, "Lab 01 variant 11.rar")
        document = open("Lab 01 variant 11.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 12
    elif message.text == "Lab 01/Variant 12":
        url = 'https://drive.google.com/uc?export=download&id=10CSSOzpD1blWf3LDTJx1YTcLmhH-ssZW'
        urllib2.urlretrieve(url, "Lab 01 variant 12.rar")
        document = open("Lab 01 variant 12.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 13
    elif message.text == "Lab 01/Variant 13":
        url = 'https://drive.google.com/uc?export=download&id=1KdB1AlaMkQoK1Sgt2BHDDB6iLYTgavWR'
        urllib2.urlretrieve(url, "Lab 01 variant 13.rar")
        document = open("Lab 01 variant 13.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 14
    elif message.text == "Lab 01/Variant 14":
        url = 'https://drive.google.com/uc?export=download&id=1fHHsuV5lhAkj6DJEz1I2sDzWaWlhbrrk'
        urllib2.urlretrieve(url, "Lab 01 variant 14.rar")
        document = open("Lab 01 variant 14.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 15
    elif message.text == "Lab 01/Variant 15":
        url = 'https://drive.google.com/uc?export=download&id=1hZQTMAvnFr04DG3i0nz92ZlMHL-3ZfVY'
        urllib2.urlretrieve(url, "Lab 01 variant 15.rar")
        document = open("Lab 01 variant 15.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 16
    elif message.text == "Lab 01/Variant 16":
        url = 'https://drive.google.com/uc?export=download&id=1UGdickb9FtuP6qgbd64MgTCb_Y96VfGc'
        urllib2.urlretrieve(url, "Lab 01 variant 16.rar")
        document = open("Lab 01 variant 16.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()

################################################################################################################

print(bot.get_me())

def log(message, answer):
    print("\n ------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3})" . format(message.from_user.first_name,
                                                                     message.from_user.last_name,
                                                                     str(message.from_user.id),
                                                                     message.text))
    print(answer)

@bot.message_handler(commands = ['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Мои возможности весьма специфичны. Но, ты только посмотри! Все работает!")

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text == "a":
        answer = "b"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "b":
        answer = "c"
        log(message, answer)
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True, interval = 0)
