from email.policy import default

from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, FSInputFile
from aiogram.types import CallbackQuery, InputMediaAnimation, InputMediaDocument, InputMediaAudio, InputMediaPhoto, InputMediaVideo
import asyncio, os
from create_bot import admins, bot
from db_handler.db_func import insert_user, get_user_data
from keyboards.inline_kb import check_data, admin_kb
from filters.IsAdmin import IsAdmin
from utils.utils import get_now_time

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject):
    # в начале, я замаскировал подгрузку данных с базы данных под имитацию набора текста.
    user_info = await get_user_data(user_id=message.from_user.id)
    # Далее, если пользователь уже был в базе данных, то просто сформируем сообщение и отправим его с клавиатурой.
    if user_info:
        response_text = f'{user_info.get("full_name")}, Вижу что вы уже в моей базе данных.'
    else:
        await insert_user(user_data={
            'user_id': message.from_user.id,
            'full_name': message.from_user.full_name,
            'user_login': message.from_user.username,
            'date_reg': get_now_time()
        })
        response_text = f' списибо за регистрацию.'

    await message.answer(text=response_text, reply_markup=admin_kb(message.from_user.id))


@start_router.message(F.text.contains('start1'), IsAdmin(admins))
async def admin(message: Message):
    await message.answer('privet admin', reply_markup=admin_kb())

@start_router.message(F.text == '/bonus')
async def bonus_info(message: Message):
    await message.answer('вот информация как ты получаешь свои бонус за выполненую работу')

@start_router.message(Command('work'))
async def worker(message: Message):
    await message.answer('vot klava', reply_markup=check_data())

@start_router.callback_query(F.data == 'incorrect')
async def incorrect(call: CallbackQuery):
    await call.message.answer('вы отказались от работы')
    await call.answer()

@start_router.callback_query(F.data == 'correct')
async def correct(call: CallbackQuery):
    await call.message.answer('вы приняли работу')
    await call.answer()