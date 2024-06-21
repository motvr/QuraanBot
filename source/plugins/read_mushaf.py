from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup as Markup,
    InlineKeyboardButton as Button,
    InputMediaPhoto,
)
from source import hafs_db
from source.helpers import suras_keyboard1, suras_keyboard2


@Client.on_callback_query(filters.regex(r"^(suras)"))
async def get_suras_page(_: Client, callback: CallbackQuery) -> None:
    data: list = callback.data.split()
    if data[1] == "1":
        text: str = (
            "- حسنا عزيزي يمكنك اختيار السورة التي تريد من خلال الفهرس المرتب التالي :"
        )
        markup: Markup = suras_keyboard1
        await callback.message.edit_text(text, reply_markup=markup)
    else:
        text: str = None
        markup: Markup = suras_keyboard2
        await callback.message.edit_reply_markup(reply_markup=markup)


@Client.on_callback_query(filters.regex(r"^(del)$"))
async def delete(_: Client, callback: CallbackQuery) -> None:
    await callback.answer("- تم الحذف")
    await callback.message.delete()
