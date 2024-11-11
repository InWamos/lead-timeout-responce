from pyrogram.types import Message

COMMANDS = ["работа"]

async def check_if_message_in_commands(_, __, query: Message) -> bool:
    if isinstance(query, Message) and query.text:
        return query.text.lower() in COMMANDS
    else:
        return False