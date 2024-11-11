from pyrogram.types import Message
from pyrogram.client import Client
from data_readers.data_reader_io import is_timespan_long_enough, add_client

STICKER_ID = "CAACAgIAAxkBAAKI02cyUrhn_snxmh07Ag7PMsenNowqAAJhAQACEBptIu-IjH2qmk0HNgQ"

async def on_command(client: Client, message: Message) -> None:

    if message.chat.type.value == "private" and not message.from_user.is_self and not message.from_user.is_bot:
        if message.text.lower() == "работа":
            client_id = client.name
            sender_id = str(message.from_user.id)
        
            if is_timespan_long_enough(client_id, sender_id):
                await client.send_sticker(chat_id=message.chat.id, sticker=STICKER_ID)
                add_client(client_id, sender_id)