from datetime import datetime, timedelta
from pyrogram.types import Message
from pyrogram.client import Client


async def on_message(client: Client, message: Message) -> None:

    if message.chat.type.value == "private":
        first_message_scheduled_date = datetime.now() + timedelta(minutes=3)
        second_message_scheduled_date = datetime.now() + timedelta(minutes=5)
        await message.reply(text="Привет)", schedule_date=first_message_scheduled_date)
        await client.send_sticker(
            chat_id=message.chat.id,
            sticker="CAACAgQAAxkBAAKH92culXa1_BeNrC5FV9OrNRZ3sft4AAKwFgAC0p4hUdwkJLVYoVIlNgQ",
            schedule_date=second_message_scheduled_date,
        )
