from yoomoney import Client
from yoomoney import Quickpay
from aiogram.dispatcher.filters import Command
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from sys import exit
from replit import db

bot_token = "5116068253:AAFkw9zZTPm-0LrLA82B7klhl9yF6xXiJxU"
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)


# phone_chat_id =
# text =

gift_purse = 0

# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Authorize(
#       client_id="1A206994431D361204927B957303CBF2EC89ACE4DAFE12D35071E745401D3B54",
#       redirect_uri="https://t.me/adbot_ch_bot?code=659419",
#       scope=["account-info",
#              "operation-history",
#              "operation-details",
#              "incoming-transfers",
#              "payment-p2p",
#              "payment-shop",
#              ]
#       )

token = "4100117410709216.91A707B6031CEB98B302232BE7214D11849168D33AC6D3F305BE12190B0D6BF638D08FEBA8F1258BB87" \
        "65231AAED09DFA9B094EBEFE4D72AA930FAFFF872D6B87ECA99CB1AACB497D5AA1690B67685D72AB19678938F25374EB4F38" \
        "85E4692E2A907E1AB60C8C65BC3C15649D4FB56BF4D6F1A903239DD95531B7E005AD6D959"


client = Client(token)
user = client.account_info()
print()
print("Account number:", user.account)
print("Account balance:", user.balance)
# print("Account currency code in ISO 4217 format:", user.currency)
print("Account status:", user.account_status)
print("Account type:", user.account_type)
print()
print()
# print("Extended balance information:")
# for pair in vars(user.balance_details):
#     print("\t-->", pair, ":", vars(user.balance_details).get(pair))
# print("Information about linked bank cards:")
# cards = user.cards_linked
#  if len(cards) != 0:
#     for card in cards:
#         print(card.pan_fragment, " - ", card.type)
# else:
#     print("No card is linked to the account")


cost = "20р"


def get_startkeyboard():
    buttons = [
        types.InlineKeyboardButton(text="Мой канал с мемчиками.",
                                   callback_data="lh_mem"),
        types.InlineKeyboardButton(text="Отзывы и предложения.",
                                   callback_data="local_chat"),
        types.InlineKeyboardButton(text="Пожертвовать деньги на развитие.",
                                   callback_data="pl_pay"),
        types.InlineKeyboardButton(text="Оформить новую рекламу.",
                                   callback_data="new_ad")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard

def get_vip():
    buttons = [
        types.InlineKeyboardButton(text="Бесплатный проход",
                                   callback_data="send_ad")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def vip_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Отчет о рекламах", "Проверка работы бота"]
    keyboard.add(*buttons)
    return keyboard


def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None



@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
  await message.answer(
        "Приветствую вас в боте по продаже рекламы, и установки ее во многих каналах"
        " одновременно!\nКаналы с 1к подписчиков.",
        reply_markup=get_startkeyboard())
  unique_code = extract_unique_code(message.text)
  if unique_code:
    db["new_ref_us"] = message.from_user.id, unique_code
  else:
    pass
  if message.from_user.id == 900645059:
     await message.answer("👑Ты в VIP-ке!", reply_markup=vip_menu())
     await message.answer(".", reply_markup=get_vip())
     print()
     print(f"Владелец вошел в приватку!")



@dp.message_handler(Text(equals="Отчет о рекламах"))
async def db_open(message: types.Message):
  value = db["key"]
  refers = db["new_ref_us"]
  await message.answer(refers)
  await message.answer(value, reply_markup=get_startkeyboard())


@dp.message_handler(Text(equals="Проверка работы бота"))
async def debug(message: types.Message):

    await message.answer("Проверка произведена!", reply_markup=get_startkeyboard())
  

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

@dp.message_handler(Text(equals="Проверка работы бота"))
async def cmd_debug(message: types.Message):
  value = db["key"]
  print(value)



@dp.callback_query_handler(text="new_ad")
async def new_ad(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Реклама в 1 канал(200+подписчиков)",
                                   callback_data="1_ch_ad"),
        types.InlineKeyboardButton(text="Реклама в 2 канала(500+подписчиков)",
                                   callback_data="2_ch_ad"),
        types.InlineKeyboardButton(text="Реклама в 5 каналов(1k+подписчиков)",
                                   callback_data="5_ch_ad")
    ]
    keyboard_ad = types.InlineKeyboardMarkup(row_width=1)
    keyboard_ad.add(*buttons)
    await call.message.answer("Выберете тип:", reply_markup=keyboard_ad)


@dp.callback_query_handler(text="1_ch_ad")
async def new_ad1(call: types.CallbackQuery):
    await call.message.answer("Напишите свою рекламу начиная с /ad1")


@dp.message_handler(commands="ad1")
async def text_added1(message: types.Message):
    usersmessage = message.get_args()
    buttons = [ types.InlineKeyboardButton(text="Устраивает.",
                                   callback_data="k_oplate1"), types.InlineKeyboardButton(text="Давайте заново!",
                                   callback_data="1_ch_ad") ]
    keyboard_allok = types.InlineKeyboardMarkup(row_width=1)
    keyboard_allok.add(*buttons)
#  msg_text = 
    await message.reply("Вас устраивает такая публикация:\n\n" + usersmessage + "?", reply_markup=keyboard_allok)
    db["ad_text"] = usersmessage


@dp.callback_query_handler(text="k_oplate1")
async def oplata1(call: types.CallbackQuery):
    quickpay = Quickpay(receiver="4100117410709216",
                        quickpay_form="shop",
                        targets="Оплата за рекламу",
                        paymentType="SB",
                        sum=20,
                        label= call.from_user.id)
    print()
    print("Кто-то платит 20р")
    print()

    buttons = [
        types.InlineKeyboardButton(text="Оплатить тута!",
                                   url=quickpay.redirected_url),
             types.InlineKeyboardButton(text="Проверить оплату", callback_data = "open_hist")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    
    await call.message.answer(
        f"Перейдем к оплате:\nС вас взыскано по тарифу:" + cost,
        reply_markup=keyboard)


@dp.callback_query_handler(text="open_hist")
async def ope_hist(call: types.CallbackQuery):
  buttons = [
        types.InlineKeyboardButton(text="Отправить✉.",
                                   callback_data="send_ad")
    ]
  keyboard_send = types.InlineKeyboardMarkup(row_width=1)
  keyboard_send.add(*buttons)
  history = client.operation_history(label=call.from_user.id)
  print("List of operations:")
  print("Next page starts with: ", history.next_record)
  for operation in history.operations:
    print()
    print("Operation:", operation.operation_id)
    print("\tStatus     -->", operation.status)
    print("\tDatetime   -->", operation.datetime)
    print("\tTitle      -->", operation.title)
    print("\tPattern id -->", operation.pattern_id)
    print("\tDirection  -->", operation.direction)
    print("\tAmount     -->", operation.amount)
    print("\tLabel      -->", operation.label)
    print("\tType       -->", operation.type)
    print()
    print()
    print("Статус операции: " + operation.status)
    if operation.status == "success":
     await call.message.answer("Вы успешно оплатили заказ!\nМожем приступать к отправке Вашей рекламы", reply_markup=keyboard_send)
  if history.operations == []:
    await call.message.answer("Вы не оплатили заказ!\nПожалуйста оплатите заказ еще раз!")
    print()
    print("Оплата сорвалась!")


@dp.callback_query_handler(text="2_ch_ad")
async def new_ad_2(call: types.CallbackQuery):
    await call.message.answer("Напишите свою рекламу начиная с /ad2")




@dp.message_handler(commands="ad2")
async def text_added2(message: types.Message):
    usersmessage = message.get_args()
    buttons = [
        types.InlineKeyboardButton(text="Устраивает.",
                                   callback_data="k_oplate2"),
        types.InlineKeyboardButton(text="Давайте заново!",
                                   callback_data="2_ch_ad")
    ]
    keyboard_allok = types.InlineKeyboardMarkup(row_width=1)
    keyboard_allok.add(*buttons)
    await message.reply("Вас устраивает такая публикация:\n\n" + usersmessage + "?",
                        reply_markup=keyboard_allok)
    db["ad_text"] = usersmessage


@dp.callback_query_handler(text="k_oplate2")
async def oplata2(call: types.CallbackQuery):
    quickpay = Quickpay(receiver="44100117410709216",
                        quickpay_form="shop",
                        targets="Оплата за рекламу",
                        paymentType="SB",
                        sum=50,
                        label= call.from_user.id)
    print()
    print("Кто-то платит 50р")
    print()

    buttons = [
        types.InlineKeyboardButton(text="Оплатить тута!",
                                   url=quickpay.redirected_url),
             types.InlineKeyboardButton(text="Проверить оплату", callback_data = "open_hist")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    global cost
    await call.message.answer(
        f"Перейдем к оплате:\nС вас взыскано по тарифу: 50р",
        reply_markup=keyboard)
    

@dp.callback_query_handler(text="5_ch_ad")
async def new_ad5(call: types.CallbackQuery):
    await call.message.answer("Напишите свою рекламу начиная с /ad5")


@dp.message_handler(commands="ad5")
async def text_added5(message: types.Message):
    usersmessage = message.get_args()
    buttons = [
        types.InlineKeyboardButton(text="Устраивает.",
                                   callback_data="k_oplate5"),
        types.InlineKeyboardButton(text="Давайте заново!",
                                   callback_data="5_ch_ad")
    ]
    keyboard_allok = types.InlineKeyboardMarkup(row_width=1)
    keyboard_allok.add(*buttons)
    await message.reply("Вас устраивает такая публикация:\n\n" + usersmessage + "?",
                        reply_markup=keyboard_allok)
    db["ad_text"] = usersmessage

@dp.callback_query_handler(text="k_oplate5")
async def oplata5(call: types.CallbackQuery):
    quickpay = Quickpay(receiver="4100117410709216",
                        quickpay_form="shop",
                        targets="Оплата за рекламу",
                        paymentType="SB",
                        sum=100,
                        label= call.from_user.id)
    print()
    print("Кто-то платит 100р")
    print()

    buttons = [
        types.InlineKeyboardButton(text="Оплатить тута!",
                                   url=quickpay.redirected_url),
             types.InlineKeyboardButton(text="Проверить оплату", callback_data = "open_hist")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    global cost
    await call.message.answer(
        f"Перейдем к оплате:\nС вас взыскано по тарифу: 100р",
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


@dp.callback_query_handler(text="pl_pay")
async def oplata(call: types.CallbackQuery):
    quickpay = Quickpay(receiver="4100117410709216",
                        quickpay_form="shop",
                        targets="Пожертвование на новые проекты",
                        paymentType="SB",
                        sum=50,
                        label= call.from_user.id)
    print(quickpay.base_url)
    print(quickpay.redirected_url)

    buttons = [
        types.InlineKeyboardButton(text="Оплатить здесь!",
                                   url=quickpay.redirected_url),
             types.InlineKeyboardButton(text="Проверить оплату", callback_data = "open_hist")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    global cost
    await call.message.answer(
        f"Спасибо большое за посильную помощь!\nПерейдем к оплате:\nНажмите на кнопку, что бы сделать пожертвование: 50р",
        reply_markup=keyboard)


@dp.callback_query_handler(text="send_ad")
async def otpravka(call: types.CallbackQuery):
  value = db["ad_text"]
  await call.message.answer("Отправляем...")
  await bot.send_message(1440259230, "Новая реклама:\n\n" + value)
  await bot.send_message(5037678159, "Новая реклама:\n\n" + value)
  await bot.send_message(1687605952, "Новая реклама:\n\n" + value)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
