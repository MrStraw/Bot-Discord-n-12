import os

import discord

from bot12 import Bot12
from contents.env import TOKEN
from modules import Common, ServMC


bot = Bot12(command_prefix="12.",
            intents=discord.Intents.all())

bot.add_cog(Common(bot))
bot.add_cog(ServMC(bot))

bot.run(TOKEN)
