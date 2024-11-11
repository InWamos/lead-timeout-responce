import asyncio
import pyrogram
import uvloop

from pathlib import Path
from filters import filter_pm_isbot_isself, filter_in_commands_list
from pyrogram.sync import compose
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from handlers.timeout_responce import on_message
from handlers.command_responce import on_command


async def main() -> None:
    sessions_folder = Path("data/sessions")
    session_files = list(sessions_folder.glob("*.session"))

    apps = []
    for session_file in session_files:
        app = Client(str(session_file.stem), workdir="data/sessions/")
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
