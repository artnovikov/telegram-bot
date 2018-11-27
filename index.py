import telebot
import os
import urllib.request as urllib2

bot = telebot.TeleBot("746612461:AAHHnGHEFbyBzIWnte6rG40vZWFmqmnb1Pg")

################################################################################################################
################################################################################################################
################################################################################################################

def download_lab(number_of_lab, number_of_variant, google_link, user_id):
    bot.send_message(user_id, "Something...")
    url = 'https://drive.google.com/uc?export=download&id=' + google_link
    urllib2.urlretrieve(url, "Lab " + number_of_lab + " variant " + number_of_variant + ".rar")
    document = open("Lab " + number_of_lab + " variant " + number_of_variant + ".rar", "rb")
    bot.send_chat_action(user_id, "upload_document")
    bot.send_document(user_id, document)
    document.close()

@bot.message_handler(commands = ['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row("Exit")
    user_markup.row("Help")
    user_markup.row("Lab 01")
    user_markup.row("Lab 02")
    user_markup.row("Lab 05")
    user_markup.row("Lab 06")
    bot.send_message(message.from_user.id, "Hello, we're glad to c u. Please choose lab number.", reply_markup = user_markup)

################################################################################################################
################################################################################################################
################################################################################################################

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text == "Exit":
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Thank you for using our bot...", reply_markup = hide_markup)
    elif message.text == "Help":
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Choose your variant. Download and unzip the archive on your desktop. Run the \"Project1.sln\" file. Enjoy.", reply_markup = hide_markup)
    elif message.text == "Lab 01":
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 01", callback_data="lab_01_variant_01"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 02", callback_data="lab_01_variant_02"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 03", callback_data="lab_01_variant_03"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 04", callback_data="lab_01_variant_04"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 05", callback_data="lab_01_variant_05"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 06", callback_data="lab_01_variant_06"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 07", callback_data="lab_01_variant_07"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 08", callback_data="lab_01_variant_08"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 09", callback_data="lab_01_variant_09"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 10", callback_data="lab_01_variant_10"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 11", callback_data="lab_01_variant_11"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 12", callback_data="lab_01_variant_12"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 13", callback_data="lab_01_variant_13"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 14", callback_data="lab_01_variant_14"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 15", callback_data="lab_01_variant_15"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 01/Variant 16", callback_data="lab_01_variant_16"))
        bot.send_message(message.from_user.id, "Choose your variant", reply_markup = markup)
    elif message.text == "Lab 02":
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 01", callback_data="lab_02_variant_01"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 02", callback_data="lab_02_variant_02"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 03", callback_data="lab_02_variant_03"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 04", callback_data="lab_02_variant_04"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 05", callback_data="lab_02_variant_05"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 06", callback_data="lab_02_variant_06"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 07", callback_data="lab_02_variant_07"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 08", callback_data="lab_02_variant_08"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 09", callback_data="lab_02_variant_09"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 10", callback_data="lab_02_variant_10"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 11", callback_data="lab_02_variant_11"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 12", callback_data="lab_02_variant_12"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 13", callback_data="lab_02_variant_13"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 14", callback_data="lab_02_variant_14"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 15", callback_data="lab_02_variant_15"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 02/Variant 16", callback_data="lab_02_variant_16"))
        bot.send_message(message.from_user.id, "Choose your variant", reply_markup = markup)
    elif message.text == "Lab 05":
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 01", callback_data="lab_05_variant_01"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 02", callback_data="lab_05_variant_02"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 03", callback_data="lab_05_variant_03"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 04", callback_data="lab_05_variant_04"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 05", callback_data="lab_05_variant_05"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 06", callback_data="lab_05_variant_06"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 07", callback_data="lab_05_variant_07"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 08", callback_data="lab_05_variant_08"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 09", callback_data="lab_05_variant_09"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 10", callback_data="lab_05_variant_10"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 11", callback_data="lab_05_variant_11"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 12", callback_data="lab_05_variant_12"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 13", callback_data="lab_05_variant_13"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 14", callback_data="lab_05_variant_14"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 15", callback_data="lab_05_variant_15"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 05/Variant 16", callback_data="lab_05_variant_16"))
        bot.send_message(message.from_user.id, "Choose your variant", reply_markup = markup)
    elif message.text == "Lab 06":
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Lab 06/Variant 01", callback_data="lab_06_variant_01"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 06/Variant 02", callback_data="lab_06_variant_02"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 06/Variant 03", callback_data="lab_06_variant_03"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 06/Variant 04", callback_data="lab_06_variant_04"))

        markup.add(telebot.types.InlineKeyboardButton("Lab 06/Variant 05", callback_data="lab_06_variant_05"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 06/Variant 06", callback_data="lab_06_variant_06"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 06/Variant 07", callback_data="lab_06_variant_07"))
        markup.add(telebot.types.InlineKeyboardButton("Lab 06/Variant 08", callback_data="lab_06_variant_08"))
        bot.send_message(message.from_user.id, "Choose your variant", reply_markup = markup)

################################################################################################################
################################################################################################################
################################################################################################################

@bot.callback_query_handler(func=lambda call:True)
def call_back_payment(call):
    # Lab 01
    # Lab 01/Variant 01
    if call.data == "lab_01_variant_01":
        download_lab("01", "01", "1sd1snZ8-1IW9baKh6nL_1F1UQlvOB-sb", call.from_user.id)
    # Lab 01/Variant 02
    elif call.data == "lab_01_variant_02":
        download_lab("01", "02", "188aI7rh1lOWN5p7ouU0CvS_2wSbx5dPu", call.from_user.id)
    # Lab 01/Variant 03
    elif call.data == "lab_01_variant_03":
        download_lab("01", "03", "1ZJpEGukVXwEXOHznV68FZ12sVW-IAWF7", call.from_user.id)
    # Lab 01/Variant 04
    elif call.data == "lab_01_variant_04":
        download_lab("01", "04", "1TPPDnjGRqqOUXoHLhS1xQQVc5qWAXUlK", call.from_user.id)
    # Lab 01/Variant 05
    elif call.data == "lab_01_variant_05":
        download_lab("01", "05", "1cKjD758MgPB23X_I3E0SHAJdW9cRqTSK", call.from_user.id)
    # Lab 01/Variant 06
    elif call.data == "lab_01_variant_06":
        download_lab("01", "06", "14ySKjBfEdlNpQQd1FO-j5CcyTg4911v3", call.from_user.id)
    # Lab 01/Variant 07
    elif call.data == "lab_01_variant_07":
        download_lab("01", "07", "15MUW7gwWtnvzs-ziKcDf-Kkwz5NexdZZ", call.from_user.id)
    # Lab 01/Variant 08
    elif call.data == "lab_01_variant_08":
        download_lab("01", "08", "1SBeSDrFF_u8JQzatCq-3GSau5v4rgfIp", call.from_user.id)
    # Lab 01/Variant 09
    elif call.data == "lab_01_variant_09":
        download_lab("01", "09", "1rVXB6a8E2l6NLPUekwFSUmqN-mFZ-vI1", call.from_user.id)
    # Lab 01/Variant 10
    elif call.data == "lab_01_variant_10":
        download_lab("01", "10", "1ZqE9-wvT3vR4y7qQ2XgRKlmZGgfkM6Rv", call.from_user.id)
    # Lab 01/Variant 11
    elif call.data == "lab_01_variant_11":
        download_lab("01", "11", "1Sh7GhCNDNuWeM37apZZesSMVGOvKe8Al", call.from_user.id)
    # Lab 01/Variant 12
    elif call.data == "lab_01_variant_12":
        download_lab("01", "12", "10CSSOzpD1blWf3LDTJx1YTcLmhH-ssZW", call.from_user.id)
    # Lab 01/Variant 13
    elif call.data == "lab_01_variant_13":
        download_lab("01", "13", "1KdB1AlaMkQoK1Sgt2BHDDB6iLYTgavWR", call.from_user.id)
    # Lab 01/Variant 14
    elif call.data == "lab_01_variant_14":
        download_lab("01", "14", "1fHHsuV5lhAkj6DJEz1I2sDzWaWlhbrrk", call.from_user.id)
    # Lab 01/Variant 15
    elif call.data == "lab_01_variant_15":
        download_lab("01", "15", "1hZQTMAvnFr04DG3i0nz92ZlMHL-3ZfVY", call.from_user.id)
    # Lab 01/Variant 16
    elif call.data == "lab_01_variant_16":
        download_lab("01", "16", "1UGdickb9FtuP6qgbd64MgTCb_Y96VfGc", call.from_user.id)
    # Lab 02
    # Lab 02/Variant 01
    elif call.data == "lab_02_variant_01":
        download_lab("02", "01", "1vMHCfk2b7txtqeKU0vs8Wq70zd2GOl2s", call.from_user.id)
    # Lab 02/Variant 02
    elif call.data == "lab_02_variant_02":
        download_lab("02", "02", "1gz0iGuJp0Do4ALtoQd_BPVk99LUyahb3", call.from_user.id)
    # Lab 02/Variant 03
    elif call.data == "lab_02_variant_03":
        download_lab("02", "03", "1ikLuJiqW-Hp_TjyNdkZl8SArnwJWLyws", call.from_user.id)
    # Lab 02/Variant 04
    elif call.data == "lab_02_variant_04":
        download_lab("02", "04", "1c597BFu770wqOqg7mVKEN1-O2AtLWknv", call.from_user.id)
    # Lab 02/Variant 05
    elif call.data == "lab_02_variant_05":
        download_lab("02", "05", "1uV-Gi8eTFg9kwmAvBzbz-DD1jjxgyks9", call.from_user.id)
    # Lab 02/Variant 06
    elif call.data == "lab_02_variant_06":
        download_lab("02", "06", "1spRtb7fFlHhNjxaXjDrOkI7PoSsoSXxh", call.from_user.id)
    # Lab 02/Variant 07
    elif call.data == "lab_02_variant_07":
        download_lab("02", "07", "1Udnv9wct-ath8BsDOVtI06AwOhF7aWmj", call.from_user.id)
    # Lab 02/Variant 08
    elif call.data == "lab_02_variant_08":
        download_lab("02", "08", "15QL-VO1m8_2EHh9Uc-ZKU0isepL9y_8y", call.from_user.id)
    # Lab 02/Variant 09
    elif call.data == "lab_02_variant_09":
        download_lab("02", "09", "1nPYSWsuCLExEg6JCnwtWNNQ_1-AWCT6L", call.from_user.id)
    # Lab 02/Variant 10
    elif call.data == "lab_02_variant_10":
        download_lab("02", "10", "10Z5Xw4CIZ8By_aWDRMO5entgHCedXnzF", call.from_user.id)
    # Lab 02/Variant 11
    elif call.data == "lab_02_variant_11":
        download_lab("02", "10", "13uMpuYW7__3iO4prnJGLBNKAzW9VqFMW", call.from_user.id)
    # Lab 02/Variant 12
    elif call.data == "lab_02_variant_12":
        download_lab("02", "12", "1g88u4v_OFqjUML69kczKWIh8XBkXtEnK", call.from_user.id)
    # Lab 02/Variant 13
    elif call.data == "lab_02_variant_13":
        download_lab("02", "13", "1ZmZH6YwDAozQAm2V5UAJ5_H8pKZ2wwob", call.from_user.id)
    # Lab 02/Variant 14
    elif call.data == "lab_02_variant_14":
        download_lab("02", "14", "18Nf-cVascVpe7ul0owcEk0ehHrtnN4XU", call.from_user.id)
    # Lab 02/Variant 15
    elif call.data == "lab_02_variant_15":
        download_lab("02", "15", "1WABXwwBlsUXiW6mRzZ3chtGDnAqM9Mhf", call.from_user.id)
    # Lab 02/Variant 16
    elif call.data == "lab_02_variant_16":
        download_lab("02", "16", "1iq39UhSa3K7uF86xFtzRLmuFGjsuMPHZ", call.from_user.id)
	# Lab 05
	# Lab 05/Variant 01
    elif call.data == "lab_05_variant_01":
        download_lab("05", "01", "1-0aNuz27F7Voumakgm6sKTwkhdeg2zxI", call.from_user.id)
    # Lab 05/Variant 02
    elif call.data == "lab_05_variant_02":
        download_lab("05", "02", "1SxrJFMtOalgfxzy_2WWnNPM-XLL5aE2q", call.from_user.id)
    # Lab 05/Variant 03
    elif call.data == "lab_05_variant_03":
        download_lab("05", "03", "1URqDqkkFt639W5ARFb4tSbD_ZlZMmGGC", call.from_user.id)
    # Lab 05/Variant 04
    elif call.data == "lab_05_variant_04":
        download_lab("05", "04", "1q7LLyjPIX4r8UJgND9I33b-NHKTfCAmB", call.from_user.id)
    # Lab 05/Variant 05
    elif call.data == "lab_05_variant_05":
        download_lab("05", "05", "1YD3UoMc0uPu2CUFa56eS_eAewd5Nv8Xh", call.from_user.id)
    # Lab 05/Variant 06
    elif call.data == "lab_05_variant_06":
        download_lab("05", "06", "1siMHmHBTrok6VffUH3SFmH4GUq7AVPg4", call.from_user.id)
    # Lab 05/Variant 07
    elif call.data == "lab_05_variant_07":
        download_lab("05", "07", "1rBKXzaFywiqKYdXh3SB9A-l8xRXX9UQc", call.from_user.id)
    # Lab 05/Variant 08
    elif call.data == "lab_05_variant_08":
        download_lab("05", "08", "13uT0Y42BeljKvwWWoCUMasVgrZElIDxm", call.from_user.id)
    # Lab 05/Variant 09
    elif call.data == "lab_05_variant_09":
        download_lab("05", "09", "1Knh7-JEWYhuX5yMA3XNDvo1MfO7CnLDG", call.from_user.id)
    # Lab 05/Variant 10
    elif call.data == "lab_05_variant_10":
        download_lab("05", "10", "1R34OjbJmZVYHvSfrRINbHSzm_STl8b9-", call.from_user.id)
    # Lab 05/Variant 11
    elif call.data == "lab_05_variant_11":
        download_lab("05", "11", "1pHh-dfUNtVxntQFs41-jRf5uyblGx59D", call.from_user.id)
    # Lab 05/Variant 12
    elif call.data == "lab_05_variant_12":
        download_lab("05", "12", "1Z4dS3DZnBKUeniaYWzl6DOtx32UDfIsU", call.from_user.id)
    # Lab 05/Variant 13
    elif call.data == "lab_05_variant_13":
        download_lab("05", "13", "1tZaRyFwiuDF4i-T7bK8ZW85TWlxQd7TB", call.from_user.id)
    # Lab 05/Variant 14
    elif call.data == "lab_05_variant_14":
        download_lab("05", "14", "1Sp55XxATlq267_sjUD0ksqvaL9OXDN_Q", call.from_user.id)
    # Lab 05/Variant 15
    elif call.data == "lab_05_variant_15":
        download_lab("05", "15", "1HIXADEbaA-iQB09L3wXcfArR7ENdhTi5", call.from_user.id)
    # Lab 05/Variant 16
    elif call.data == "lab_05_variant_16":
        download_lab("05", "16", "1s4tz3jmTujTsoFESJosEsKbb4DLrcZVE", call.from_user.id)
    # Lab 06
    # Lab 06/Variant 01
    elif call.data == "lab_06_variant_01":
        download_lab("06", "01", "14KuONQjrXgvgAqjuaPkl1vfK1hmsVB2r", call.from_user.id)
    # Lab 06/Variant 02
    elif call.data == "lab_06_variant_02":
        download_lab("06", "02", "1MnBaCTC-zhATKcsn24mP2Ix7hCIOXH6q", call.from_user.id)
    # Lab 06/Variant 03
    elif call.data == "lab_06_variant_03":
        download_lab("06", "03", "1jynJp0seyZwEYxzbRIAxe_8FNlq0jwr3", call.from_user.id)
    # Lab 06/Variant 04
    elif call.data == "lab_06_variant_04":
        download_lab("06", "04", "1vrXZYJSL9l5trnz8xEaWv-T2W461_reP", call.from_user.id)
    # Lab 06/Variant 05
    elif call.data == "lab_06_variant_05":
        download_lab("06", "05", "1sy5pLq5JGK9cyozB0QUOaXku7C_yw_nb", call.from_user.id)
    # Lab 06/Variant 06
    elif call.data == "lab_06_variant_06":
        download_lab("06", "06", "1u07xJhnfiR2mVWKYfUL5GYUzzAIoGsTa", call.from_user.id)
    # Lab 06/Variant 07
    elif call.data == "lab_06_variant_07":
        download_lab("06", "07", "1p-t7uXw68mU9k9q3UIWlHeroUbbURJGW", call.from_user.id)
    # Lab 06/Variant 08
    elif call.data == "lab_06_variant_08":
        download_lab("06", "08", "1RZqcI1KOzc459_pWiCQoTjsz1UTCUO_u", call.from_user.id)

################################################################################################################
################################################################################################################
################################################################################################################

print(bot.get_me())

def log(message, answer):
    print("\n ------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3})" . format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
    print(answer)

bot.polling(none_stop = True, interval = 0)
