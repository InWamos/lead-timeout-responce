import asyncio
import pyrogram
import uvloop

from pathlib import Path
from filters.commands import filter_in_commands_list
from filters.config import sticker_filter
from pyrogram.sync import compose
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from filters.timeout import filter_pm_isbot_isself
from handlers.timeout.timeout_responce import on_message
from handlers.commands.command_responce import on_command
from handlers.config.stickers.stickers_config_handler import (
    on_sticker_add_command,
    on_sticker_set_command,
    on_sticker_rm_command,
    on_sticker_get_command,
)


async def main() -> None:
    sessions_folder = Path("data/sessions")
    session_files = list(sessions_folder.glob("*.session"))

    apps = []
    for session_file in session_files:
        app = Client(str(session_file.stem), workdir="data/sessions/")
        app.add_handler(
            MessageHandler(
                callback=on_sticker_add_command,
                filters=pyrogram.filters.create(
                    sticker_filter.filter_on_sticker_add_command
                )
                & pyrogram.filters.me,
            )
        )

        app.add_handler(
            MessageHandler(
                callback=on_sticker_set_command,
                filters=pyrogram.filters.create(
                    sticker_filter.filter_on_sticker_set_command
                )
                & pyrogram.filters.me,
            )
        )

        app.add_handler(
            MessageHandler(
                callback=on_sticker_rm_command,
                filters=pyrogram.filters.create(
                    sticker_filter.filter_on_sticker_rm_command
                )
                & pyrogram.filters.me,
            )
        )

        app.add_handler(
            MessageHandler(
                callback=on_sticker_get_command,
                filters=pyrogram.filters.create(
                    sticker_filter.filter_on_sticker_get_command
                )
                & pyrogram.filters.me,
            )
        )
        app.add_handler(
            MessageHandler(
                callback=on_command,
                filters=pyrogram.filters.create(
                    filter_pm_isbot_isself.check_pm_isbot_isself
                )
                & pyrogram.filters.create(
                    filter_in_commands_list.check_if_message_in_commands
                ),
            )
        )
        app.add_handler(
            MessageHandler(
                callback=on_message,
                filters=pyrogram.filters.create(
                    filter_pm_isbot_isself.check_pm_isbot_isself
                ),
            )
        )
        apps.append(app)

    await compose(apps)


if __name__ == "__main__":
    uvloop.install()
    asyncio.run(main())
