from asyncio import sleep

from discord import Member, TextChannel, Message
from discord.ext import commands, tasks
from discord.ext.commands import Bot


class Test(commands.Cog, name='loopTest'):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.channel: TextChannel = self.bot.get_channel(836906660211589130)  # Salon test de la section admin
        self.the_loop.start()

    @commands.command()
    async def t_channel(self, ctx, *args):
        # channel: TextChannel = self.bot.get_channel(836906660211589130)
        user: Member = ctx.author
        message: Message = await self.channel.send("ok ok")
        await sleep(2)
        await message.edit(content="test")

    @tasks.loop(seconds=5)
    async def the_loop(self):
        await self.channel.send("loop")
