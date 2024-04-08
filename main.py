import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
import logging
from handlers import common, tariff_choice

# Асинхронная функция main, содержащая логику бота
async def main():
    # Включение логирования для отслеживания действий бота
    logging.basicConfig(level=logging.INFO)

    # Создание объекта бота с использованием токена из файла config
    bot = Bot(token=config.token)

    # Создание диспетчера для обработки входящих сообщений
    dp = Dispatcher()

    # Добавление роутеров из модулей common и career_choice для обработки команд
    dp.include_router(tariff_choice.router)
    dp.include_router(common.router)

    # Запуск опроса сервера Telegram для получения новых сообщений
    await dp.start_polling(bot)

# Точка входа в программу, запускающая функцию main
if __name__ == '__main__':
    asyncio.run(main())
