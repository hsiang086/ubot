import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='#',intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is onlinne<<")

bot.run('MTA4MTIyMzc1NjUxNDYwMzE3OQ.G7pHCh.cu1ICkwbOdAY0l1QlGiizvcPejjjPtgNvv_Zec')