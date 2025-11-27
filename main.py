import discord
from discord import app_commands
from bot_config import DISCORD_TOKEN, GUILD_IDS 

# import bot commands
from commands.ping import ping, christine


intents = discord.Intents.default()
client = discord.Client(intents=intents) # sets up bot
tree = app_commands.CommandTree(client)


tree.add_command(ping, guilds=[discord.Object(id=gid) for gid in GUILD_IDS])
tree.add_command(christine, guilds=[discord.Object(id=gid) for gid in GUILD_IDS])

@client.event
async def on_ready():
    # registers commands for bot with instant sync
    for gid in GUILD_IDS:
        guild_obj = discord.Object(id=gid)
        await tree.sync(guild=guild_obj)
        print(f"Synced slash commands to guild {gid}")

    print(f"Bot is online as {client.user} (ID: {client.user.id})")

# run bot
client.run(DISCORD_TOKEN)
