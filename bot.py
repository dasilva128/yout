# bot.py
import os
from pyrogram import Client, filters
from handlers import start, download, gdrive

# ایجاد پوشه دانلود در صورت عدم وجود
if not os.path.exists("downloads"):
    os.makedirs("downloads")

app = Client(
    "my_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# ثبت هندلرها
app.add_handler(start.start_handler)
app.add_handler(download.download_handler)
app.add_handler(gdrive.upload_handler)
app.add_handler(gdrive.download_handler)

if __name__ == "__main__":
    print("Bot is running...")
    app.run()