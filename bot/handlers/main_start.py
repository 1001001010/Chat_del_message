from bot.data.loader import dp, bot

@dp.message_handler(content_types = ['new_chat_members', 'left_chat_member'])
async def delete(message):
    try:
        await bot.delete_message(message["chat"]["id"], message["message_id"])
    except:
        pass