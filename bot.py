# (c) @AbirHasan2005

import os
from aiohttp import web
from handlers import web_server
from configs import Config,PORT,TG_BOT_WORKERS
from pyrogram import Client

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=Config.BOT_USERNAME,
            in_memory = True,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "handlers"
            },            
            bot_token=Config.BOT_TOKEN,
            workers=TG_BOT_WORKERS
        )
    async def start(self):        
        await super().start()
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
