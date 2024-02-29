import discord

from discord import app_commands
from discord.ext import commands
from config import GUILD


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="ping")
    @app_commands.guilds(discord.Object(id=GUILD))
    async def ping(self, interaction):
        await interaction.response.send_message("Pong", ephemeral=True)


async def setup(bot):
    await bot.add_cog(PingCog(bot))
