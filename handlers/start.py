# handlers/start.py
from pyrogram import Client, filters
from pyrogram.types import Message

start_handler = filters.command("start")

async def start(client: Client, message: Message):
    await message.reply_text(
        "سلام! به ربات دانلود و آپلود خوش آمدید.\n"
        "دستورات:\n"
        "/download <لینک> - دانلود از لینک (پشتیبانی از yt-dlp)\n"
        "/upload <لینک فایل محلی> <نام فایل در گوگل درایو> - آپلود به گوگل درایو\n"
        "/gdownload <شناسه فایل گوگل درایو> - دانلود از گوگل درایو"
    )