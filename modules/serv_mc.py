from re import search
from typing import Union

from discord import Member, Guild, Role, Message, TextChannel, User
from discord.ext import commands, tasks
from discord.ext.commands import Bot

from contents.douziens import douziens
from contents.env import MC_SERVER__IP
from utils import mc_command
from utils.mc_utils import mc_list, mc_nb_online, mc_get_raw


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
        user: Union[Member, User] = ctx.author
        message: Message = ctx.message

        if self.role_douzien not in user.roles:
            await ctx.send(f"**Commande résérvée au rôle {self.role_douzien.name}.**")
            return
        elif not raw_args:
            await ctx.send("**Utilisation :**\n"
                           "    12.mc command arg1 arg2 ... \n"
                           "    Faite _12.mc help_ pour avoir la lite des commandes. ")
            return

        command, args = raw_args[0], raw_args[1:]

        # -------------------------------------- Commandes Valides -----------------------------------------------------

        if command == 'help':
            await ctx.send(f"**__HELP mc__**\n"
                           f"```md\n"
                           f"# Commande résérvées au role {self.role_douzien.name}.\n"
                           f"# Permet d'intéargir avec le serveur minecraft.\n\n"
                           # "  raw  : Lance la commande en brut. Exemple: `12.mc raw /list`.\n"
                           "  - say     : Envoie un message au serveur en signant par votre nom discord.\n"
                           "  - list    : Donne la liste des personnes connéctées, donne leur nom discord idéalement.\n"
                           "  - connect : Fiche d'aide pour ce connecter au serveur.\n"
                           "```")

        elif command == 'raw' and (user.id == 180213164749619200 or user.id == 186131928598970368):
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
            players_list = mc_list()
            if not players_list:
                await message.add_reaction('❌')
                return
            s = ''
            for player_name in players_list:
                check_pseudo = douziens.get(player_name, None)
                pseudo = f"**{self.guild.get_member(check_pseudo[1]).display_name}** ({player_name})" \
                    if check_pseudo is not None else player_name
                s += f"- {pseudo}\n"
            await ctx.send(s)

        elif command == 'connect':
            await ctx.send(f"```md\n"
                           f"# Fiche pour l'aide à la connection au serveur :\n\n"
                           f"  - ip      : {MC_SERVER__IP}:{mc_get_raw('hostport')}\n"
                           f"  - version : {mc_get_raw('version')}\n"
                           f"```")

        # elif command == 'test':
        #     await self.channel.edit(topic="ceci est un test")

        else:
            await ctx.send(f"**Commande non reconnue**. faites `12.mc help` "
                           f"pour avoir la liste des commandes dédiées au serveur minecraft des douziens.")

    @tasks.loop(minutes=1)
    async def check_online(self):
        nb_players = mc_nb_online()
        if not nb_players:
            await self.channel.edit(topic="0 joueur connécté")
        elif nb_players == 1:
            player_name = mc_list()[0]
            check_pseudo = douziens.get(player_name, None)
            pseudo = f"**{self.guild.get_member(check_pseudo[1]).display_name}**" \
                if check_pseudo is not None else player_name
            await self.channel.edit(topic=f"1 joueur connécté: {pseudo}")
        else:
            await self.channel.edit(topic=f"{nb_players} joueurs connéctés")
