import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents, activity=discord.Game(name="In Production"))
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"We have logged in as {client.user}")

@tree.command(name="ping", description="test command")
async def ping(message):
    await message.response.send_message("pong")

client.run(os.getenv("discord_token"))