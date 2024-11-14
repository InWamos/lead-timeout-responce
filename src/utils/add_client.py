import asyncio
import uuid
from pyrogram.client import Client

API_ID = 0
API_HASH = ""


async def main():
    async with Client(
        str(uuid.uuid4()),
        API_ID,
        API_HASH,
        workdir="data/sessions"
    ) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
