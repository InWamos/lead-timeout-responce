import asyncio
import os
import uvloop

from pyrogram.sync import compose
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from dotenv import load_dotenv
from handlers.timeout_responce import on_message


load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
if not API_ID or not API_HASH:
    raise ValueError("No config data provided")


async def main() -> None:

    apps = [Client("my_account"), Client("my_account2")]

    for app in apps:
        app.add_handler(MessageHandler(on_message))

    await compose(apps)


if __name__ == "__main__":
    uvloop.install()
    asyncio.run(main())
