import telebot
from aarrr import password_generate
from emodji import gen_emodji
from telebot import types
import time
bot = telebot.TeleBot("TOKEN")



bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("pass", "сгенерируй крутой пароль и напиши сколько цифр нужно"),
        telebot.types.BotCommand("emodji", "Супер мега смешное эмодзи класс"),
        telebot.types.BotCommand("start", "Сообщение от гениального разработчика Артёма супер легенды")
    ],
    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
)

# check command
cmd = bot.get_my_commands(scope=None, language_code=None)
print([c.to_json() for c in cmd])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я не умею работать в питоне:)")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Лови эмоджи': {emodji}")

@bot.message_handler(commands=['pass'])
def send_password(message):
    pass_length = message.text
    pass_length = int (pass_length.split()[1])
    passwordsuper = password_generate(int(pass_length))
    bot.reply_to(message, passwordsuper)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
