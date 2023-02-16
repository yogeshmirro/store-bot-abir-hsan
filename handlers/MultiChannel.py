from configs import Config
DB_CHANNEL = [Config.DB_CHANNELS[0]]
DBChannelDict = {i:f"storedb{Config.DB_CHANNELS.index(i)}" for i in Config.DB_CHANNELS}
async def get_db_channel():
    return int(DB_CHANNEL[0])
async def get_db_dict():
    return DBChannelDict
async def change_db_channel(channel_id):
    DB_CHANNEL[0]=str(channel_id)
async def get_db_indentity():
    db_channel = await get_db_channel()
    return DBChannelDict[str(db_channel)]
