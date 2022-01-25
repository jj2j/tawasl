import telebot
from telebot import types
import requests
import  random, time, user_agent,requests
from user_agent import generate_user_agent
ID = '1818416834'

token = '1771143161:AAHmMU5t0kZF50Rjl8BtOdSQgWOaHmLaZgY'
bot = telebot.TeleBot(token)
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
@bot.message_handler(commands=['hunt'])
