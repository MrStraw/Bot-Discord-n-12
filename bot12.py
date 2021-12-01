from discord import Guild, TextChannel, Role
from discord.ext.commands import Bot


class Bot12(Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

    def charge_guild(self):
        self.epopee: Guild = self.get_guild(593145606839730206)  # serv épopée

        self.channel_mc: TextChannel = self.epopee.get_channel(892309111700615230)
        self.channel_test: TextChannel = self.epopee.get_channel(836906660211589130)
        self.channel_admin: TextChannel = self.epopee.get_channel(599392002978742361)

        self.role_douzien: Role = self.epopee.get_role(593152841552625870)
