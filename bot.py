from telebot import types
import telebot
import configure

bot = telebot.TeleBot(configure.config['token'])


@bot.message_handler(commands=['start', 'info'])
def get_city_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_city = types.InlineKeyboardButton(text='Указать город', callback_data='city')
    item_discover = types.InlineKeyboardButton(text='Узнать погоду', callback_data='discover')

    markup_inline.add(item_city, item_discover)
    bot.send_message(message.chat.id, 'Что желаете узнать?',
                     reply_markup=markup_inline
                     )


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'city':
        bot.send_message(call.message.chat.id, 'Укажите желаемый город')
    if call.data == 'discover':
        pass


bot.polling(none_stop=True, interval=0)
