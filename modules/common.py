from discord.ext import commands

from bot12 import Bot12


class Common(commands.Cog):
    def __init__(self, bot: Bot12):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        bot = self.bot
        print(bot.user, "est connecté.")
        bot.charge_guild()
        print("Bot12 ready !")

