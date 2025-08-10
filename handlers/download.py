# handlers/download.py
from pyrogram import Client, filters
from pyrogram.types import Message
from utils.download_utils import download_with_ytdlp
import os

download_handler = filters.command("download")

async def download(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("لطفاً یک لینک معتبر وارد کنید. مثال: /download <لینک>")
        return

    url = message.command[1]
    try:
        file_path = download_with_ytdlp(url)
        with open(file_path, "rb") as file:
            await message.reply_document(file, caption=f"دانلود شده: {os.path.basename(file_path)}")
        os.remove(file_path)  # حذف فایل پس از ارسال
    except Exception as e:
        await message.reply_text(f"خطا در دانلود: {str(e)}")