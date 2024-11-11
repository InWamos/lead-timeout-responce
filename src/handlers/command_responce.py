from pyrogram.types import Message
from pyrogram.client import Client

STICKER_ID = "CAACAgIAAxkBAAKI02cyUrhn_snxmh07Ag7PMsenNowqAAJhAQACEBptIu-IjH2qmk0HNgQ"

async def on_command(client: Client, message: Message) -> None:

    if message.chat.type.value == "private" and not message.from_user.is_self and not message.from_user.is_bot:
        if message.text == "работа":
            await client.send_sticker(chat_id=message.chat.id, sticker=STICKER_ID)