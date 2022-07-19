import wikipedia    # TELEGRAM WIKI_BOT ADDRESS  @ranglevangle_bot
import telebot


bot = telebot.TeleBot('')   #  <---------  YOUR TOKEN

@bot.message_handler(commands=['start'])
def start(message):
    sending_mess = f"<b> HELLO {message.from_user.first_name} {message.from_user.last_name} !</b>\n Enter a word to start searching."
    bot.send_message(message.chat.id, sending_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    word = message.text.strip().lower()
    try:
        final_message = wikipedia.summary(word)
    except wikipedia.exceptions.PageError:
        final_message = ""

    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)