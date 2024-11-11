from datetime import datetime, timedelta
from pyrogram.types import Message
from pyrogram.client import Client
from data_readers.data_reader_io import is_timespan_long_enough, add_client

STICKER_ID = "CAACAgQAAxkBAAKH92culXa1_BeNrC5FV9OrNRZ3sft4AAKwFgAC0p4hUdwkJLVYoVIlNgQ"

async def on_message(client: Client, message: Message) -> None:

    if message.chat.type.value == "private" and not message.from_user.is_self and not message.from_user.is_bot:
        client_id = client.name
        sender_id = str(message.from_user.id)
        
        if is_timespan_long_enough(client_id, sender_id):

            first_message_scheduled_date = datetime.now() + timedelta(minutes=3)
            second_message_scheduled_date = datetime.now() + timedelta(minutes=5)
            await message.reply(text="Привет)", schedule_date=first_message_scheduled_date)
            await client.send_sticker(
                chat_id=message.chat.id,
                sticker=STICKER_ID,
                schedule_date=second_message_scheduled_date,
            )
            
            add_client(client_id, sender_id)