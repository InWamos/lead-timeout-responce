import asyncio

from pathlib import Path
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from handlers.timeout_responce import on_message
from handlers.command_responce import on_command


async def main() -> None:
    sessions_folder = Path("data/sessions")
    session_files = list(sessions_folder.glob("*.session"))

    for session_file in session_files:
        app = Client(str(session_file.stem), workdir="data/sessions/")
        try:
            await app.start()
        except:
            print(str(session_file) + " Broken session")


if __name__ == "__main__":
    asyncio.run(main())
