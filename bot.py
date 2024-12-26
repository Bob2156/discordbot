import os
import asyncio
from discord.ext import commands
from flask import Flask

# Flask app for Vercel deployment
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Discord bot setup
intents = discord.Intents.default()
intents.messages = True  # Ensure message-related intents are enabled
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Start Flask and bot together
if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN not set!")
    else:
        loop = asyncio.get_event_loop()
        loop.create_task(bot.start(token))
        app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
