import discord

client=discord.Client()
@client.event
async def on_ready():
    print(f'I am ready! I am logged as {client.user}')

client.run(token)
