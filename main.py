import os

from discord.ext import commands

from contents.env import TOKEN
from modules import Start, ServMC, Test


bot = commands.Bot(command_prefix="12.")
# bot.add_cog(Test(bot))
bot.add_cog(Start(bot))
bot.add_cog(ServMC(bot))
bot.run(TOKEN)
