from telebot import types
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def choice_buttons():

    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    git_hub = types.KeyboardButton('Hello')
    discord = types.KeyboardButton('Bye')
    help_bar = types.KeyboardButton('help')
    button.add(git_hub, discord, help_bar)

    return button


def links_commands():
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    link1 = types.KeyboardButton('Github')
    link2 = types.KeyboardButton('Channel')
    link3 = types.KeyboardButton('Discord')
    button.add(link1, link2, link3)

    return button

def help_commands():
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    help_com1 = types.KeyboardButton('Github')
    help_com2 = types.KeyboardButton('Channel')
    help_com3 = types.KeyboardButton('Discord')
    back_bar = types.KeyboardButton('Назад')
    button.add(help_com1, help_com2, help_com3, back_bar)
    return button

# def inlinelanguage():
#     button = InlineKeyboardMarkup(row_width=2)
#     rus = InlineKeyboardButton('Русский язык', callback_data='rus')
#     uzb = InlineKeyboardButton("O'zbek tili", callback_data='uzb')
#     button.row(rus, uzb)
#
#     return button
# def back():
#     button = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     back_bar = types.KeyboardButton('Назад')
#     pass








