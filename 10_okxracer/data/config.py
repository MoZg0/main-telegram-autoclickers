import os
import sys
import importlib.util
parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
file_path = os.path.join(parent_dir, "global_data", "global_config.py")
spec = importlib.util.spec_from_file_location("global_config", file_path)
modu = importlib.util.module_from_spec(spec)
sys.modules["global_config"] = modu
spec.loader.exec_module(modu)
import global_config

# api id, hash
API_ID = global_config.API_ID
API_HASH = global_config.API_HASH

USE_TG_BOT = global_config.USE_TG_BOT # True if you want use tg, else False
BOT_TOKEN = global_config.OKXRACER_BOT_TOKEN # API TOKEN get in @BotFather
CHAT_ID = global_config.CHAT_ID # Your telegram id

ACC_DELAY = global_config.ACC_DELAY
PROXY_TYPE = global_config.PROXY_TYPE
REF_CODE = 'linkCode_65404668'

WHITELIST = {4, 6, 7, 10, 11, 12, 13, 14, 15, 16}

WORKDIR = "sessions/"

USE_PROXY = global_config.USE_PROXY

# задержка между кругом
BIG_SLEEP = [3600,10000]

MINI_SLEEP = [3,20]

# задержка между тасками
TASK_SLEEP = [10,30] #[min,max]

# задержка между бустами
BOOST_SLEEP = [5,15] #[min,max]


hello ='''              _                               __  _        
 _ __    ___ | |_  _   _   __ _  ___   ___   / _|| |_  ___ 
| '_ \  / _ \| __|| | | | / _` |/ __| / _ \ | |_ | __|/ __|
| |_) ||  __/| |_ | |_| || (_| |\__ \| (_) ||  _|| |_ \__ \\
| .__/  \___| \__| \__, | \__,_||___/ \___/ |_|   \__||___/
|_|                |___/        

'''
