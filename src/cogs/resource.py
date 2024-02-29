from os import EFD_SEMAPHORE
import discord
import authorize
import log

from discord import app_commands
from discord.ext import commands
from config import GUILD, RESOURCE_CHANNEL_ID


class ResourceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="resource")
    @app_commands.check(authorize.has_authorized_role)
    @app_commands.guilds(discord.Object(id=GUILD))
    @app_commands.describe(
        title       = "The title of the resource",
        url         = "The link to the resource",
        description = "(Optional) A description of the resource",
        tags        = "(Optional) A comma separated list of tags to make it easier to find the resource. Only supports letters and numbers."
    )
    async def resource(
        self,
        interaction: discord.Interaction,
        title      : str,
        url        : str,
        description: str = "",
        tags       : str = ""
    ):
        log.info(f"User {interaction.user.name}: /resource {title} {url} {description} {tags}")

        resource_channel = self.bot.get_channel(RESOURCE_CHANNEL_ID)

        embed = discord.Embed(title=title, description=description)
        embed.add_field(name="Tags", value=tags, inline=False)
        embed.add_field(name="URL",  value=url,  inline=False)

        await resource_channel.send(embed=embed)

    @resource.error
    async def resource_error(self, interaction, error):
        log.warn(f"UNAUTHORIZED: User {interaction.user.name}: /resource [arguments dropped]")
        await interaction.response.send_message(
            "Not authorized to use /resource!",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(ResourceCog(bot))
