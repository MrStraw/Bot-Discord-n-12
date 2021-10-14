import os

from discord.ext import commands
from dotenv import load_dotenv

from modules import Start, ServMC, Test

load_dotenv()


bot = commands.Bot(command_prefix="12.")
# bot.add_cog(Test(bot))
bot.add_cog(Start(bot))
bot.add_cog(ServMC(bot))
bot.run(os.getenv("TOKEN"))
