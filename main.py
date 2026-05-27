import telebot
from telebot import types
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "Bot is Alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

API_TOKEN = '8653406085:AAEXACbOB6vn4iwft8QhnLlgznvLGTYmBBI' 

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("🛍️ شراء رقم وهمي", callback_data="buy_num")
    btn2 = types.InlineKeyboardButton("💰 شحن الرصيد", callback_data="deposit")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f"أهلاً بك في بوت الأرقام التلقائي 🤖✨\n\nالبوت شغال دائمي 24 ساعة لحسابك!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "buy_num":
        bot.send_message(call.message.chat.id, "⚠️ عذراً، رصيدك 0$. اشحن حسابك أولاً.")
    elif call.data == "deposit":
        bot.send_message(call.message.chat.id, "💳 للشحن وتفعيل الحساب تواصل مع الإدارة.")

keep_alive()
bot.polling(none_stop=True)
