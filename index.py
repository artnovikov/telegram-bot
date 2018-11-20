import telebot
import os
import urllib.request as urllib2

bot = telebot.TeleBot("746612461:AAHHnGHEFbyBzIWnte6rG40vZWFmqmnb1Pg")

################################################################################################################
################################################################################################################
################################################################################################################

def download_lab(number_of_lab, number_of_variant, google_link, user_id):
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
    user_markup.row("Lab 01")
    user_markup.row("Lab 02")
    user_markup.row("Lab 05")
    bot.send_message(message.from_user.id, "Hello, we're glad to c u. Please select lab number.", reply_markup = user_markup)

################################################################################################################
################################################################################################################
################################################################################################################

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text == "Exit":
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Thank you for using our bot...", reply_markup = hide_markup)
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
        download_lab("05", "01", "1JAr8CQ8HNjJDsZWrTQB0TptoaTqOFfMM", call.from_user.id)
    # Lab 05/Variant 02
    elif call.data == "lab_05_variant_02":
        download_lab("05", "02", "1UEnl_MPTjyTCjQUYehkdB9nQAFd2RPfU", call.from_user.id)
    # Lab 05/Variant 03
    elif call.data == "lab_05_variant_03":
        download_lab("05", "03", "1CiFB6zSC2IuBlBYkamzBRhY5kpl3d-5h", call.from_user.id)
    # Lab 05/Variant 04
    elif call.data == "lab_05_variant_04":
        download_lab("05", "04", "1bSb4Yl4QXcOTfZvDFQqItK4fEfAh54O3", call.from_user.id)
    # Lab 05/Variant 05
    elif call.data == "lab_05_variant_05":
        download_lab("05", "05", "18U5kHhOStZnIHDLRwY2EY3ZcoYnH_Xnn", call.from_user.id)
    # Lab 05/Variant 06
    elif call.data == "lab_05_variant_06":
        download_lab("05", "06", "18-3i6UIcwqwigABV1rR6JgGjKcF1WID2", call.from_user.id)
    # Lab 05/Variant 07
    elif call.data == "lab_05_variant_07":
        download_lab("05", "07", "1q16_sAYtl2Uo2Ri9ip-ZMyGP8UsrTfwC", call.from_user.id)
    # Lab 05/Variant 08
    elif call.data == "lab_05_variant_08":
        download_lab("05", "08", "17reDwicvDvtg3MEuTKAR9uH0hFGbcWgi", call.from_user.id)
    # Lab 05/Variant 09
    elif call.data == "lab_05_variant_09":
        download_lab("05", "09", "1IWbQ0M8j87B-Php3mCqBzJvxSBwWOV5_", call.from_user.id)
    # Lab 05/Variant 10
    elif call.data == "lab_05_variant_10":
        download_lab("05", "10", "1QCaKYCYZauq6rds5UELGkPCr-NYarl99", call.from_user.id)
    # Lab 05/Variant 11
    elif call.data == "lab_05_variant_11":
        download_lab("05", "11", "18igeT2RDORWdnAYQ0TsksQ3OdzBGbxbC", call.from_user.id)
    # Lab 05/Variant 12
    elif call.data == "lab_05_variant_12":
        download_lab("05", "12", "1tID3zIqiKTj14oxiDmFAdqoKmS7cH9l1", call.from_user.id)
    # Lab 05/Variant 13
    elif call.data == "lab_05_variant_13":
        download_lab("05", "13", "1giBkcV5mcFyQgxqV62pndJMFlVa2gF_R", call.from_user.id)
    # Lab 05/Variant 14
    elif call.data == "lab_05_variant_14":
        download_lab("05", "14", "1tZHwrItCcrH603GyY_ofg4AH0kDz5oOW", call.from_user.id)
    # Lab 05/Variant 15
    elif call.data == "lab_05_variant_15":
        download_lab("05", "15", "1tugCSMo5mcmCL_kR9gK3-4ihNwznMydJ", call.from_user.id)
    # Lab 05/Variant 16
    elif call.data == "lab_05_variant_16":
        download_lab("05", "16", "1s31fgzPNlfypssdEPOngWrOLYAOOCuxJ", call.from_user.id)

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
