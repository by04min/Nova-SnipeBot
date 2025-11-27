# commands/ping.py
import discord
from discord import app_commands
import sqlite_db    # Database handling


db = sqlite_db.SQLiteBackend("assassins.db")

@app_commands.command(
    name="ping",
    description="Replies with pong"
)
async def ping(interaction: discord.Interaction):
    # Test incrementScore and get total_snipes count
    db.increment_total_snipes()
    total_snipes = db.get_total_snipes()
    await interaction.response.send_message(f"pong (total_pongs: {total_snipes})")

@app_commands.command(
    name="christine",
    description="Replies with encouragemenet for Christine"
)
async def christine(interaction: discord.Interaction):
    await interaction.response.send_message("You are the best lebron james, Christine")