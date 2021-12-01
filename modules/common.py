import sys
from typing import Union

from discord import Member, User
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
        # bot.load_extension("modules.serv_mc")
        print("Bot12 ready !")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def sudo(self, ctx, *args):
        """ Commandes appartenants à l'owner du bot """
        bot = self.bot
        admin_c = bot.channel_admin
        command, args = args[0], args[1:]

        if command == 'stop':
            await admin_c.send('arret du bot..')
            await bot.channel_mc.edit(topic="")
            sys.exit()

        elif command == 'load':
            cog = 'modules.' + args[0]
            try:
                bot.load_extension(cog)
                print()
            except Exception as e:
                await admin_c.send(f"`ERROR:` _{type(e).__name__}_ - {e}")
            else:
                await admin_c.send('`SUCCESS`')

        elif command == 'unload':
            cog = 'modules.' + args[0]
            try:
                bot.unload_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send('**`SUCCESS`**')
