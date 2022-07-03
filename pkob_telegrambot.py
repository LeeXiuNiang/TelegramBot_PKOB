import django
import os
from telegram import Update
import bot as b

os.environ['DJANGO_SETTINGS_MODULE'] = 'PKOB.settings'
TOKEN = os.getenv('TOKEN')
django.setup()

from telegram.ext import *
from App_Soc.models import *
import re

API_KEY = '5053154519:AAGDS1z7rbAZtFbWp_0j38esPsFlwcN7zhI'
print('Bot started')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        f"WELCOME to our PKOB bot~ :)\nYou may refer to the menu to proceed.")

def check(update, context):
    update.message.reply_text(f"Hi, {update['message']['chat']['first_name']}.\nPlease enter your IC Number and Phone Number to get your information.\nExample: 990112108999 0123456789")

def visit(update, context):
    update.message.reply_text(
        f"Our website: https://pkob272033.herokuapp.com/")

def isValidIC(ic_no):
    regex = "(([[0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01]))([0-9]{2})([0-9]{4})";
    p = re.compile(regex)
    if (ic_no == ''):
        return False;
    m = re.match(p, ic_no)
    if m is None:
        return False
    else:
        return True

def isValidPhone(phone_no):
    regex = "[0-9]";
    p = re.compile(regex)
    if (phone_no == ''):
        return False;
    m = re.match(p, phone_no)
    if m is None:
        return False
    else:
        return True

def handle_message(update, context):
    text = str(update.message.text).lower()
    bots = b.sample_responses(text)
    update.message.reply_text(bots)



if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('check', check))
    dp.add_handler(CommandHandler('visit', visit))
    dp.add_handler(MessageHandler(Filters.text, handle_message))


    updater.start_polling(1.0)
    updater.idle()