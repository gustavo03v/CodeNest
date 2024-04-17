from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá, este é o seu bot do Telegram!')

def report_spam(update: Update, context: CallbackContext) -> None:
    # Aqui você pode adicionar a lógica para denunciar spam
    update.message.reply_text('Spam reportado!')

def main() -> None:
    updater = Updater("7032025783:AAEy5ImUkEj9wW9dopyZeZbl_EGBREBvGcQ", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("reportspam", report_spam))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
