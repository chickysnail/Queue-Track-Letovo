from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update


def help(update: Update, context: CallbackContext):
    help_text = 'There will be no help for you, figure it out yourself'
    update.message.reply_text(help_text)

def queue(update: Update, context: CallbackContext):
    pass

TOKEN = "2082795270:AAHLwx1DaetOsPu3u4O8iOWa6fF3ysazL8E"

def main():
    updater: Updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # get help
    help_handler = CommandHandler("help", help)
    dispatcher.add_handler(help_handler)

    # get queue
    get_queue_handler = CommandHandler("queue", queue)
    dispatcher.add_handler(get_queue_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()