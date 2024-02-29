import discord

from discord import app_commands
from discord.ext import commands
from config import TOKEN, GUILD

guild_id = discord.Object(id=GUILD)
intents  = discord.Intents.all()
bot      = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    try:
        await bot.load_extension("cogs.ping")
        await bot.load_extension("cogs.resource")

        synced = await bot.tree.sync(guild=guild_id)
        print(f'Synced commands: {len(synced)}')

    except Exception as e:
        print(e)


bot.run(TOKEN)
