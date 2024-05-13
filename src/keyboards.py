from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


subscription_keyboard = InlineKeyboardMarkup(row_width = 1, inline_keyboard=[
    [InlineKeyboardButton(text="Подписаться", url="https://t.me/test_chanel_46")],
    [InlineKeyboardButton(text="Проверить подписку", callback_data="check_subscription")],
])

main_keyboard = InlineKeyboardMarkup(row_width = 1, inline_keyboard=[
    [InlineKeyboardButton(text="Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="Вывод средств", callback_data="withdraw")],
    [InlineKeyboardButton(text="Пригласить друга", callback_data="invite_friend")],
])
