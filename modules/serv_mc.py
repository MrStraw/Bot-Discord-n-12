from re import search

from discord import Member, Guild, Role, Message, TextChannel
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.utils import get

from utils import mc_command
from utils.mc_list import mc_list, mc_nb_online
from utils.nick_mc_to import nick_mc_to


class ServMC(commands.Cog, name="Serveur minecraft des Douziens"):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.guild: Guild = self.bot.get_guild(593145606839730206)  # serv épopée
        self.channel: TextChannel = self.guild.get_channel(892309111700615230)  # channel mc
        self.role_douzien: Role = self.guild.get_role(593152841552625870)
        self.check_online.start()

    @commands.command()
    async def mc(self, ctx, *raw_args):
        """ Lance une commande sur le serveur, dois être Douzien """
        user: Member = ctx.author
        message: Message = ctx.message

        if self.role_douzien not in user.roles:
            await ctx.send(f"**Commande résérvée au rôle {self.role_douzien.name}.**")
            return
        if not raw_args:
            await ctx.send("**Utilisation :**\n"
                           "    12.mc command arg1 arg2 ... \n"
                           "    Faite _12.mc help_ pour avoir la lite des commandes. ")
            return

        command, args = raw_args[0], raw_args[1:]

        # -------------------------------------- Commandes Valides -----------------------------------------------------

        if command == 'help':
            await ctx.send(f"**HELP mc**\n"
                           f"```"
                           f"Commande résérvées au role {self.role_douzien.name}\n"
                           f"Permet d'intéargir avec le serveur minecraft\n\n"
                           "  raw : Lance la commande en brut. Exemple: 12.mc raw /list\n"
                           "  say : Envoie un message au serveur (en signant par votre nom discord). "
                           "```")

        elif command == 'raw':
            command, args = raw_args[1], raw_args[2:]
            response = mc_command(command, *args)
            await ctx.send(response)

        elif command == 'say':
            check_some_players_co = mc_nb_online()
            if not check_some_players_co:
                await message.add_reaction('❌')
                return
            await message.add_reaction('✅')
            en_tete = f"[Discord: {user.display_name}] "
            mc_command('say', en_tete, *args)

        elif command == 'list':
            check_some_players_co = mc_nb_online()
            if not check_some_players_co:
                await message.add_reaction('❌')
                return
            s = ''
            for player_name in mc_list():
                discord_id = nick_mc_to(player_name)
                user_discord: Member = self.guild.get_member(discord_id)
                s += f"\n  - **{user_discord.display_name}** ({player_name})"
            await ctx.send(s)

        else:
            await ctx.send(f"**Commande non reconnue**. faites ``2.mc help` "
                           f"pour avoir la liste des commandes dédiées au serveur minecraft des douziens.")

    @tasks.loop(minutes=1)
    async def check_online(self):
        await self.channel.edit(name=f"serv-mc_{mc_nb_online()}_sur_20")
