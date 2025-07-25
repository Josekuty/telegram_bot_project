from app import app
from telegram_bot import run_bot
from flask import Flask
from threading import Thread
import asyncio
import nest_asyncio

nest_asyncio.apply()

def run_flask():
    app.run(host='0.0.0.0', port=10000)

def run_telegram():
    asyncio.run(run_bot())

if __name__ == "__main__":
    Thread(target=run_flask).start()
    run_telegram()
