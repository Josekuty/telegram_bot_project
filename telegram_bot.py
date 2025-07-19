from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update
import os
import subprocess

BOT_TOKEN = os.getenv("TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Send me an Instagram reel link to download it.")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Available Commands:\n"
        "/start - Start the bot\n"
        "/help - Show help message\n"
        "/info - Show bot information\n"
        "\nYou can also just send an Instagram reel link directly."
    )

# /info command
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ Bot Creator: Josekuty\n"
        "📽️ Purpose: Instagram Reel Downloader\n"
        "🗓️ Date Created: 25 March 2025"
    )

# Respond to "hi", "hello", etc.
async def greetings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text in ["hi", "hello", "hey", "hai"]:
        await update.message.reply_text("Hi there! 👋 Send me an Instagram reel link to download.")
    else:
        await download_reel(update, context)

# Reel download handler
async def download_reel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    if "instagram.com/reel/" not in url:
        return  # Not a reel, ignore

    await update.message.reply_text("⏬ Downloading reel... Please wait.")

    try:
        filename = "reel.mp4"
        subprocess.run(['yt-dlp','--cookies', 'cookies.txt', '-o', filename, url], check=True)

        if os.path.exists(filename):
            with open(filename, 'rb') as video:
                await update.message.reply_video(video)
            os.remove(filename)
        else:
            await update.message.reply_text("❌ Failed to download the reel.")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")

# Run the bot
async def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, greetings))

    print("🤖 Telegram bot is running...")
    await app.run_polling()
