from datetime import datetime, timedelta
from pyrogram.types import Message
from pyrogram.client import Client
from data_readers.memory.data_reader_io import is_timespan_long_enough, add_client
from data_readers.config.stickers.sticker_config import (
    get_main_sticker,
    get_sticker_id_by_key,
)


async def on_message(client: Client, message: Message) -> None:

    client_id = client.name
    sender_id = str(message.from_user.id)

    if is_timespan_long_enough(client_id, sender_id):
        sticker_main_key = get_main_sticker()
        sticker_main = get_sticker_id_by_key(sticker_main_key)
        first_message_scheduled_date = datetime.now() + timedelta(minutes=3)
        second_message_scheduled_date = datetime.now() + timedelta(minutes=5)
        await message.reply(text="Привет)", schedule_date=first_message_scheduled_date)
        await client.send_sticker(
            chat_id=message.chat.id,
            sticker=sticker_main,
            schedule_date=second_message_scheduled_date,
        )

        add_client(client_id, sender_id)
