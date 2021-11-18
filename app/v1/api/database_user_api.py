from app.v1.api.database_api import *


async def user_exist(email):
    return bool(await users.find_one({"email":email}))


async def insert_user(user_object):
    return bool(await users.insert_one(user_object))


async def backup_user(user):
    if bool(await user_deleted.find_one({"email":user["email"]})):
        await user_deleted.insert_one(user)


async def get_user(email):
    return await users.find_one({"email":email})


async def update_user(email, new_data):
    return await users.update_one({"email":email}, {"$set": new_data}, upsert=True)


async def delete_user(email):
    await backup_user(await get_user(email))
    return bool(await users.delete_one({"email":email}))