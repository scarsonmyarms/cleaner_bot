import asyncio
from create_bot import bot, dp, scheduler
from handlers.admin import start_router
from aiogram.types import (BotCommand, #объект, используемый для создания команд бота. Каждая команда имеет два атрибута: command (имя команды) и description (описание команды)
                           BotCommandScopeDefault) #объект, определяющий область действия команд. В данном случае используется область по умолчанию, что означает, что команды будут действовать для всех пользователей

#Объявляем асинхронную функцию set_commands, которая будет использоваться для установки команд бота. Асинхронная функция используется, потому что взаимодействие с API Telegram требует выполнения асинхронных запросов
async def set_commands(): #Создаем список commands, содержащий три команды
    commands = [BotCommand(command='start', description='Старт'), #команда /start с описанием "Старт".
                BotCommand(command='bonus', description='инфо про бо')] #команда /start_3 с описанием "Старт 3"
    await bot.set_my_commands(commands, BotCommandScopeDefault()) #Вызываем метод set_my_commands объекта bot для установки команд бота. commands: список команд, который мы создали ранее. BotCommandScopeDefault(): область действия команд по умолчанию, которая устанавливает команды для всех пользователей

#Определяем основную асинхронную функцию main, которая будет запускаться при старте бота
async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10) #Добавляем задачу в планировщик scheduler. Задача send_time_msg будет выполняться каждые 10 секунд
    # scheduler.start() #Запускаем планировщик задач, чтобы он начал выполнять добавленные задачи по расписанию
    dp.include_router(start_router) #Добавляем роутер start_router в диспетчер dp. Это позволяет диспетчеру знать о всех обработчиках команд, которые определены в start_router

    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands() #вызовем функцию в конце главной функции (то есть наш бот сначала будет запускаться, а после отправлять командное меню):
    await dp.start_polling(bot) #Запускаем бота в режиме опроса (polling). Бот начинает непрерывно запрашивать обновления с сервера Telegram и обрабатывать их


if __name__ == "__main__":
    asyncio.run(main())

