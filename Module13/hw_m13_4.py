from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = "..."
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Привет! Я бот, помогающий твоему здоровью.')


@dp.message_handler(text=['Calories'])
async def set_age(message: types.Message):
    await message.reply('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_height(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.reply('Введите свой рост:')
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(height=int(message.text))
    await message.reply('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data['age']
    height = data['height']
    weight = data['weight']

    calories = 10 * weight + 6.25 * height - 5 * age + 5

    await message.reply(f'Ваша норма калорий: {calories:.2f}')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
