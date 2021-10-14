import os

from dotenv import load_dotenv
from rcon import Client


load_dotenv()
ip = os.getenv("MC_SERVER__IP")
port = int(os.getenv("MC_SERVER__RCON_PORT"))
passwd = os.getenv("MC_SERVER__RCON_PASSWD")


def mc_command(command: str, *args: str):
    with Client(ip, port, passwd=passwd) as client:
        response = client.run(f"/{command}", *args)
        return response
