import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = ""
with open("token", "r") as token_file:
    token = token_file.read()

@client.event
async def on_read():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "Ping":
        await message.channel.send("Pong")

    # Command handler here

client.run(token)
