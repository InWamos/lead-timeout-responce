from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.client import Client
from data_readers.config.stickers.sticker_config import (
    add_sticker,
    get_main_sticker,
    remove_sticker,
    get_sticker_config,
    set_main_sticker,
)


async def on_sticker_add_command(client: Client, message: Message) -> None:
    """Pattern: /add <sticker_name> <sticker_id>

    Args:
        client (Client): _description_
        message (Message): _description_
    """
    elements = message.text.split()
    sticker_name = elements[1]
    sticker_id = elements[2]

    try:
        await client.send_sticker(chat_id=message.chat.id, sticker=sticker_id)
        await message.reply(
            f"The sticker has been successfully added. Use:\n`/set {sticker_name} `to set it as main",
            parse_mode=ParseMode.MARKDOWN
        )
        add_sticker(sticker_name, sticker_id)
    except Exception as e:
        await message.reply("Couldn't add the sticker to list")


async def on_sticker_set_command(client: Client, message: Message) -> None:
    """Pattern: /set <sticker_name>

    Args:
        client (Client): _description_
        message (Message): _description_
    """
    elements = message.text.split()
    sticker_name = elements[1]

    try:
        set_main_sticker(sticker_name)
        await message.reply(f"Sticker {sticker_name} set as main. We gonna use it now")
    except ValueError as ve:
        await message.reply(
            f"This sticker doesn't exist. Add is with\n`/add {sticker_name} your-sticker-id `",
            parse_mode=ParseMode.MARKDOWN,
        )
    except Exception as e:
        await message.reply(f"unknown server error: {e}")


async def on_sticker_rm_command(client: Client, message: Message) -> None:
    """Pattern: /rm <sticker_name>

    Args:
        client (Client): _description_
        message (Message): _description_
    """
    elements = message.text.split()
    sticker_name = elements[1]

    try:
        remove_sticker(sticker_name)
        await message.reply(f"Sticker {sticker_name} has been removed")
    except Exception as e:
        await message.reply(
            "Couldn't remove this sticker. Maybe it doesn't exist or you made a typo"
        )


async def on_sticker_get_command(client: Client, message: Message) -> None:
    """Pattern: /get

    Args:
        client (Client): _description_
        message (Message): _description_
    """
    stickers_config = get_sticker_config()
    stickers: dict[str, str] = stickers_config["stickers"]  # type: ignore
    try:
        main_sticker = get_main_sticker()
    except ValueError as ve:
        main_sticker = None

    string_builder = ""

    if stickers:
        string_builder += "Your sticker setup:\n"
        for sticker_name, sticker_value in stickers.items():
            string_builder += f"**{sticker_name}** : {sticker_value}\n"
        if main_sticker:
            string_builder += f"\nCurrent sticker: {main_sticker}"

    else:
        string_builder = (
            "We have no stickers to show. Add them with \n`/add name sticker-id `"
        )

    await message.reply(string_builder, parse_mode=ParseMode.MARKDOWN)
