import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="b.", intents=intents, activity=discord.Game(name="In Production"))

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")
    
    await bot.tree.sync()

bot.run(os.getenv("discord_token"))