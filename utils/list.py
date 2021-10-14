import os
from typing import Tuple

from mcstatus import MinecraftServer
from dotenv import load_dotenv

load_dotenv()
ip = os.getenv("MC_SERVER__IP")
port = int(os.getenv("MC_SERVER__PORT"))
mc_server = MinecraftServer.lookup(f"{ip}:{port}")


def mc_get_online() -> int:
    return mc_server.status().players.online
