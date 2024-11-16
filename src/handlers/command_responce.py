from pyrogram.types import Message
from pyrogram.client import Client
from data_readers.memory.data_reader_io import is_timespan_long_enough, add_client

STICKER_ID = "CAACAgIAAxkBAAKI02cyUrhn_snxmh07Ag7PMsenNowqAAJhAQACEBptIu-IjH2qmk0HNgQ"

async def on_command(client: Client, message: Message) -> None:

    client_id = client.name
    sender_id = str(message.from_user.id)

    if is_timespan_long_enough(client_id, sender_id):
        await client.send_sticker(chat_id=message.chat.id, sticker=STICKER_ID)
        add_client(client_id, sender_id)