# (c) @AbirHasan2005

import datetime
import secrets
import motor.motor_asyncio
from configs import Config
import string
N = 6
class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            verify_date=datetime.date.today().isoformat(),
            verify_key=secrets.choice(Config.VERIFY_KEY) if Config.VERIFY_KEY else "".join(secrets.choice(string.ascii_uppercase+string.digits+string.ascii_lowercase) for i in range(N)),
            ban_status=dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason=''
            )
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return True if user else False
    
    async def get_verify_key(self,id):
        status = await self.col.find_one({'id' : int(id)})
        user_key = status.get('verify_key')
        if Config.VERIFY_KEY:
            if user_key in Config.VERIFY_KEY:
                pass
            else:
                verify_key=secrets.choice(Config.VERIFY_KEY)
                await self.col.update_one({'id': id}, {'$set' : {'verify_key': verify_key}})
                user_key = status.get('verify_key')
        return user_key
    
    async def update_verify_key(self,id):
        if Config.VERIFY_KEY:
            updates = secrets.choice(Config.VERIFY_KEY)
            await self.col.update_one({'id': id}, {'$set' : {'verify_key': updates}})
        else:
            updates = "".join(secrets.choice(string.ascii_uppercase+string.digits+string.ascii_lowercase) for i in range(N))
            await self.col.update_one({'id': id}, {'$set' : {'verify_key': updates}})
    
    async def update_verify_date(self , id):
        updates = datetime.date.today().isoformat()
        await self.col.update_one({'id': id}, {'$set': {'verify_date': updates}})
    
    async def verify_status(self,id):
        status = await self.col.find_one({'id' : int(id)})
        return status.get('verify_date')

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def remove_ban(self, id):
        ban_status = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason=''
        )
        await self.col.update_one({'id': id}, {'$set': {'ban_status': ban_status}})

    async def ban_user(self, user_id, ban_duration, ban_reason):
        ban_status = dict(
            is_banned=True,
            ban_duration=ban_duration,
            banned_on=datetime.date.today().isoformat(),
            ban_reason=ban_reason
        )
        await self.col.update_one({'id': user_id}, {'$set': {'ban_status': ban_status}})

    async def get_ban_status(self, id):
        default = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason=''
        )
        user = await self.col.find_one({'id': int(id)})
        return user.get('ban_status', default)

    async def get_all_banned_users(self):
        banned_users = self.col.find({'ban_status.is_banned': True})
        return banned_users


db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
