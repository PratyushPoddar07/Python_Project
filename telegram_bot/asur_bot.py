from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

Token = "Your TELEGRAM API_KEY"

# Initialize the application
app = Application.builder().token(Token).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to ASUR")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This particular message
        /Python -> The first video from the Python Playlist
        /SQL -> The first video from the SQL Playlist
        /Java -> The first video from the Java Playlist
        /contact -> Contact information
        """
    )

# async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("We have various playlists and articles available.")

async def Python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg.")

async def Java(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://www.youtube.com/playlist?list=PLs-JnCrPsdJFLUurhEk4AZ69xaqbDw6H4.")

async def SQL(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tutorial link: https://www.youtube.com/playlist?list=PLrL_PSQ6q062H5CetdplYW7xQKeq8XaR0.")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can contact on the  gmail:- 'shuvampoddar018@gmail.com' for more information.")

# Adding command handlers
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(CommandHandler('Python', Python))
app.add_handler(CommandHandler('Java', Java))
app.add_handler(CommandHandler('SQL', SQL))
app.add_handler(CommandHandler('contact', contact))

# Start the bot
app.run_polling()
