#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '1613607846:AAGBJh81RIp4-JV4qya-apFmBrfcZoz7jMQ'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ciao! sono Netassistent_bot!/""")
Dimmi di cosa hai bisogno!

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
if message.text=='/info'
    bot.reply_to(message,'Per essere chiaro e coinciso, noi ci occupiamo di farti avere il tuo account Netflix in sicurezza! Con soli 5€ al mese, avrai il tuo account e potrai disdire quando vuoi! Non c’è niente da perdere, appunto perchè è un metodo già testato molte volte! E se nel caso ci fossero problemi, riavrai indietro il 100% dei tuoi soldi!')
elif message.text=='/buyacc'
    bot.reply_to(message,'Comprare un account è semplice e, come già detto nelle info, costa solo 5€ al mese! Per averlo ti basterá contattare il Proprietario @krayway_121 che ti fornirà un link PayPal, dove potrai pagare in sicurezza! Al termine del pagamento avrai il tuo account già pronto per essere utilizzato!!!')
elif message.text=='/help'
    bot.reply_to(message,'se hai problemi con il tuo account, non avere paura! Basta scrivere il problema al nostro amministratore @Paologreco17 che appena possibile, risponderà proponendoti una soluzione, oppure un rimborso!')

bot.polling()
