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
        synced = await bot.tree.sync(guild=guild_id)
        print(f'Synced commands: {len(synced)}')

    except Exception as e:
        print(e)


@bot.tree.command(name="ping", guild=guild_id)
async def ping(
    interaction: discord.Interaction
):
    await interaction.response.send_message("Pong. I am alive.")
 

@bot.tree.command(name="resource", guild=guild_id)
@app_commands.describe(
    title="The title of the resource",
    description="Description of the resource",
    url="The link to the resource"
)
async def resource(
    interaction: discord.Interaction,
    title: str,
    url: str,
    description: str=''
):
    embed = discord.Embed(title=title, description=description)
    embed.add_field(name="URL", value=url)

    await interaction.response.send_message(embed=embed)


bot.run(TOKEN)
