import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    await client.change_presence(status=discord.Status.online)

token = os.environ.get('DISCORD_TOKEN')
if not token:
    raise ValueError("DISCORD_TOKEN environment variable not set.")

client.run(token)
