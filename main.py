import telebot
import buttons

bot = telebot.TeleBot('6641621950:AAFkPVGCKuME3CUBbELQH6zWjUOQPFMWL8I')
#a = int(input())

@bot.message_handler(commands=['start', 'help'])
def start_bot(message):
    print(message)
    bot.send_message(message.from_user.id, 'Привет!', reply_markup=buttons.choice_buttons())
    bot.send_message(message.from_user.id, 'как твои дела? если не знаешь что делать то жми на кнопки')
    #bot.register_next_step_handler()
    # for i in range(1, 100 + 1):
    #     bot.send_message(5264469692, f'Гондон бля Гарри Поттер')
    #bot.reply_to(message, 'https://discord.gg/AkQcPPdN')





@bot.message_handler(content_types=['text'])
def start_mybot_text(message):

    if message.text.lower() == 'hello':
        bot.send_message(message.from_user.id, 'очень приятно, я бот')
        # bot.send_message(message.from_user.id, 'выберите язык!, tilni tanlang!', reply_markup=buttons.inlinelanguage())

    elif message.text.lower() == 'links':
        bot.send_message(message.from_user.id, 'дискорд => discord')
        bot.send_message(message.from_user.id, 'мой гит => github')
        bot.send_message(message.from_user.id, 'мой ютуб => сhannel')
        bot.send_message(message.from_user.id, 'стримы => twitch')

    elif message.text.lower() == 'help':
        bot.send_message(message.from_user.id, 'вот тебе помощь, все команды!', reply_markup=buttons.help_commands())

    elif message.text.lower() == 'назад':
        bot.send_message(message.from_user.id, 'возвращаю!', reply_markup=buttons.choice_buttons())


    elif message.text.lower() == 'channel':
        bot.reply_to(message, 'https://www.youtube.com/@timbusien')

    elif message.text.lower() == 'discord':
        bot.reply_to(message, 'https://discord.gg/AkQcPPdN')

    elif message.text.lower() == 'github':
        bot.reply_to(message, 'https://github.com/Timbusien')

    elif message.text.lower() == 'twitch':
        bot.reply_to(message, 'https://www.twitch.tv/timbusien')

    elif message.text.lower() == 'bye':
        bot.send_message(message.from_user.id, 'раз не надо так не надо, нехуй было заходить на бота')
        bot.send_message(message.from_user.id, 'кстати спасибо за данные которые ты мне любезно придоставил')

    else:
        bot.send_message(message.from_user.id, 'по русски говори эээ!!')


# @bot.callback_query_handler(lambda call: call.data in ['rus', 'uzb'])
# def change_lan(call):
#     user_id = call.message.chat.id
#     if call.data =='rus':
#         bot.send_message(user_id, 'язык выбран русский')
#         bot.send_message(user_id, 'для следующей операции нажмите на команды', reply_markup=buttons.links_commands())
#     elif call.data == 'uzb':
#         bot.send_message(user_id, "o'zbek tili tanlangan")
#         bot.send_message(user_id, 'keyingi boshqaruv uchun comandalarni ishlating', reply_markup=buttons.links_commands())



bot.infinity_polling()






