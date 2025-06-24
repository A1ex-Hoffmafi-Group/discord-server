import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import webbrowser


intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix='t!',
    intents=intents
)


@bot.tree.command(name="test")
async def test(ctx: discord.Interaction):
    await ctx.response.send_message("Test")


@bot.tree.command(name="i_love_mrdrip_by_andi", description="PingPong")
@app_commands.describe(user="Wen soll ich pingen?")
async def pingmich(interaction: discord.Interaction, user: discord.User):
    user_mention = user.mention

    await interaction.response.send_message()


@bot.event
async def on_ready():
    print(f"Bot eingelogt als {bot.user}")
    await bot.tree.sync()

load_dotenv()
webserver.keep_alive()
bot.run(os.getenv("MTM4Njc3MDgyMTg2Mjc4NTA5NQ.Gz0CCt.il8GV7ZyGkHooLZ1wqm-2oXZXE_0wYe85K-gV4"))