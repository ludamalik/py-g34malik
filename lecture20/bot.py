import telebot
from telebot import types

TOKEN = '6453525916:AAFR108xfUYY_KkcE044pTDUp-n3JoFeONc'
bot = telebot.TeleBot(TOKEN)

events = {
    'today': [],
    'important': [],
    'secondary': []
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your reminder bot. Use /help to get list of commands.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Available commands:
    /add - Add new event
    /today - Show events for today
    /important - Show important events
    /secondary - Show secondary events
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['add'])
def add_event(message):
    msg = bot.reply_to(message, "Enter event's name:")
    bot.register_next_step_handler(msg, process_event_name)

def process_event_name(message):
    event_name = message.text
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn1 = types.KeyboardButton('Today')
    itembtn2 = types.KeyboardButton('Important')
    itembtn3 = types.KeyboardButton('Secondary')
    markup.add(itembtn1, itembtn2, itembtn3)
    msg = bot.reply_to(message, "Choose the category:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_category, event_name)

def process_category(message, event_name):
    category = message.text.lower()
    if category == 'today':
        events['today'].append(event_name)
    elif category == 'important':
        events['important'].append(event_name)
    elif category == 'secondary':
        events['secondary'].append(event_name)
    else:
        bot.reply_to(message, "Wrong category. Try again.")
        return

    bot.reply_to(message, f"Event '{event_name}' added to the category '{category}'.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=['today'])
def show_today_events(message):
    if events['today']:
        event_list = "\n".join(events['today'])
        bot.reply_to(message, f"Events for today:\n{event_list}")
    else:
        bot.reply_to(message, "No events for today.")

@bot.message_handler(commands=['important'])
def show_important_events(message):
    if events['important']:
        event_list = "\n".join(events['important'])
        bot.reply_to(message, f"Important events:\n{event_list}")
    else:
        bot.reply_to(message, "No important events.")

@bot.message_handler(commands=['secondary'])
def show_secondary_events(message):
    if events['secondary']:
        event_list = "\n".join(events['secondary'])
        bot.reply_to(message, f"Secondary events:\n{event_list}")
    else:
        bot.reply_to(message, "No secondary events.")

bot.polling()