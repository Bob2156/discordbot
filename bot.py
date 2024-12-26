iimport os
import asyncio
from discord.ext import commands
import discord
from flask import Flask

# Flask setup for Vercel
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    print(f"Received !ping from {ctx.author}")
    await ctx.send("Pong!")

# Combine Flask and Discord bot
if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN not found!")
    else:
        loop = asyncio.get_event_loop()
        loop.create_task(bot.start(token))
        app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
