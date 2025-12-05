
import discord
import simplegeneralgroup
import discord.ext.commands
from getDiscordToken import token
MY_GUILD = discord.Object(id=1444004258335686759)

class MyBot(discord.ext.commands.Bot):
    async def on_ready(self):
        await self.tree.sync(guild=MY_GUILD)

bot: discord.ext.commands.Bot = MyBot(command_prefix="/", intents=discord.Intents.default())


@bot.tree.command(guild=MY_GUILD)
async def slash(interaction: discord.Interaction, number: int, string: str):
    await interaction.response.send_message(f'Modify {number=} {string=}', ephemeral=True)

bot.tree.add_command(simplegeneralgroup.Generalgroup(bot), guild=MY_GUILD)

if __name__ == "__main__":
    bot.run(token())
