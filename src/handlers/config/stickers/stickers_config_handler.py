from pyrogram.types import Message
from pyrogram.client import Client
from data_readers.config.stickers.sticker_config import add_sticker, remove_sticker, get_sticker_config

async def on_sticker_add_command(client: Client, message: Message) -> None:
    """ Pattern: /add <sticker_name> <sticker_id>

    Args:
        client (Client): _description_
        message (Message): _description_
    """
    elements = message.text.split()
    sticker_name = elements[1]
    sticker_id = elements[2]

    try:
        await client.send_sticker(chat_id=message.chat.id, sticker=sticker_id)
        await message.reply(f"The sticker has been successfully added. Use:
                             ```/set {sticker_name}```
                             to set it as main")
        add_sticker(sticker_name, sticker_id)
    except Exception as e:
        await message.reply("Couldn't add the sticker to list")

