from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import os

BOT_TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot!")

async def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()
