
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VIPMUSIC import app as Bot




@Bot.on_callback_query(filters.regex("^qz$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_qz,
        reply_markup=InlineKeyboardMarkup(buttons_qz),
        disable_web_page_preview=True,
    )

text_quo = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Qᴜᴏᴛᴇ:

ǫᴜᴏᴛᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs

ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴄʀᴇᴀᴛᴇ ǫᴜᴏᴛᴇs ғʀᴏᴍ ᴍᴇssᴀɢᴇs:

々 /q: ᴄʀᴇᴀᴛᴇ ᴀ ǫᴜᴏᴛᴇ ғʀᴏᴍ ᴀ sɪɴɢʟᴇ ᴍᴇssᴀɢᴇ.
々 /r: ᴄʀᴇᴀᴛᴇ ᴀ ǫᴜᴏᴛᴇ ғʀᴏᴍ ᴀ sɪɴɢʟᴇ ᴍᴇssᴀɢᴇ ᴀɴᴅ ɪᴛs ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ.

ᴇxᴀᴍᴘʟᴇs:
々 /q : ᴄʀᴇᴀᴛᴇ ᴀ ǫᴜᴏᴛᴇ ғʀᴏᴍ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs.
々 /r : ᴄʀᴇᴀᴛᴇ ᴀ ǫᴜᴏᴛᴇ ғʀᴏᴍ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs.

ɴᴏᴛᴇ:
ᴍᴀᴋᴇ sᴜʀᴇ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ғᴏʀ ᴛʜᴇ ǫᴜᴏᴛᴇ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴡᴏʀᴋ.
"""
buttons_quo = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^quo$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_quo,
        reply_markup=InlineKeyboardMarkup(buttons_quo),
        disable_web_page_preview=True,
    )

text_rd = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Radio:

/radio - ᴛᴏ ᴘʟᴀʏ ʀᴀᴅɪᴏ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.
"""
buttons_rd = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^rd$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_rd,
        reply_markup=InlineKeyboardMarkup(buttons_rd),
        disable_web_page_preview=True,
    )

text_rsm = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Resume:

Resume

This module allows administrators to resume playback of the currently paused track.

Commands:
々 /resume: Resumes playback of the currently paused track for group.
々 /cresume: Resumes playback of the currently paused track for channel.

Note:
- Only administrators can use these commands.
"""
buttons_rsm = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^rsm$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_rsm,
        reply_markup=InlineKeyboardMarkup(buttons_rsm),
        disable_web_page_preview=True,
    )
