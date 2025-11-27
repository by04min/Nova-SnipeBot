# commands/ping.py
import discord
from discord import app_commands

@app_commands.command(
    name="ping",
    description="Replies with pong"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")
