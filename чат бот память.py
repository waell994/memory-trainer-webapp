import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# 🔐 Вставь свой токен от BotFather
TOKEN = 'YOUR_BOT_TOKEN_HERE'

bot = telebot.TeleBot("7637354916:AAEDRWfetIsiStgfgCEKJnUlSwDWIcyoMUw")

# 📲 Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    
    # 🔗 Вставь сюда свою ссылку на Web App (например, на Vercel, GitHub Pages)
    web_app_url = 'https://waell994.github.io/memory-trainer-webapp/'
    
    web_app_button = KeyboardButton(
        text="🧠 Открыть мини-приложение",
        web_app=WebAppInfo(url=web_app_url)
    )
    
    markup.add(web_app_button)

    bot.send_message(message.chat.id, "Привет! Нажми кнопку ниже, чтобы начать тренировку памяти 🧠", reply_markup=markup)

# 📥 Обработка данных, полученных из Web App
@bot.message_handler(content_types="web_app_data")
def handle_web_app_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"📊 Получены данные из Web App: {data}")

# 🚀 Запуск бота
bot.infinity_polling()
