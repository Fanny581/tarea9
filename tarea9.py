import telebot # importamos la libreria de telebot

# token = os.getenv['TOKEN']
bot = telebot.TeleBot('1904520783:AAHMvs_kt-3Rk1unjMYOFMYZb757piv9WDY') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['info','hola']) #definimos el comando
def hola(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id,  "Envia 1 o Metros para ver formula Metros a Centímetros \n Envia 2 o Kilómetros para ver formula Kilómetros a Metros \n Envia 3 o Millas para ver formula Millas a Kilómetros \n Envia 4 o Pie para ver formula Pie a Pulgadas \n ")
    print("Mandaron info")

@bot.message_handler(commands=["metros","metro"]) 
def Metros(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "1 metro equivale a 100 centímetros (1m = 100cm)")
    print("Mandaron metro , metros")

@bot.message_handler(commands=["kilometros ","kilometros"])
def Kilómetros(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "1 kilómetro equivale a 1000 metros (1km = 1000m)")
    print("Mandaron kilometros, kilometros")

@bot.message_handler(commands=["millas ","milla"])
def Millas(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "1 milla es igual a 1.609 kilometros")
    print("Mandaron millas , milla")

@bot.message_handler(commands=["pie ","pie"])
def Pie(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "1 pie = 12.00 pulgada")
    print("Mandaron pie")

bot.polling()