import os
from discord.ext import commands
from flask import Flask

# Discord bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Flask app for Vercel
app = Flask(__name__)

@app.route("/")
def home():
    return "Discord Bot is running!"

# Run the bot
if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    bot.loop.create_task(bot.start(token))
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

