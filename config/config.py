from environs import Env
import os

_path = os.path.abspath(os.curdir)
env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
DATABASE_URI = env.str('DATABASE_URI')
