from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = '8076030403:AAGJXblqM3T48y-Zc69KjRMnirs7zMthhd8'

main_menu = ReplyKeyboardMarkup(
    keyboard=[['💻 Услуги', '🧠 Обо мне'], ['📩 Связаться']],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я Fixteen 🤖\nГотов помочь с компьютерами, текстами и чисткой телефонов.\nВыбери опцию ниже:",
        reply_markup=main_menu
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == '💻 Услуги':
        await update.message.reply_text(
            "🔧 Услуги Fixteen:\n\n"
            "🖥 Установка Windows — договорная\n"
            "🧼 Чистка ПК и телефонов — договорная\n"
            "✍️ Копирайтинг текста — договорная"
        )
    elif text == '🧠 Обо мне':
        await update.message.reply_text(
            "Здравствуйте! Меня зовут Иль
