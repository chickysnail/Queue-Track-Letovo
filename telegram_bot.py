import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import getPhoto, imageConverter

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\!')


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def authors(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("@FrostDeath, @mikhailandri, @chickysnail")


def request_queue(update: Update, context: CallbackContext) -> None:
    photo = getPhoto.get(last=-1)
    update.message.reply_photo(photo)


def main() -> None:
    updater = Updater("2082795270:AAHLwx1DaetOsPu3u4O8iOWa6fF3ysazL8E")  # Tocken of Bot

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("queue", request_queue))
    dispatcher.add_handler(CommandHandler("authors", authors))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()