import asyncio

from pathlib import Path
from pyrogram.client import Client


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
