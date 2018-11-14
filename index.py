import telebot
import os
import urllib.request as urllib2

bot = telebot.TeleBot("746612461:AAHHnGHEFbyBzIWnte6rG40vZWFmqmnb1Pg")

################################################################################################################
################################################################################################################
################################################################################################################

@bot.message_handler(commands = ['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("/start", "Exit")
    user_markup.row("Lab 01")
    user_markup.row("Lab 02")
    user_markup.row("Lab 03")
    user_markup.row("Lab 04")
    user_markup.row("Lab 05")
    bot.send_message(message.from_user.id, "welcome...", reply_markup = user_markup)

################################################################################################################
################################################################################################################
################################################################################################################

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text == "Exit":
        hide_markup = telebot.types.ReplyKeyboardRemove() # Нет такой функции
        bot.send_message(message.from_user.id, "Bye", reply_markup = hide_markup)

################################################################################################################
################################################################################################################
################################################################################################################

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, message.text)
    #if message.text == "Lab 01":
    #    markup = telebot.types.InlineKeyboardMarkup()
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 01", callback_data="lab_01_variant_01"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 02", callback_data="lab_01_variant_02"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 03", callback_data="lab_01_variant_03"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 04", callback_data="lab_01_variant_04"))

    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 05", callback_data="lab_01_variant_05"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 06", callback_data="lab_01_variant_06"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 07", callback_data="lab_01_variant_07"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 08", callback_data="lab_01_variant_08"))

    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 09", callback_data="lab_01_variant_09"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 10", callback_data="lab_01_variant_10"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 11", callback_data="lab_01_variant_11"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 12", callback_data="lab_01_variant_12"))

    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 13", callback_data="lab_01_variant_13"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 14", callback_data="lab_01_variant_14"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 15", callback_data="lab_01_variant_15"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 16", callback_data="lab_01_variant_16"))
    #    bot.send_message(message.from_user.id, "Choose your variant", reply_markup = markup)

    #elif message.text == "Lab 02":
    #    markup = telebot.types.InlineKeyboardMarkup()
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 01", callback_data="lab_02_variant_01"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 02", callback_data="lab_02_variant_02"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 03", callback_data="lab_02_variant_03"))
    #    markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 04", callback_data="lab_02_variant_04"))

################################################################################################################
################################################################################################################
################################################################################################################

@bot.callback_query_handler(func=lambda call:True)
def call_back_payment(call):
    # Lab 01
    # Lab 01/Variant 01
    if call.data == "lab_01_variant_01":
        url = 'https://drive.google.com/uc?export=download&id=1sd1snZ8-1IW9baKh6nL_1F1UQlvOB-sb'
        urllib2.urlretrieve(url, "Lab 01 variant 01.rar")
        document = open("Lab 01 variant 01.rar", "rb")
        bot.send_chat_action(call.from_user.id, "upload_document")
        bot.send_document(call.from_user.id, document)
        document.close()
        bot.send_message(call.message.chat.id, "")
    # Lab 01/Variant 02
    elif call.data == "Lab 01/Variant 02":
        url = 'https://drive.google.com/uc?export=download&id=188aI7rh1lOWN5p7ouU0CvS_2wSbx5dPu'
        urllib2.urlretrieve(url, "Lab 01 variant 02.rar")
        document = open("Lab 01 variant 02.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 03
    elif call.data == "Lab 01/Variant 03":
        url = 'https://drive.google.com/uc?export=download&id=1ZJpEGukVXwEXOHznV68FZ12sVW-IAWF7'
        urllib2.urlretrieve(url, "Lab 01 variant 03.rar")
        document = open("Lab 01 variant 03.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 04
    elif call.data == "Lab 01/Variant 04":
        url = 'https://drive.google.com/uc?export=download&id=1TPPDnjGRqqOUXoHLhS1xQQVc5qWAXUlK'
        urllib2.urlretrieve(url, "Lab 01 variant 04.rar")
        document = open("Lab 01 variant 04.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 05
    elif call.data == "Lab 01/Variant 05":
        url = 'https://drive.google.com/uc?export=download&id=1cKjD758MgPB23X_I3E0SHAJdW9cRqTSK'
        urllib2.urlretrieve(url, "Lab 01 variant 05.rar")
        document = open("Lab 01 variant 05.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 06
    elif call.data == "Lab 01/Variant 06":
        url = 'https://drive.google.com/uc?export=download&id=14ySKjBfEdlNpQQd1FO-j5CcyTg4911v3'
        urllib2.urlretrieve(url, "Lab 01 variant 06.rar")
        document = open("Lab 01 variant 06.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 07
    elif call.data == "Lab 01/Variant 07":
        url = 'https://drive.google.com/uc?export=download&id=15MUW7gwWtnvzs-ziKcDf-Kkwz5NexdZZ'
        urllib2.urlretrieve(url, "Lab 01 variant 07.rar")
        document = open("Lab 01 variant 07.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 08
    elif call.data == "Lab 01/Variant 08":
        url = 'https://drive.google.com/uc?export=download&id=1SBeSDrFF_u8JQzatCq-3GSau5v4rgfIp'
        urllib2.urlretrieve(url, "Lab 01 variant 08.rar")
        document = open("Lab 01 variant 08.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 09
    elif call.data == "Lab 01/Variant 09":
        url = 'https://drive.google.com/uc?export=download&id=1rVXB6a8E2l6NLPUekwFSUmqN-mFZ-vI1'
        urllib2.urlretrieve(url, "Lab 01 variant 09.rar")
        document = open("Lab 01 variant 09.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 10
    elif call.data == "Lab 01/Variant 10":
        url = 'https://drive.google.com/uc?export=download&id=1ZqE9-wvT3vR4y7qQ2XgRKlmZGgfkM6Rv'
        urllib2.urlretrieve(url, "Lab 01 variant 10.rar")
        document = open("Lab 01 variant 10.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 11
    elif call.data == "Lab 01/Variant 11":
        url = 'https://drive.google.com/uc?export=download&id=1Sh7GhCNDNuWeM37apZZesSMVGOvKe8Al'
        urllib2.urlretrieve(url, "Lab 01 variant 11.rar")
        document = open("Lab 01 variant 11.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 12
    elif call.data == "Lab 01/Variant 12":
        url = 'https://drive.google.com/uc?export=download&id=10CSSOzpD1blWf3LDTJx1YTcLmhH-ssZW'
        urllib2.urlretrieve(url, "Lab 01 variant 12.rar")
        document = open("Lab 01 variant 12.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 13
    elif call.data == "Lab 01/Variant 13":
        url = 'https://drive.google.com/uc?export=download&id=1KdB1AlaMkQoK1Sgt2BHDDB6iLYTgavWR'
        urllib2.urlretrieve(url, "Lab 01 variant 13.rar")
        document = open("Lab 01 variant 13.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 14
    elif call.data == "Lab 01/Variant 14":
        url = 'https://drive.google.com/uc?export=download&id=1fHHsuV5lhAkj6DJEz1I2sDzWaWlhbrrk'
        urllib2.urlretrieve(url, "Lab 01 variant 14.rar")
        document = open("Lab 01 variant 14.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 15
    elif call.data == "Lab 01/Variant 15":
        url = 'https://drive.google.com/uc?export=download&id=1hZQTMAvnFr04DG3i0nz92ZlMHL-3ZfVY'
        urllib2.urlretrieve(url, "Lab 01 variant 15.rar")
        document = open("Lab 01 variant 15.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 01/Variant 16
    elif call.data == "Lab 01/Variant 16":
        url = 'https://drive.google.com/uc?export=download&id=1UGdickb9FtuP6qgbd64MgTCb_Y96VfGc'
        urllib2.urlretrieve(url, "Lab 01 variant 16.rar")
        document = open("Lab 01 variant 16.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()

    # Lab 02
    # Lab 02/Variant 01
    elif call.data == "lab_02_variant_01":
        url = 'https://drive.google.com/uc?export=download&id=1vMHCfk2b7txtqeKU0vs8Wq70zd2GOl2s'
        urllib2.urlretrieve(url, "Lab 02 variant 01.rar")
        document = open("Lab 02 variant 01.rar", "rb")
        bot.send_chat_action(call.from_user.id, "upload_document")
        bot.send_document(call.from_user.id, document)
        document.close()
        bot.send_message(call.message.chat.id, "")
    # Lab 02/Variant 02
    elif call.data == "Lab 02/Variant 02":
        url = 'https://drive.google.com/uc?export=download&id=1gz0iGuJp0Do4ALtoQd_BPVk99LUyahb3'
        urllib2.urlretrieve(url, "Lab 02 variant 02.rar")
        document = open("Lab 02 variant 02.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 02/Variant 03
    elif call.data == "Lab 02/Variant 03":
        url = 'https://drive.google.com/uc?export=download&id=1ikLuJiqW-Hp_TjyNdkZl8SArnwJWLyws'
        urllib2.urlretrieve(url, "Lab 02 variant 03.rar")
        document = open("Lab 02 variant 03.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 02/Variant 04
    elif call.data == "Lab 02/Variant 04":
        url = 'https://drive.google.com/uc?export=download&id=1c597BFu770wqOqg7mVKEN1-O2AtLWknv'
        urllib2.urlretrieve(url, "Lab 02 variant 04.rar")
        document = open("Lab 02 variant 04.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    # Lab 02/Variant 05
    elif call.data == "Lab 02/Variant 05":
        url = 'https://drive.google.com/uc?export=download&id=1uV-Gi8eTFg9kwmAvBzbz-DD1jjxgyks9'
        urllib2.urlretrieve(url, "Lab 02 variant 05.rar")
        document = open("Lab 02 variant 05.rar", "rb")
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()

################################################################################################################
################################################################################################################
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
