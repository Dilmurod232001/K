from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import CommandStart

BOT_TOKEN = "6799142842:AAGI9W_63USw4dT33BclpPKjso2Rgrlgbyg"

bot =Bot(token=BOT_TOKEN)
dp =Dispatcher(bot)

@dp.message_handler(CommandStart())
async def start_bot(message : types.Message):
    await message.reply(f"<b>Salom {message.from_user.first_name} ! Menga stiker yuboring va men uning identifikatori bilan javob beraman. \nBu Botlarni ishlab chiquvchi uchun foydali bo'lishi mumkin</b> ", parse_mode=types.ParseMode.HTML)

@dp.message_handler(content_types=['sticker'])
async def id_sticker(message : types.Message):
    try:
        await message.reply(message.sticker.file_id, parse_mode=types.ParseMode.MARKDOWN)
    except:
        await message.reply("*Qandaydir Xatolik Qayta yuborin...*", parse_mode=types.ParseMode.MARKDOWN)

@dp.message_handler(state=None)
async def echo_sticker(message : types.Message):
    try:
        await message.answer_sticker(message.text)
    except:
        await message.reply("*Bunday id da sticker Mavjud emas*", parse_mode=types.ParseMode.MARKDOWN)

# DASTURCHI : @MISTRUZ
#MANBA : @kingsofpy MANBAGA TEGILMASIN


from art import tprint as t

t("Kingsofpy")

if __name__ == '__main__':
    executor.start_polling(dp)
