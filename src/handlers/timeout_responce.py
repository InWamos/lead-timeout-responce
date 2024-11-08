from pyrogram.types import Message
from pyrogram.client import Client

WHITELISTED = []


async def on_message(client: Client, message: Message) -> None:
    await message.react(emoji="🔥")