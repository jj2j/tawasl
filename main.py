from flask import Flask
import logging
import os
import config
import telebot
from telebot import types
import requests
ID = '1818416834'
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
###start###
start_msg = '''
𝐰𝐞𝐥𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐢𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐡𝐮𝐜𝐤 𝐚𝐜𝐜𝐨𝐮𝐧𝐭𝐬 𝐛𝐨𝐭  ᵈᵉᵛ @BQBXB
 ______________________
 
 𖢿 - ˢᵗᵃʳᵗ ʰᵘᶰᵗ - - > /hunt  <- - 
______________________ 
'''
@bot.message_handler(commands=['start'])
def hello(message):
	photo = 'https://t.me/bqbzb/3'
	bot.send_photo(message.chat.id, photo, start_msg)
	voice = 'https://t.me/bqbzb/2'
	bot.send_voice(message.chat.id, voice, '@BQBXB')
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://tawasl.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
