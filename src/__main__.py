import os
import asyncio

from pyrogram.sync import compose
from pyrogram.client import Client
from dotenv import load_dotenv


load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
if not API_ID or not API_HASH:
    raise ValueError("No config data provided")

async def main() -> None:

    apps = [
        Client("my_account2"),
        Client("my_account")
    ]

    for app in apps:
        app.add_handler
        
    await compose(apps)



if __name__ == "__main__":
    asyncio.run(main())