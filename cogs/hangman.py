import discord
from discord.ext import commands
import random
import requests
import json

class hangman(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="ping", description="test command")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong")


    @discord.app_commands.command(name="hangman", description="Play hangman!")
    @discord.app_commands.describe(length="Word length for the Hangman.")
    @discord.app_commands.choices(length=[
        discord.app_commands.Choice(name="short", value=1),
        discord.app_commands.Choice(name="medium", value=2),
        discord.app_commands.Choice(name="long", value=3),
    ])
    async def hangman(self, interaction: discord.Interaction, length: discord.app_commands.Choice[int]):
        
        await interaction.response.send_message(f"you have chosen {length.name}")
        game_length = length.value

        #code from my hangman repo
        if game_length == 1:
            number = str(random.randint(4, 6))
            word_request = requests.get("https://random-word-api.herokuapp.com/word?length=" + number)
        elif game_length == 2:
            number = str(random.randint(7, 10))
            word_request = requests.get("https://random-word-api.herokuapp.com/word?length=" + number)
        elif game_length == 3:
            number = str(random.randint(11, 15))
            word_request = requests.get("https://random-word-api.herokuapp.com/word?length=" + number)
        
        word = json.loads(word_request.text)
        word = json.dumps(word)
        word = word[2:-2]

        decompsed_word = list(word)

        word_length = len(word)

        #need to figure out embeds
        print(word)
        print()

async def setup(bot):
    await bot.add_cog(hangman(bot))