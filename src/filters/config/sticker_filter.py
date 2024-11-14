from pyrogram.types import Message


async def filter_on_sticker_add_command(_, __, query: Message) -> bool:
    if isinstance(query, Message) and query.text:
        if query.text.startswith("/add") and len(query.text.split()) == 3:
            return True
    return False


async def filter_on_sticker_set_command(_, __, query: Message) -> bool:
    if isinstance(query, Message) and query.text:
        if query.text.startswith("/set") and len(query.text.split()) == 2:
            return True
    return False


async def filter_on_sticker_rm_command(_, __, query: Message) -> bool:
    if isinstance(query, Message) and query.text:
        if query.text.startswith("/rm") and len(query.text.split()) == 2:
            return True
    return False


async def filter_on_sticker_get_command(_, __, query: Message) -> bool:
    if isinstance(query, Message) and query.text:
        if query.text.startswith("/get") and len(query.text.split()) == 1:
            return True
    return False
