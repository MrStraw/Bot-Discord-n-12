import os

import discord
from discord.ext import commands

from contents.env import TOKEN
from modules import Start, ServMC, Test


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="12.", intents=intents)

# bot.add_cog(Test(bot))
bot.add_cog(Start(bot))
bot.add_cog(ServMC(bot))

bot.run(TOKEN)
