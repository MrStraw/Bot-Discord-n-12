from typing import Union

from discord import Member, Message, User
from discord.ext import commands, tasks

from bot12 import Bot12
from contents.douziens import douziens
from contents.env import MC_SERVER__IP
from utils.mc_utils import mc_list, mc_nb_online, mc_get_raw, mc_command


class ServMC(commands.Cog):
    def __init__(self, bot: Bot12):
        self.bot = bot
        self.check_online.start()
        print("Cog ServMC loaded")

    @commands.command()
    async def mc(self, ctx, *raw_args):
        """ Lance une commande sur le serveur, dois être Douzien """
        bot = self.bot
        user: Union[Member, User] = ctx.author
        message: Message = ctx.message

        if bot.role_douzien not in user.roles:
            await ctx.send(f"**Commande résérvée au rôle {bot.role_douzien.name}.**")
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
                           f"# Commande résérvées au role {bot.role_douzien.name}.\n"
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
                pseudo = f"**{bot.epopee.get_member(check_pseudo[1]).display_name}** ({player_name})" \
                    if check_pseudo is not None else player_name
                s += f"- {pseudo}\n"
            await ctx.send(s)

        elif command == 'connect':
            await ctx.send(f"```md\n"
                           f"# Fiche pour l'aide à la connection au serveur :\n\n"
                           f"  - ip      : {MC_SERVER__IP}:{mc_get_raw('hostport')}\n"
                           f"  - version : {mc_get_raw('version')}\n"
                           f"```")

        elif command == 'test':
            await self.bot.channel_test.send('test')

        else:
            await ctx.send(f"**Commande non reconnue**. faites `12.mc help` "
                           f"pour avoir la liste des commandes dédiées au serveur minecraft des douziens.")

    @tasks.loop(minutes=1)
    async def check_online(self):
        bot = self.bot
        nb_players = mc_nb_online()
        if not nb_players:
            await bot.channel_mc.edit(topic="0 joueur connécté")
        elif nb_players == 1:
            player_name = mc_list()[0]
            check_pseudo = douziens.get(player_name, None)
            pseudo = f"**{bot.epopee.get_member(check_pseudo[1]).display_name}**" \
                if check_pseudo is not None else player_name
            await bot.channel_mc.edit(topic=f"1 joueur connécté : {pseudo}")
        else:
            await bot.channel_mc.edit(topic=f"{nb_players} joueurs connéctés")


def setup(bot):
    bot.add_cog(ServMC(bot))
