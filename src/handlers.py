from aiogram.filters.command import Command
from aiogram import F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram import Router
from aiogram.utils.deep_linking import create_start_link
import src.keyboards as kb
import src.db as db
import base64


router = Router()
CHANEL_NAME = "@test_chanel_46"


async def is_referral(message):
    encoded_string = message.text
    encoded_string = encoded_string.replace("/start ", "")
    print(encoded_string)
    if len(encoded_string) > 7:
        if len(encoded_string)%4 != 0:
            encoded_string += "=" * (4 - len(encoded_string)%4)
        decoded_id = base64.b64decode(encoded_string).decode()
        
        if decoded_id != str(message.from_user.id):
            db.add_invitation(decoded_id)
            db.add_tokens(decoded_id, 200)
            return True
    
    return False


@router.message(F.text, Command("start"))
async def start_loop(message: Message, bot: Bot):
    await message.answer_photo(caption=f"Привет, @{message.from_user.username}!\n"
        "Подпишитесь на наш канал и получите 200 токенов SHEIKH!🤑", photo=FSInputFile("./img/welcome_image.jpg"), reply_markup=kb.subscription_keyboard)
    if not db.is_old(message.from_user.id):
        user_referral_link = await create_start_link(bot, str(message.from_user.id), encode=True)
        db.add_new_user(message.from_user.id, message.from_user.username, user_referral_link)
        await is_referral(message)


@router.callback_query(F.data == "check_subscription")
async def send_random_value(callback: CallbackQuery, bot: Bot):
    user_channel_status = await bot.get_chat_member(chat_id=f"{CHANEL_NAME}", user_id=callback.from_user.id)
    if user_channel_status.status != 'left':
        await callback.answer("Подписка обработана!")
        db.change_subscribed(callback.from_user.id)
        if not db.if_subscribed(callback.from_user.id):
            db.add_tokens(callback.from_user.id, 200)
            db.change_subscribed_bonus(callback.from_user.id)
        await callback.message.edit_caption(caption = "Выберите одну из опций:")
        await callback.message.edit_reply_markup(reply_markup = kb.main_keyboard)
    else:
        await callback.answer("Пожалуйста, подпишитесь наш канал")
        

@router.callback_query(F.data == "balance")
async def send_random_value(callback: CallbackQuery, bot: Bot):
    user_balance = db.get_balance(callback.from_user.id)
    await callback.message.edit_caption(caption = f"Ваш текущий баланс: {user_balance} SHEIKH")
    await callback.message.edit_reply_markup(reply_markup = kb.main_keyboard)


@router.callback_query(F.data == "withdraw")
async def send_random_value(callback: CallbackQuery, bot: Bot):
    await callback.message.edit_caption(caption = "Для вывода средств напишите админу @SHEIKH_support1")
    await callback.message.edit_reply_markup(reply_markup = kb.main_keyboard)


@router.callback_query(F.data == "invite_friend")
async def send_random_value(callback: CallbackQuery, bot: Bot):
    user_referral_link = await create_start_link(bot, str(callback.from_user.id), encode=True)
    await callback.message.edit_caption(caption = "Ваша реферальная ссылка:\n"
                                    f"{user_referral_link}\n\n"
                                    "Скопируйте ссылку и поделитесь со своим другом. За каждого приведенного пользователя вы получите 200 SHEIKH 💰.")
    await callback.message.edit_reply_markup(reply_markup = kb.main_keyboard)