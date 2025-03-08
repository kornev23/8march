import logging
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Вставь сюда свой токен от BotFather
TOKEN = "7560547647:AAGAVPMAxtQzEsYCxh65DJ3g9w_E10wXyD8"

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Список предсказаний
predictions = [
    "Сегодня ты получишь столько комплиментов, что можно будет составить книгу! 📖💖",
    "Грядет день, полный радости и весеннего настроения. Готовься сиять! ✨",
    "Вокруг тебя сегодня будет кружиться целая буря цветов и поздравлений! 🌸💐",
    "Этот день подарит тебе неожиданный сюрприз. Что-то сладкое уже в пути! 🍫",
    "Поздравления будут сыпаться, как весенний дождь! ☔🌷",
    "Будь готова принимать внимание и заботу — сегодня ты королева! 👑",
    "Настоящая магия 8 Марта в том, что ты сияешь ярче солнца! ☀️",
    "Сегодня можно не думать о делах — только наслаждаться моментом! 🎉",
    "Этот день будет полон смеха, улыбок и маленьких радостей. 😍",
    "Будет столько цветов, что можно открыть собственный магазин! 🌹🏪",
    "Кто-то сегодня обязательно сделает тебе день! Ожидай сюрприз! 🎁",
    "Даже если забудут подарки, то точно не забудут обнять и сказать теплые слова! 🤗",
    "Сегодня у тебя иммунитет от всех забот — только счастье и весна в душе! 🌞",
    "Ты — главное украшение этого дня, а не цветы! 💃",
    "День пройдет так хорошо, что захочется праздновать всю неделю! 🍾",
    "Сегодня можно баловать себя без угрызений совести. Шоколад? ДА! 🍩",
    "Звезды предсказывают... стоп! Они просто сияют в твою честь! 🌟",
    "Сегодня никто не сможет устоять перед твоей харизмой и очарованием! 💘",
    "Твой 8 Марта будет идеальным — просто потому, что ты этого заслуживаешь! 😌",
    "Праздник пройдет весело и легко, как весенний ветер. Наслаждайся моментом! 🌬️",
]

# Клавиатура с кнопкой предсказания
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("🔮 Получить предсказание!"))

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer("🌸 Приветствую тебя! Давай погадаем, как пройдет твой день?\n\nНажми на кнопку ниже, чтобы получить предсказание!", reply_markup=keyboard)

# Обработчик кнопки предсказания
@dp.message_handler(lambda message: message.text == "🔮 Получить предсказание!")
async def send_prediction(message: types.Message):
    prediction = random.choice(predictions)
    await message.answer(prediction)
    await asyncio.sleep(2)
    await message.answer("А теперь держи поздравление! 🎁")
    with open("flower_8_march.png", "rb") as photo:
        await bot.send_photo(message.chat.id, photo, caption="С 8 Марта! 🌸💖")

# Запуск бота
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
