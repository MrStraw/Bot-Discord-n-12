import discord

from bot12 import Bot12
from contents.env import TOKEN
from modules import Common, ServMC


bot = Bot12(command_prefix='//', intents=discord.Intents.all())
bot.add_cog(Common(bot))
bot.run(TOKEN)
