import asyncio
import uvloop

from pathlib import Path
from pyrogram.sync import compose
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from handlers.timeout_responce import on_message


async def main() -> None:
    sessions_folder = Path("data/sessions")
    session_files = list(sessions_folder.glob("*.session"))

    apps = []
    for session_file in session_files:
        app = Client(str(session_file.stem), workdir="data/sessions/")
        app.add_handler(MessageHandler(on_message))
        apps.append(app)

    await compose(apps)


if __name__ == "__main__":
    uvloop.install()
    asyncio.run(main())
