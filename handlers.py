import deepl
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from db import create_history, edit_history

# библиотека заменяющая deepl
from translate import Translator
trans = Translator(from_lang='en', to_lang='ru')


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer('Привет! Я бот-переводчик. Отправь мне текст на английском языке, и я переведу его на русский.')
    #await create_history(user_id=msg.from_user.id)


@router.message()
async def message_handler(msg: Message):
    text = msg.text
    await msg.answer(trans.translate(text))
    # Решение задачи с использованием deepl
    #translator = deepl.Translator("YOUR_AUTH_KEY")
    #translate_message = await msg.answer(str(translator.translate_text(text, target_lang='ru')))
    #await edit_history(user_id=msg.from_user.id, message=text, translate_message=translate_message)


