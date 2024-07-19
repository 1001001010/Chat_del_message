import colorama
import asyncio
import logging
from aiogram import executor, Dispatcher, bot

from bot.handlers import dp
from bot.data.loader import scheduler
from bot.utils.utils_functions import delete_message

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)
colorama.init()

# Запуск заданий
async def scheduler_start():
    scheduler.add_job(delete_message, "interval", minutes=1)
    
#Выполнение функция после запуска бота
async def on_startup(dp: Dispatcher):
    await scheduler_start()
    
    print(colorama.Fore.RED + "=======================")
    print(colorama.Fore.GREEN + "Бот успешно запущен")
    print(colorama.Fore.RESET)
 
# Выполнение функции после выключения бота
async def on_shutdown(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()
    await (await dp.bot.get_session()).close()

if __name__ == "__main__":
    scheduler.start()
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)