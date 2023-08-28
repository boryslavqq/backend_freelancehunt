import asyncio
import logging
from typing import Callable

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker

import handlers
from config import config
from database.models import Base
from middlewares.database import DatabaseMiddleware
from middlewares.logging import logger


async def main():
    logger.info("Bot started!")
    logger.debug("Debug mode is on!")

    engine: AsyncEngine = create_async_engine(config.DATABASE_URI, echo=False, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_sessionmaker: Callable = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML, validate_token=True)

    dp = Dispatcher(bot)

    dp.middleware.setup(DatabaseMiddleware(async_sessionmaker))

    handlers.setup(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        session = await bot.get_session()
        await session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
