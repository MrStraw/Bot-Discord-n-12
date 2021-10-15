import os

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")
MC_SERVER__IP = os.getenv("MC_SERVER__IP")
MC_SERVER__RCON_PORT = int(os.getenv("MC_SERVER__RCON_PORT"))
MC_SERVER__RCON_PASSWD = os.getenv("MC_SERVER__RCON_PASSWD")
MC_SERVER__QUERY_PORT = int(os.getenv("MC_SERVER__QUERY_PORT"))
