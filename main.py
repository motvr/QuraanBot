from source import app
from config import db_path
from os.path import exists
from source.helpers import write
from asyncio import get_event_loop
from pyrogram import idle


async def main() -> None:
    if not exists(db_path):
        write(db_path, {})
    await app.start()
    await idle()
    await app.stop()


if __name__ == "__main__":
    get_event_loop().run_until_complete(main())
