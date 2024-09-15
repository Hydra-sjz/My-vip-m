from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VIPMUSIC import app as Bot

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

text_rep = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Rᴇᴘᴏ:

Dᴄʀɪᴘᴛɪᴏɴ:
Dᴏᴡɴᴏᴀᴅ ᴀɴᴅ ʀᴇᴛʀɪᴇᴠᴇ ғɪᴇs ғʀᴏᴍ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ.

Usᴀɢᴇ:
々 /dlrepo [Rᴇᴘᴏ_URL]

Dᴇᴛᴀɪs:
- Cᴏɴᴇs ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ.
- Cʀᴇᴀᴛᴇs ᴀ ᴢɪᴘ ғɪᴇ ᴏғ ᴛʜᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ.
- Sᴇɴᴅs ᴛʜᴇ ᴢɪᴘ ғɪᴇ ʙᴀᴄᴋ ᴀs ᴀ ᴅᴏᴄᴜᴍᴇɴᴛ.
- Iғ ᴛʜᴇ ᴅᴏᴡɴᴏᴀᴅ ғᴀɪs, ᴀɴ ᴇʀʀᴏʀ ᴍᴇssᴀɢᴇ ᴡɪ ʙᴇ ᴅɪsᴘᴀʏᴇᴅ.

Exᴀᴍᴘᴇs:
- /dlrepo ʜᴛᴛᴘs://ɢɪᴛʜᴜʙ.ᴄᴏᴍ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘᴏsɪᴛᴏʀʏ
"""
buttons_rep = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^rep$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_rep,
        reply_markup=InlineKeyboardMarkup(buttons_rep),
        disable_web_page_preview=True,
    )

text_rpd = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Speed:

Speed Control

This module allows administrators to control the playback speed of audio files in the group.

Commands:
々 /cspeed: Speed up the playback.
々 /speed: Speed up the playback.
々 /cslow: Slow down the playback.
々 /slow: Slow down the playback.
々 /playback: Control the playback speed.
々 /cplayback: Control the playback speed.

Note:
- Only administrators can use these commands.
"""
buttons_rpd = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^rpd$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_rpd,
        reply_markup=InlineKeyboardMarkup(buttons_rpd),
        disable_web_page_preview=True,
    )

text_tag = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Sɪɴɢʟᴇ Tᴀɢ:

Tᴀɢ A Usᴇʀs Oɴᴇ Bʏ Oɴᴇ

Tʜɪs ᴍᴏᴅᴜᴇ ᴀᴏᴡs ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ ᴏʀ VC.

Cᴏᴍᴍᴀɴᴅs:
- /tag: Mᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ᴏɴᴇ ʙʏ ᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
- /vctag: Mᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ᴏɴᴇ ʙʏ ᴏɴᴇ ғᴏʀ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

Tᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ:
- /stoptag: Sᴛᴏᴘ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
- /stopvctag: Sᴛᴏᴘ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

Nᴏᴛᴇ:
- Oɴʏ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs.
- Usᴇ /sᴛᴏᴘᴛᴀɢᴀ ᴏʀ /sᴛᴏᴘᴠᴄᴛᴀɢ ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ. 
"""
buttons_tag = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^tag$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_tag,
        reply_markup=InlineKeyboardMarkup(buttons_tag),
        disable_web_page_preview=True,
    )
