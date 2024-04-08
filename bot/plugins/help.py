from bot import SUPPORT_CHAT_LINK
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import Messages as tr

@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=tr.START_MSG.format(message.from_user.mention),
    )

@app.on_message(filters.private & filters.command("help"))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=tr.HELP_MSG[1],
        reply_markup=InlineKeyboardMarkup(await map(1)),
        reply_to_message_id=message.message_id,
    )

@app.on_callback_query(filters.regex("^help_"))
async def help_answer(client, callback_query):
    msg = int(callback_query.data.split("_")[1])
    await callback_query.edit_message_text(
        text=tr.HELP_MSG[msg],
        reply_markup=InlineKeyboardMarkup(await map(msg)),
    )

async def map(pos):
    if pos == 1:
        buttons = [[InlineKeyboardButton(text='-->', callback_data=f"help_{pos + 1}")]]
    elif pos == len(tr.HELP_MSG) - 1:
        buttons = [
            [
                InlineKeyboardButton(text='Support Chat', url=SUPPORT_CHAT_LINK),
                InlineKeyboardButton(text='Feature Request', url="https://github.com/viperadnan-git/google-drive-telegram-bot/issues/new")
            ],
            [InlineKeyboardButton(text='<--', callback_data=f"help_{pos - 1}")]
        ]
    else:
        buttons = [
            [
                InlineKeyboardButton(text='<--', callback_data=f"help_{pos - 1}"),
                InlineKeyboardButton(text='-->', callback_data=f"help_{pos + 1}")
            ]
        ]
    return buttons
