import os
import asyncio

from pyrogram.client import Client
from dotenv import load_dotenv


load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
if not API_ID or not API_HASH:
    raise ValueError("No config data provided")

async def main() -> None:
    async with Client("my_account", str(API_ID), str(API_HASH)) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


if __name__ == "__main__":
    asyncio.run(main())