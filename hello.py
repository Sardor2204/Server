from telebot import *

bot = telebot.TeleBot("2101941831:AAFg1_2b3v44YJZU0Ckg-RjtxUx7LS8Nj4k")

@bot.message_handler(commands=["start"])
def start_bot(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Это бот для админов класса 7В\n\n\n"
                                          "Чтобы написать домашную работу напишите /homework")

@bot.message_handler(commands=["homework"])
def homework_bot(message):
    if message.text == "/homework":
        msg = bot.send_message(message.chat.id, "Напишите домашную работу\n"
                                                "Например\n\n"
                                                "Алгебра стр 45 номера 135-140\n"
                                                "Русский язык упр 197\n"
                                                "История читать 56-60 стр\n"
                                                "Геометрия стр 45 1-10")

        bot.register_next_step_handler(msg, homework)

def homework(message):
    i = message.text

    k = open('homework.txt', 'w')

    k.write(i)

    bot.send_message(message.chat.id, "Спасибо за внимание")

bot.polling(none_stop=True)