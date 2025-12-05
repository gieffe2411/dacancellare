# Source - https://stackoverflow.com/a
# Posted by Jeffrey DeLucca
# Retrieved 2025-12-05, License - CC BY-SA 4.0

import discord
import discord.ext.commands
from discord import app_commands as apc
class Generalgroup(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot

    @apc.command()
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message('Hello')

    # commands that prints the user message: /say [message]
    @apc.command()
    async def say(self, interaction: discord.Interaction, message: str):
        """Prints the user message"""
        await interaction.response.send_message(message)

    @apc.command()
    async def version(self, interaction: discord.Interaction):
        """tells you what version of the bot software is running."""
        await interaction.response.send_message('This is an untested test version')
