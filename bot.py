import os
import random
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

jokes = [
    "مرة واحد غبي راح للسوق، سألوه تريد شي؟ كال لا بس جاي اتفرج على الاسعار وهي تصعد 😂",
    "ليش الكمبيوتر راح للدكتور؟ لان بيه فايروس 😂",
    "واحد كال لصاحبه: ليش لابس نظارة بالليل؟ كاله: حتى اشوف احلامي بوضوح 😂",
    "مرة مدرس سأل طالب: شنو عاصمة العراق؟ كاله: بغداد. كاله: عفية، وشنو عاصمة فرنسا؟ كاله: هم بغداد، بس بالفرنسي 😂",
    "ليش الدجاجة عبرت الشارع؟ حتى توصل للجهة الثانية 😂",
    "واحد راح للصيدلية كال: عندك دوا للنسيان؟ كاله: اي، بس نسيت وين حطيته 😂"
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "هلا بيك! دزلي اي شي وانا انطيك نكتة 😂")

@bot.message_handler(func=lambda m: True)
def send_joke(message):
    bot.reply_to(message, random.choice(jokes))

bot.infinity_polling()
