import os
import telebot
from dotenv import load_dotenv
import metro as m
from telebot import types

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['incio', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Aoba, como vai?")


@bot.message_handler(commands=['trem', 'metro'])
def send_status(message):
    bot.reply_to(message, m.montar_txt())

def enviar_teclado(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)  # Crie um teclado com 2 colunas

    # Crie botões e adicione-os ao teclado
    btn1 = types.KeyboardButton('Trens/Metro')
    btn2 = types.KeyboardButton('Onibus')

    markup.add(btn1, btn2)  # Adicione os botões ao teclado

    bot.send_message(message.chat.id, "Bem Vindo ao MetroBot, escolha uma opção:", reply_markup=markup)

# Manipulador de comando para mostrar o teclado personalizado
@bot.message_handler(commands=['menu'])
def mostrar_teclado(message):
    enviar_teclado(message)

# Manipulador de mensagens de texto
@bot.message_handler(func=lambda message: True)
def responder_mensagem(message):
    if message.text == 'Trens/Metro':
        bot.reply_to(message, m.montar_txt())
    elif message.text == 'b':
        bot.reply_to(message, "Você escolheu o Botão 2.")
    else:
        bot.reply_to(message, "Não entendi sua escolha. Use os botões abaixo:")

bot.infinity_polling()