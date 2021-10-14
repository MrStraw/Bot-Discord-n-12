from discord import Member, Guild, Role
from discord.ext import commands
from discord.ext.commands import Bot

from utils import mc_command


class ServMC(commands.Cog, name="Serveur minecraft des Douziens"):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.command()
    async def mc(self, ctx, *args):
        """ Lance une commande sur le serveur, dois être Douzien """
        user: Member = ctx.author
        guild: Guild = user.guild
        role_douzien: Role = guild.get_role(593152841552625870)

        if role_douzien not in user.roles:
            await ctx.send(f"**Il faut être {role_douzien.name} pour accéder à la commande _12.mc_**")
        elif not args:
            await ctx.send("**Utilisation :** 12.mc command arg1 arg2 ... \n"
                           "Faite _12.mc help_ pour plus d'info. ")

        else:
            command, args = args[0], args[1:]

        # -------------------- Commandes Valides --------------------

            if command == 'help':
                await ctx.send("menu help")

            elif command == 'raw':
                command, args = args[1], args[2:]
                response = mc_command(command, *args)
                await ctx.send(response)

            elif command == 'say':
                en_tete = '[Discord: ' + user.display_name + '] '
                await ctx.send(mc_command('say', en_tete, *args))
