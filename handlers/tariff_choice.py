from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.tariff_keyboards import make_row_keyboard

# Создание экземпляра маршрутизатора для обработки сообщений
router = Router()

# Список доступных тарифов
available_tariff_names = ["Начальный уровень (1500 р.)", "Продвинутый уровень (2500 р.)", "Профессиональный уровень (5000 р.)"]
# Список доступных опций
available_options = ["С обучением", "Без обучения"]

# Определение класса состояний для выбора Тарифа и Опций
class ChoiceTariffNames(StatesGroup):
    choice_tariff_names = State()  # Состояние для выбора тарифа
    choice_options = State()  # Состояние для выбора опций

# Хэндлер на команду /tariff, начинает процесс выбора тарифа
@router.message(Command('tariff'))
@router.message(Command('Выбор тарифа'))
@router.message(F.text.lower() == 'выбор тарифа')
@router.message(Command('Тариф'))
@router.message(F.text.lower() == 'тариф')
async def cmd_tariff(message: types.Message, state: FSMContext):
    # Приветствие пользователя и запрос на выбор тарифа
    name = message.chat.first_name
    await message.answer(f'Привет, {name}, выбери свой тариф', reply_markup=make_row_keyboard(available_tariff_names))

    # Переход в состояние выбора тарифа
    await state.set_state(ChoiceTariffNames.choice_tariff_names)

# Хэндлер для выбранного тарифа
@router.message(ChoiceTariffNames.choice_tariff_names, F.text.in_(available_tariff_names))
async def tariff (message: types.Message, state: FSMContext):
    # Сохранение выбранного тарифа и запрос на выбор опций
    await state.update_data(chosen_tariff=message.text.lower())
    await message.answer(f'Спасибо, Теперь выбери дополнительную опцию', reply_markup=make_row_keyboard(available_options))

    # Переход в состояние выбора опций
    await state.set_state(ChoiceTariffNames.choice_options)

# Хэндлер для некорректно выбранного тарифа
@router.message(ChoiceTariffNames.choice_tariff_names)
async def tariff_chosen_incorrectly(message: types.Message):
    # Уведомление о некорректном выборе и новый запрос на выбор тарифа
    await message.answer(f'Я не знаю такого тарифа', reply_markup=make_row_keyboard(available_tariff_names))

# Хэндлер для выбранной опции
@router.message(ChoiceTariffNames.choice_options, F.text.in_(available_options))
async def tariff_chosen(message: types.Message, state: FSMContext):
    # Получение данных о выбранном тарифе и уведомление пользователя
    user_data = await state.get_data()
    await message.answer(f'Ваш Тариф - {user_data.get("chosen_tariff")}. Дополнительная опция - {message.text.lower()}',reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f'В течении 5 минут вам придет сообщение с ссылкой на оплату тарифа и регистрационные данные.')
    await message.answer(f'Спасибо, что выбрали нас \u2764\ufe0f')

    # Очистка состояния
    await state.clear()

# Хэндлер для некорректно выбранной опции
@router.message(ChoiceTariffNames.choice_options)
async def options_chosen_incorrectly(message: types.Message):
    # Уведомление о некорректном выборе и новый запрос на выбор опции
    await message.answer(f'Я не знаю таких дополнительных опций', reply_markup=make_row_keyboard(available_options))
