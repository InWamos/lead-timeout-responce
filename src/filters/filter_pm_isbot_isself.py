from pyrogram.types import Message

# For example, in a MessageHandler the update argument will be a Message;
# in a CallbackQueryHandler the update will be a CallbackQuery
async def check_pm_isbot_isself(_, __, query: Message) -> bool:
    """Filter to validate that the message not from the bot, in dm and not from the userbot

    Args:
        _ (_type_): self
        __ (_type_): client
        query (_type_): Message
    """
    if isinstance(query, Message):
        return (
            query.chat.type.value == "private"
            and not query.from_user.is_self
            and not query.from_user.is_bot
        )

    return False