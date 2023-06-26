import logging
import os
import asyncio
import datetime
from telegram.ext import JobQueue, CommandHandler, CallbackQueryHandler

## mysql module
#python -m pip install mysql-connector-python
import mysql.connector
from mysql.connector import errorcode

from datetime import datetime, timedelta
from difflib import get_close_matches

import telegram  # pip install python-telegram-bot
from telegram import __version__ as TG_VER
try:
  from telegram import __version_info__
except ImportError:
  __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
  raise RuntimeError(
    f"This example is not compatible with your current PTB version {TG_VER}. To view the "
    f"{TG_VER} version of this example, "
    f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html")
from telegram.constants import ParseMode
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler

from telegram import (
  ReplyKeyboardMarkup,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
)
from telegram.ext import (
  Updater,
  ApplicationBuilder,
  CommandHandler,
  MessageHandler,
  ConversationHandler,
  CallbackQueryHandler,
  filters,
)
## Calendar module
import calendar

import random

# Use flask
from flask import Flask
from threading import Thread

# Enable logging for debugging purposes
logging.basicConfig(
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Telegram Bot token
TOKEN = os.getenv("BOT_TOKEN")

# keep alive script for uptimerobot

#define flask app
app = Flask('')
#create route for home page

@app.route('/')
def main():
	return "server online!"
#Run our flask app in a thread so that the bot and website can run simultaneously.

def run():
	app.run(host="0.0.0.0", port=8080)
  
def keep_alive():
	server = Thread(target=run)
	server.start()

keep_alive()



# Initialize the database connection
# For dbms connection
try:
  conn = mysql.connector.connect(
    host=os.getenv("HOST_SITE"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
  )
  cursor = conn.cursor()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    logger.error("Access denied error: Invalid database credentials")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    logger.error("Bad database error: Database does not exist")
  else:
    logger.error(err)
  exit(1)

# Initialize the list to store meal entries
meal_entries = []

# Initialise reminder list to store reminder entries
reminders = []

# Conversation states
ISCURRENT, DATE, TIME, NAME, CREATE_MEAL_NAME,INSERT_MEAL_ENTRY = range(6)

CATEGORY, HALAL = range(2)

async def start(update, context):
  """Handler for the /start command."""
  # Clear any existing conversation data
  context.user_data.clear()
  user = update.effective_user
  await context.bot.send_message(
    chat_id=update.effective_chat.id,
    text=
    f"Welcome {user.mention_markdown_v2()}\!\nWhat can I do for you today?",
    parse_mode=ParseMode.MARKDOWN_V2)
  await show_menu(update, context)


async def show_menu(update, context):
  """Handler for the /menu command."""
  menu_options = [['/logmeal'], ['/setreminder'], ['/recommend'], ['/cancel']]
  reply_markup = ReplyKeyboardMarkup(menu_options, one_time_keyboard=True)
  await update.message.reply_text(
    'Please select an option from the menu at the bottom right:',
    reply_markup=reply_markup)


def create_calendar(year, month, date_limit):
  calendar = []
  current_date = datetime(year, month, 1)
  today = datetime.now().date()
  #date_limit = today - timedelta(days=3)
  while current_date.month == month:
    week = []
    for i in range(7):
      if current_date.date() < date_limit.date() or current_date.date(
      ) > today:
        # Disable dates before the date limit and after today
        day_button = InlineKeyboardButton(text="", callback_data='disabled')
      else:
        day_button = InlineKeyboardButton(
          text=str(current_date.day),
          callback_data=current_date.strftime('%Y-%m-%d'))
      week.append(day_button)
      current_date += timedelta(days=1)
    calendar.append(week)
  return calendar


async def logmeal_start(update, context):
  """Handler to start the logmeal conversation."""
  await update.message.reply_text("Let's log a meal!")
  # Ask for date verification
  keyboard = [
    [InlineKeyboardButton("Yup!", callback_data="yes")],
    [InlineKeyboardButton("Nope", callback_data="no")],
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  await update.message.reply_text(f"Are you having your meal now?",
                                  reply_markup=reply_markup)

  return ISCURRENT


async def logmeal_IsCurrent(update, context):
  query = update.callback_query

  if query.data == 'yes':
    print("having meal now")
    context.user_data["Time_Of_Meal"] = datetime.now()
    await query.answer()  # Acknowledge the callback query

    #await update.message.reply_text(text=datetime.now())
    datetime_input = datetime.now()
    await logmeal_type(update, context, datetime_input)
    print("returned back to isCurrent")
    return NAME
    #return TYPE  # Proceed to the next step
  elif query.data == 'no':
    print("not having meal now")
    now = datetime.now()
    date_limit = now - timedelta(days=3)
    calendar = create_calendar(now.year, now.month, date_limit)
    reply_markup = InlineKeyboardMarkup(calendar)
    await query.message.edit_text(
      f"Please select a date from {date_limit.strftime('%Y-%m-%d')} to {now.strftime('%Y-%m-%d')}:",
      reply_markup=reply_markup)
    await query.answer()  # Acknowledge the callback query
    return DATE  # Proceed to handle_date_selection

  #default case
  else:
    await query.answer("Invalid selection")
    return None  # Stay in the current state


async def handle_date_selection(update, context):
  query = update.callback_query
  await query.answer()
  user_input = query.data  # Use query.data to access the callback query text

  selected_date = datetime.strptime(user_input, '%Y-%m-%d')
  current_date = datetime.now().date()
  date_limit = current_date - timedelta(days=3)

  if selected_date.date() >= date_limit and selected_date.date(
  ) <= current_date:
    print(selected_date.date())
    await update.callback_query.message.reply_text(
      text=f"You selected {selected_date.date()}.")
    context.user_data["Selected_Date"] = selected_date.date()
    await update.callback_query.message.reply_text(
      "Please enter the time in HH:MM format (24-hour clock):")
    return TIME
  else:
    await update.callback_query.message.edit_text(
      text="Please select a date within the past 3 days.")
    return None


async def logmeal_time(update, context):
  # query = update.callback_query
  # await query.answer()
  # user_input = query.data.strip()  # Use query.data to access the callback query text
  user_input = update.message.text.strip()
  print("Inside logmeal_time data is " + user_input)
  try:
    time_input = datetime.strptime(user_input, "%H:%M").time()
    selected_date = context.user_data.get("Selected_Date")
    if selected_date:
      time_full = datetime.combine(selected_date, time_input)
      context.user_data["Time_Of_Meal"] = time_full
      print(time_full)
      await update.message.reply_text(
        f"You have entered datetime: {time_full.strftime('%Y-%m-%d %H:%M')}")
      print("sending over to logmeal_type " + update.message.text)
      await logmeal_type(update, context, update.message.text)
      return NAME
    else:
      await update.message.reply_text("No selected date found.")
  except ValueError:
    await update.message.reply_text(
      "Invalid time format. Please enter the time in HH:MM format (24-hour clock)."
    )
  return NAME


async def logmeal_type(update, context, datetime_input):
  """Handler to get the meal type."""
  print("received from isCurrent", datetime_input)
  #print("LINK SUCCESSFUL,inside logmeal_type")
  # query = update.callback_query
  # await query.answer()
  # print("inside logmeal_type and data from logmeal_type" + query.data)
  if (datetime_input is None):
    datetime_input = update.message.text
  else:
    datetime_input = datetime_input
  print("inside logmeal_type and data from logmeal_type", datetime_input)
  meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Snack']
  keyboard = [[InlineKeyboardButton(type, callback_data=type)]
              for type in meal_types]
  reply_markup = InlineKeyboardMarkup(keyboard)

  if update.message is not None:
    await update.message.reply_text("Please select the type of the meal:",
                                    reply_markup=reply_markup)
  else:
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Please select the type of the meal:",
                                   reply_markup=reply_markup)

  return NAME


async def logmeal_add_Food_name(update, context):
  query = update.callback_query
  await query.answer()
  text = query.data  # Use query.data to access the callback query text
  print("Type of food is", text)

  if text in ['Breakfast', 'Lunch', 'Dinner', 'Snack']:
    context.user_data['type'] = text
    await query.message.reply_text("You have selected " + text)

  await query.message.reply_text("What have you eaten today?")
  return NAME


async def logmeal_name(update, context):
  """Handler to process the food name."""
  msg = update.message
  text = update.message.text
  print("entering logmeal_name, input food name is", text)
  #context.user_data["name"] = text
  # Search for similar food names in the database
  food_options = search_food_options(text)

  if food_options:
    # Provide food options for the user to choose from
    keyboard = [[
      InlineKeyboardButton(option, callback_data=option)
    ] for option in food_options]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose the closest food option:",reply_markup=reply_markup)
    #await update.callback_query.message.reply_text("Please choose the closest food option:",reply_markup=reply_markup)
    return INSERT_MEAL_ENTRY 
  ## have code to collect the food option chosen
  else:
    await update.message.reply_text(
      "No similar food options found. Please create a new meal name.")
    ## have code to collect the create_meal
    return CREATE_MEAL_NAME

## NOTE: COMMENTED OUT COMMIT MESSAGE FIRST TO NOT ADD TO DB!!
async def logmeal_insert_meal_entry(update, context):
  #text = update.message.text
  query = update.callback_query
  await query.answer()
  text = query.data  # Use query.data to access the callback query text
  
  print("in insert_meal_entry",text)
  context.user_data["name"] = text
  Person_id = update.effective_user.id
  print("Person_id is",Person_id)
  Halal = 0
  Food_Name = context.user_data["name"]
  Number_Of_Servings = 1
  Category = context.user_data['type']
  Time_Of_Meal = context.user_data["Time_Of_Meal"]
  insert_statement = "INSERT INTO meal VALUES (%s, %s, %s, %s, %s, %s)"
  
  # Execute the INSERT statement with user inputs
  
  try:
      cursor.execute(insert_statement, (Person_id,  Halal, Food_Name, Number_Of_Servings, Category, Time_Of_Meal))
      conn.commit()
      print("Data inserted successfully!")
  except mysql.connector.Error as err:
        
      print(f"Error: {err}")
      conn.rollback()
    
  await update.callback_query.message.reply_text("Meal entry logged successfully!")
  #await update.message.reply_text("Meal entry logged successfully!")
  

## test if it works
def search_food_options(query):
  """Search for similar food names in the database."""
  query = query.strip().lower()
  print("Entering search_food_options:", query)
  # Perform a database query to get food options
  try:
    cursor.execute("SELECT Food_Name FROM food")
    rows = cursor.fetchall()
  except mysql.connector.Error as err:
    logger.error("Database error: %s", err)
    return []

  food_names = [row[0].lower() for row in rows]
  print("food names is of type " ,type(food_names))
  matches = get_close_matches(query, food_names)
  print("matches returned", matches)
  return matches
  
async def logmeal_create_meal_name(update, context):
  """Handler to create a new meal name."""
  text = update.message.text
  if text.strip() == "":
    await update.message.reply_text("Invalid meal name. Please try again.")
    return CREATE_MEAL_NAME
  context.user_data["name"] = text.strip()
  # # Log the meal entry
  # user_id = update.message.from_user.id
  # meal_entries.append(
  #     {
  #         "user_id": user_id,
  #         "datetime": context.user_data["date"],
  #         "name": context.user_data["name"],
  #     }
  # )
  await update.message.reply_text("New food logged successfully!")
  return ConversationHandler.END


async def set_reminder(update, context):
  """Handler for setting scheduled reminders."""
  message = update.message
  user_id = message.from_user.id

  # Schedule reminders at three different times
  now = datetime.now()
  reminder_times = [
    now + timedelta(minutes=10),
    now + timedelta(minutes=30),
    now + timedelta(hours=1),
  ]

  for time in reminder_times:
    context.job_queue.run_once(send_reminder, time, context=user_id)

  await message.reply_text("Reminders set successfully!")

async def send_reminder(context):
  """Function to send reminder messages."""
  user_id = context.job.context
  await context.bot.send_message(chat_id=user_id,
                                 text="Time to eat your meal!")


async def cancel(update, context):
  """Handler for canceling the conversation."""
  # Clear the conversation data
  context.user_data.clear()
  await update.message.reply_text("Conversation canceled. You can start again using /logmeal.")
  return await logmeal_start(update, context)

# async def view_meals(update, context):
#   insert_statement = "SELECT FROM meal VALUES (%s, %s, %s, %s, %s, %s)"
#   # Execute the INSERT statement with user inputs
#   try:
#     cursor.execute(insert_statement, (Person_id,  Halal, Food_Name, Number_Of_Servings, Category, Time_Of_Meal))
#     conn.commit()
#     print("Data inserted successfully!")
#   except mysql.connector.Error as err:
#       print(f"Error: {err}")
#       conn.rollback()

async def recommend_start(update, context):
    # Create inline keyboard options for the food category
    category_keyboard = [
        [InlineKeyboardButton("Dessert", callback_data="Dessert")],
        [InlineKeyboardButton("Snack", callback_data="Snack")],
        [InlineKeyboardButton("Main", callback_data="Main")]
    ]
    reply_markup = InlineKeyboardMarkup(category_keyboard)

    # Ask the user to select a food category
    await update.message.reply_text(  # Await the reply_text coroutine
        "What category of food are you looking for?",
        reply_markup=reply_markup
    )
    return CATEGORY

async def category_selected(update, context):
    #Store the selected category in the context
    #text = update.message.text
    query = update.callback_query
    await query.answer()
    text = query.data  # Use query.data to access the callback query text
    print("in insert_meal_entry",text)
  
    context.user_data['category'] = update.callback_query.data
  
    # Create inline keyboard options for the halal preference
    halal_keyboard = [
        [InlineKeyboardButton("Halal", callback_data="Y")],
        [InlineKeyboardButton("Not Halal", callback_data="N")],
        [InlineKeyboardButton("Doesn't Matter", callback_data="DM")]
    ]
    reply_markup = InlineKeyboardMarkup(halal_keyboard)

    # Ask the user for their halal preference
    await update.callback_query.message.reply_text(
        "Do you want it to be halal?",
        reply_markup=reply_markup
    )
    return HALAL

async def halal_selected(update, context):
    # Store the selected halal preference in the context
    context.user_data['halal'] = update.callback_query.data

    # Retrieve the category and halal preference
    category = context.user_data['category']
    halal = context.user_data['halal']

    # Retrieve food recommendations from the database based on the category and halal preference
    cursor = conn.cursor()
    query = "SELECT Food_Name FROM food WHERE Category = %s AND (Halal = %s OR Halal IS NULL)"
    cursor.execute(query, (category, halal))
    results = cursor.fetchall()
    cursor.close()

    # Send a random food recommendation to the user
    if results:
        random_food = random.choice(results)[0]
        update.callback_query.message.reply_text(f"Food recommendation: {random_food}")
    else:
        update.callback_query.message.reply_text("No food found matching the criteria.")
    

def main():
  """Main function to start the bot."""
  dp = ApplicationBuilder().token(TOKEN).build()

  # Add command handlers
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("setreminder", set_reminder))
  dp.add_handler(CommandHandler("recommend", recommend_start))
  dp.add_handler(CommandHandler("menu", show_menu))
  dp.add_handler(CommandHandler("cancel", cancel))

  # Add conversation handler for logmeal
  logmeal_conv_handler = ConversationHandler(
    entry_points=[
      CommandHandler("logmeal", logmeal_start),
      CallbackQueryHandler(logmeal_start, pattern="^logmeal_start$")
    ],
    states={
      ISCURRENT: [
        CallbackQueryHandler(logmeal_IsCurrent),
        MessageHandler(filters.ALL, logmeal_IsCurrent)
      ],
      DATE: [CallbackQueryHandler(handle_date_selection)],
      TIME: [
        MessageHandler(filters.ALL, logmeal_time),
        MessageHandler(filters.ALL, logmeal_type),
        CallbackQueryHandler(logmeal_type),
      ],
      NAME: [
        CallbackQueryHandler(logmeal_add_Food_name),
        MessageHandler(filters.ALL, logmeal_name),
      ],
      CREATE_MEAL_NAME: [
        MessageHandler(filters.ALL & ~filters.COMMAND,
                       logmeal_create_meal_name)   
      ],
      INSERT_MEAL_ENTRY: [
        CallbackQueryHandler(logmeal_insert_meal_entry),
        MessageHandler(filters.ALL, logmeal_insert_meal_entry)
      ]
    },
    fallbacks=[CommandHandler("cancel", cancel)]
  )

  dp.add_handler(logmeal_conv_handler)

  # Add conversation handler for recommend
  recommend_conv_handler = ConversationHandler(
    entry_points=[
      CommandHandler("recommend", recommend_start),
      CallbackQueryHandler(recommend_start, pattern="^recommend_start$")],
    states={
      
      CATEGORY: [
         CallbackQueryHandler(category_selected),
      CallbackQueryHandler(category_selected,pattern='^(Dessert|Snack|Main)$')
      ],
      HALAL: [
        CallbackQueryHandler(halal_selected, pattern='^(Y|N|DM)$')
      ]
    },
    fallbacks=[CommandHandler("cancel", cancel)]
  )


  dp.add_handler(recommend_conv_handler)

  # Start the bot
  dp.run_polling()
  logger.info('Bot started!')
  dp.idle()


if __name__ == "__main__":
  main()
