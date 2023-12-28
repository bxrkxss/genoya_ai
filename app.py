from telegram.ext import Application, CommandHandler, MessageHandler, filters
import httpx

API_KEY = 'AIzaSyB-WcIhGE44RKrrDxrepTMf3vB-BiAzCko'
TELEGRAM_BOT_TOKEN = '6905096531:AAHBnKWydimQzAeYdc1l4Ha1m3CsZqQ104Y'

async def start(update, context):
    await update.message.reply_text('Привет! Напиши мне что-нибудь, и я использую API Google.')

async def help_command(update, context):
    await update.message.reply_text('Отправьте мне текст, и я обработаю его с помощью API Google.')

async def handle_message(update, context):
    user_message = update.message.text
    url = 'https://us-central1-aiplatform.googleapis.com/v1/predictions'
    payload = {'key': API_KEY, 'q': user_message}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=payload)
    if response.status_code == 200:
        await update.message.reply_text(response.json())
    else:
        await update.message.reply_text('Произошла ошибка при обработке вашего сообщения.')

application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
application.run_polling()
