import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import requests

# Environment Variables-ից tokens-ները կարդալ
TELEGRAM_BOT_TOKEN = os.environ.get('7796637185:AAF8_XLO7rfi4xuwgmBXv4KOjRo4CWKDtVI')
OPENAI_API_KEY = os.environ.get('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')

# Logging կարգավորել
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Բոլոր հաղորդագրությունները մշակել"""
    if update.message.voice:
        # Ձայնային հաղորդագրություն
        await update.message.reply_text("🎧 Ձայնային հաղորդագրություն ստացվեց!")
        
        voice_file = update.message.voice
        duration = voice_file.duration
        file_size = voice_file.file_size
        
        response = f"📊 Ձայնի տվյալներ:\n"
        response += f"⏱ Տևողություն: {duration} վայրկյան\n"
        response += f"📦 Չափ: {file_size} բայթ\n"
        response += f"🆔 File ID: {voice_file.file_id[:20]}..."
        
        await update.message.reply_text(response)
    else:
        # Տեքստային հաղորդագրություն
        await update.message.reply_text("📝 Ես ձայնային հաղորդագրություններ եմ մշակում: Խնդրում եմ ուղարկեք ձայնագրություն:")

def main():
    """Բոտը գործարկել"""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("❌ TELEGRAM_BOT_TOKEN բացակայում է!")
        return
    
    # Application ստեղծել
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Handler-ներ ավելացնել
    application.add_handler(MessageHandler(filters.ALL, handle_message))
    
    # Բոտը գործարկել
    logger.info("🤖 Բոտը գործարկվեց!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()