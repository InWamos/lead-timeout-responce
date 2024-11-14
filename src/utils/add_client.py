import asyncio
import uuid
from pyrogram.client import Client

TWO_FACTOR_CODE = ""

api_id = 0
api_hash = ""


async def main():
    async with Client(
        str(uuid.uuid4()),
        api_id,
        api_hash,
        workdir="data/sessions",
        password=TWO_FACTOR_CODE,
    ) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
