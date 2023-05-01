import voice 
import asyncio
from aiogram import Bot, Dispatcher, executor as exc
from aiogram.types import ContentType, Message
import os
import answers
import config

bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: Message):
    await message.answer(answers.start)

@dp.message_handler(content_types=[ContentType.VOICE, ContentType.VIDEO_NOTE])
async def voice_recognition(message: Message):
    if message.content_type == ContentType.VOICE:
        file_id = message.voice.file_id
        path=fr"Temp\Voice\Voice\{file_id}.ogg"
    elif message.content_type == ContentType.VIDEO_NOTE:
        file_id = message.video_note.file_id
        path=fr"Temp\Voice\Video\{file_id}.mp4"
    
    file = await bot.get_file(file_id)
    await bot.download_file(file.file_path, destination=path)
    data =voice.recognition(path)
    await asyncio.sleep(1)
    await message.answer(data[0], reply=True)
    try:
        os.remove(data[1])
        os.remove(data[2])
    except: pass

exc.start_polling(dp, skip_updates=True)