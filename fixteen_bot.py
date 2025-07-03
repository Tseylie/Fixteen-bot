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
            "Меня зовут Илья, мне 17. Я эрудирован, шарю в компах, хорошо играю в шахматы и футбол.\n"
            "Fixteen — это мой способ помогать людям и зарабатывать своими знаниями."
        )
    elif text == '📩 Связаться':
        await update.message.reply_text("Свяжись со мной: @tseylie\nРаботаю ежедневно с 11:00 до 19:00.")
    else:
        await update.message.reply_text("Выбери кнопку ниже 👇", reply_markup=main_menu)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.run_polling()

if __name__ == '__main__':
    main()
