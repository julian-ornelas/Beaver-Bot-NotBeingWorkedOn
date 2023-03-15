import discord
from discord.ext import commands

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

async def setup(bot):
    await bot.add_cog(hangman(bot))