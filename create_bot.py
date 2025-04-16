import logging # Импортируем библиотеку для логирования, чтобы записывать события и ошибки в процессе работы бота
import os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
# from decouple import config # Импортируем функцию config из библиотеки python-decouple для загрузки переменных окружения из файла .env
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from asyncpg_lite import DatabaseManager

#Создаем объект AsyncIOScheduler для планирования и выполнения задач по времени. Устанавливаем часовой пояс на Europe/Kiyv.
scheduler = AsyncIOScheduler(timezone='Europe/Kiev')

#Создаем список ID администраторов бота. Загружаем строку с ID администраторов из переменной окружения ADMINS, разделяем её по запятым и преобразуем каждый элемент в целое число.
admins = 7717448054

db_manager = DatabaseManager(db_url='postgresql+asyncpg://user1:mozgi389@localhost:5432/cleaner_db', deletion_password='mozgi389')

#Настраиваем базовое логирование с уровнем INFO, чтобы записывать важные сообщения. Устанавливаем формат логов, включающий время, имя логгера и уровень сообщения
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#Создаем логгер с именем текущего модуля, чтобы записывать лог-сообщения
logger = logging.getLogger(__name__)

#Создаем объект Bot с токеном, загруженным из переменной окружения TOKEN. По умолчанию прописал, чтоб бот корректно вопринимал HTML теги для форматирования текста
bot = Bot(token='7671425135:AAGeI_EdxMo7x-JqvJ2HFUq4QVnAJRsetl8', default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
