import telebot
telebot.apihelper.proxy = {'https': 'socks5://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token="982351184:AAFdbXkPxQTN8Y3Ebs_2osqOEQASK1W27mA")

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    answer = bot.send_message(chat_id, "Добро пожаловать в квест. Хочешь получить 10000000$? Тогда тебе нужно победить 3 монстров, а в конце сможешь забрать свой приз. Боссы будут нелегкие и тебе придется подбирать оружие для каждого из них. ")
    bot.send_message(chat_id, "Первый босс. Босса нужно побеждать в ближнем бою. Какое оружие ты выберешь?")
    t = """Вот твой арсенал: 
        1) Меч
        2) Лук
        3) Копьё
            """
    m = bot.send_message(chat_id, t)
    bot.register_next_step_handler(m, first_answer)


def first_answer(message):
    text = message.text
    chat_id = message.chat.id
    if text == "1":
        answer = bot.send_message(chat_id, "Правильно, ты выбрал правильное оружие. Проходи дальше")
        answer = bot.send_message(chat_id,
                         "Второй босс. Босса нужно побеждать на расстояние, но и не из лука. Какое оружие ты выберешь?")
        t = """Вот твой арсенал: 
            1) Меч
            2) Лук
            3) Копьё
                """
        answer = bot.send_message(chat_id,t)
        bot.register_next_step_handler(answer, secondb)
    else:
        bot.send_message(chat_id, "ты умер")
        start(message)

def secondb(message):
    chat_id = message.chat.id
    text = message.text
    if text == "3":
        bot.send_message(chat_id, "Правильно, ты выбрал правильное оружие. Проходи дальше")
        answer = bot.send_message(chat_id, "Третий босс. Босса нужно побеждать на расстоянии, но не их лука. Какое оружие ты выберешь?")
        t = """Вот твой арсенал: 
            1) Меч
            2) Лук
            3) Копьё
                """

        bot.send_message(chat_id, t)

        bot.register_next_step_handler(answer, thirdb)
    else:
        bot.send_message(chat_id, "ты умер")
        start(message)

def thirdb(message):
    chat_id = message.chat.id
    text = message.text
    if text == "2":
        answer = bot.send_message(chat_id, "ты победил")
    else:
        answer = bot.send_message(chat_id, "ты умер. Начинай заново")
        bot.register_next_step_handler(answer, start)


bot.polling(none_stop=True)
