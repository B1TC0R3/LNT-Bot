import discord
import os
import log

from discord import app_commands
from discord.ext import commands
from config import TOKEN, GUILD

guild_id = discord.Object(id=GUILD)
intents  = discord.Intents.all()
bot      = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    try:
        for file in os.listdir("./cogs"):
            if os.path.isfile(file) and file.endswith(".py"):
                bot.load_extension(f"cogs.{file[:-3]}")

        synced = await bot.tree.sync(guild=guild_id)
        log.info(f"Synced commands: {len(synced)}")

    except Exception as e:
        print(e)


bot.run(TOKEN)
