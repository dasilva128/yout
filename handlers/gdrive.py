# handlers/gdrive.py
from pyrogram import Client, filters
from pyrogram.types import Message
from utils.gdrive_utils import upload_to_gdrive, download_from_gdrive

upload_handler = filters.command("upload")
download_handler = filters.command("gdownload")

async def upload(client: Client, message: Message):
    if len(message.command) < 3:
        await message.reply_text("لطفاً لینک فایل و نام فایل را وارد کنید. مثال: /upload <لینک فایل> <نام فایل>")
        return

    file_path = message.command[1]
    file_name = message.command[2]
    try:
        file_id = upload_to_gdrive(file_path, file_name)
        await message.reply_text(f"فایل با موفقیت آپلود شد. شناسه فایل: {file_id}")
    except Exception as e:
        await message.reply_text(f"خطا در آپلود: {str(e)}")

async def download(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("لطفاً شناسه فایل گوگل درایو را وارد کنید. مثال: /gdownload <شناسه فایل>")
        return

    file_id = message.command[1]
    try:
        file_path = download_from_gdrive(file_id)
        with open(file_path, "rb") as file:
            await message.reply_document(file, caption=f"دانلود شده از گوگل درایو: {file_id}")
        os.remove(file_path)  # حذف فایل پس از ارسال
    except Exception as e:
        await message.reply_text(f"خطا در دانلود: {str(e)}")