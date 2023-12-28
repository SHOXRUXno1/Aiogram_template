import wikipedia
from aiogram import types

from loader import dp

wikipedia.set_lang("uz")


@dp.message_handler()
async def chek_wiki(message: types.Message):
    print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bunday ma'lumot topilmadi")
