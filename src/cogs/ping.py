import discord
import authorize
import log

from discord import app_commands
from discord.ext import commands
from config import GUILD


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="ping")
    @app_commands.guilds(discord.Object(id=GUILD))
    @app_commands.check(authorize.has_authorized_role)
    async def ping(self, interaction):
        log.info(f"User {interaction.user.name}: /ping")
        await interaction.response.send_message("Pong", ephemeral=True)

    @ping.error
    async def ping_error(self, interaction, error):
        log.warn(f"UNAUTHORIZED: User {interaction.user.name}: /ping")
        await interaction.response.send_message(
            "Not authorized to use /ping!",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(PingCog(bot))
