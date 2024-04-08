from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
from keyboards.keyboards import kb1, kb2


router = Router()

# Хэндлер на команду /start
@router.message(Command('start'))
@router.message(Command('Старт'))
@router.message(F.text.lower() == 'старт')
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет {name}', reply_markup=kb1 )

# Хэндлер на команду /info
@router.message(Command('info'))
@router.message(Command('Информация'))
@router.message(F.text.lower() == 'информация')
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'{name}, c помощью данного чат бота вы можете выбрать тариф или обратиться в службу технической поддержки.')

# Хэндлер на команду /stop
@router.message(Command('stop'))
@router.message(Command('Закрыть'))
@router.message(F.text.lower() == 'закрыть')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'До свидания, {name}')

# Хэндлер на команду /fox и альтернативные варианты вызова команды
@router.message(Command('tech'))
@router.message(Command('техническая поддержка'))
@router.message(F.text.lower() == 'техническая поддержка')
async def cmd_tech(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Зову техническую поддержку, подождите {name}')


# Хэндлер на текстовые сообщения, включающий простую реакцию на определенные слова
@router.message(F.text)
async def msg_echo(message: types.Message):
   msg_user = message.text.lower()
   name = message.chat.first_name
   if 'привет' in msg_user:
        await message.answer(f'Привет , {name}, для начала роботы, напишите /start или старт')
   elif 'пока' in msg_user:
        await message.answer(f'Пока , {name}')
   elif 'ты кто' in msg_user:
        await message.answer(f'Я чат бот Synology , {name}')
   else:
        await message.answer(f'я не знаю такого слова, {name}, если хотите начать работу, напишите /start или старт')
