import discord
from discord.ext import commands

class hangman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"This loaded.")

    @discord.app_commands.command(name="ping", description="test command")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong")

async def setup(bot):
    await bot.add_cog(hangman(bot))