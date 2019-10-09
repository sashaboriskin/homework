import telebot
telebot.apihelper.proxy = {'https': 'socks5://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token="982351184:AAFdbXkPxQTN8Y3Ebs_2osqOEQASK1W27mA")

@bot.message_handler(commands=['start'])
def start(message):
    # кто нам написал? узнаем id чата!
    chat_id = message.chat.id
    # отправляем приветствие
    answer = bot.send_message(chat_id, "Добро пожаловать в квест. Хочешь получить 10000000$? Тогда тебе нужно победить 3 монстров, а в конце сможешь забрать свой приз. Боссы будут нелегкие и тебе придется подбирать оружие для каждого из них. ")
    # в ответ на приветствие просим вызвать функцию point1
    bot.register_next_step_handler(answer, firstb)


def firstb(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Первый босс. Босса нужно побеждать в ближнем бою. Какое оружие ты выберешь?")
    t = """Вот твой арсенал: 
    1) Меч
    2) Лук
    3) Копьё
        """
    bot.send_message(chat_id, t)
    text = message.text
    if text == 1:
        pass
        #answer = bot.send_message(chat_id, "Правильно, ты выбрал правильное оружие. Проходи дальше")
        #bot.register_next_step_handler(answer, secondb)
    else:
        answer = bot.send_message(chat_id, "ты умер. Начинай заново")
        bot.register_next_step_handler(answer, firstb)



bot.polling(none_stop=True)
