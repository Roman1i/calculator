import telebot.types
from telebot import TeleBot
import calc
import loger


bot = TeleBot('5455320732:AAEFef3PRd78hkrSdFXb_0VGX0TRtgI7L34')


@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='/help - список команд\n'
                                                    '/calculation - калькулятор\n'
                                                    '/log - загрузка логов\n'
                                                    '/clearlog - очистка логов\n')


@bot.message_handler(commands=['calculation'])
def calculation_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Введите выражение')
    bot.register_next_step_handler(callback=calculation, message=msg)


def calculation(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=calc.calculation(msg.text))


@bot.message_handler(commands=['log'])
def log(msg: telebot.types.Message):
    bot.send_document(chat_id=msg.from_user.id, document=open('log.log', 'rb'))
    loger.log_upload()


@bot.message_handler(commands=['clearlog'])
def clear_log(msg: telebot.types.Message):
    loger.clear()


bot.polling()
