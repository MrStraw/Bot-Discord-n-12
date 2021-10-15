import os

from rcon import Client

from contents.env import MC_SERVER__IP, MC_SERVER__RCON_PORT, MC_SERVER__RCON_PASSWD


def mc_command(command: str, *args: str):
    with Client(MC_SERVER__IP, MC_SERVER__RCON_PORT, passwd=MC_SERVER__RCON_PASSWD) as client:
        response = client.run(command, *args)
        return response
