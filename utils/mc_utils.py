import os

from mcstatus import MinecraftServer

from contents.env import MC_SERVER__IP, MC_SERVER__QUERY_PORT

mc_server = MinecraftServer.lookup(f"{MC_SERVER__IP}:{MC_SERVER__QUERY_PORT}")


def mc_list() -> list[str]:
    return mc_server.query().players.names


def mc_nb_online() -> int:
    return mc_server.query().players.online


def mc_get_raw(key: str = None):
    if key is None:
        return mc_server.query().raw
    else:
        return mc_server.query().raw.get(key)
