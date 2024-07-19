from bot.data.loader import dp, bot
from bot.data.config import chat_id
from aiogram import types

@dp.message_handler(content_types = ['new_chat_members', 'left_chat_member'])
async def delete(message):
    print(message["message_id"])
    # await bot.delete_message(chat_id, message.message_id)
    # print("Удалил")