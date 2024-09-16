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
々 /tag: Mᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ᴏɴᴇ ʙʏ ᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
々 /vctag: Mᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ᴏɴᴇ ʙʏ ᴏɴᴇ ғᴏʀ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

Tᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ:
々 /stoptag: Sᴛᴏᴘ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
々 /stopvctag: Sᴛᴏᴘ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

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


text_sl = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Sʟᴀᴘ:

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
々 /slap: Sʟᴀᴘs sᴏᴍᴇᴏɴᴇ. Iғ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ, sʟᴀᴘs ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ.
"""
buttons_sl = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^sl$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_sl,
        reply_markup=InlineKeyboardMarkup(buttons_sl),
        disable_web_page_preview=True,
    )


text_stk = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Sᴛɪᴄᴋᴇʀ:

COMMANDS:

々 /stickerid - ɢᴇᴛs ᴛʜᴇ ғɪʟᴇ ɪᴅ ᴏғ ᴀɴʏ ʀᴇᴘʟɪᴇᴅ sᴛɪᴄᴋᴇʀ.
々 /getsticker - ɢᴇᴛs ᴛʜᴇ ɪᴍᴀɢᴇ ᴏғ ᴀɴʏ ʀᴇᴘʟɪᴇᴅ sᴛɪᴄᴋᴇʀ.
々 /kang - ᴋᴀɴɢs ᴀɴʏ sᴛɪᴄᴋᴇʀ ɪɴ ᴛʜᴇ ʏᴏᴜ ᴘᴀᴄᴋ

INFO:

- ᴛʜɪs ʙᴏᴛ ᴀʟʟᴏᴡs ᴜsᴇʀs ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇ ɪᴅ ᴏʀ ᴛʜᴇ ɪᴍᴀɢᴇ ᴏғ ᴀɴʏ sᴛɪᴄᴋᴇʀ ᴛʜᴀᴛ ɪs ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ, ᴀɴᴅ ᴀʟsᴏ ᴀʟʟᴏᴡs ᴜsᴇʀs ᴛᴏ ᴋᴀɴɢ ᴀɴʏ sᴛɪᴄᴋᴇʀ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ ᴀɴᴅ ᴀᴅᴅ ɪᴛ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ.
"""
buttons_stk = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^stk$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_stk,
        reply_markup=InlineKeyboardMarkup(buttons_stk),
        disable_web_page_preview=True,
    )


text_trt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Tʀᴜᴛʜ:

ᴛʀᴜᴛʜ ᴏʀ ᴅᴀʀᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs

ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴘʟᴀʏ ᴛʀᴜᴛʜ ᴏʀ ᴅᴀʀᴇ:

々 /truth: ɢᴇᴛ ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ ǫᴜᴇsᴛɪᴏɴ. ᴀɴsᴡᴇʀ ʜᴏɴᴇsᴛʟʏ!
々 /dare: ɢᴇᴛ ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ ᴄʜᴀʟʟᴇɴɢᴇ. ᴄᴏᴍᴘʟᴇᴛᴇ ɪᴛ ɪғ ʏᴏᴜ ᴅᴀʀᴇ!

ᴇxᴀᴍᴘʟᴇs:
々 /truth: "ᴡʜᴀᴛ ɪs ʏᴏᴜʀ ᴍᴏsᴛ ᴇᴍʙᴀʀʀᴀssɪɴɢ ᴍᴏᴍᴇɴᴛ?"
々 /dare: "ᴅᴏ 10 ᴘᴜsʜ-ᴜᴘs."

ɴᴏᴛᴇ:
ɪғ ʏᴏᴜ ᴇɴᴄᴏᴜɴᴛᴇʀ ᴀɴʏ ɪssᴜᴇs ᴡɪᴛʜ ғᴇᴛᴄʜɪɴɢ ǫᴜᴇsᴛɪᴏɴs, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.
"""
buttons_trt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^trt$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_trt,
        reply_markup=InlineKeyboardMarkup(buttons_trt),
        disable_web_page_preview=True,
    )


text_tgl = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Tᴀɢᴀʟʟ:


@all ᴏʀ /all | /tagall ᴏʀ  @tagall | /mentionall ᴏʀ  @mentionall [ᴛᴇxᴛ] ᴏʀ [ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ] ᴛᴏ ᴛᴀɢ ᴀʟʟ ᴜsᴇʀ's ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴛ ʙᴏᴛ

々 /admins | @admins | /report [ᴛᴇxᴛ] ᴏʀ [ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ] ᴛᴏ ᴛᴀɢ ᴀʟʟ ᴀᴅᴍɪɴ's ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

々 /cancel Oʀ @cancel |  /offmention Oʀ @offmention | /mentionoff Oʀ @mentionoff | /cancelall Oʀ @cancelall - ᴛᴏ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴀɴʏ ᴛᴀɢ ᴘʀᴏᴄᴇss

Nᴏᴛᴇ Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ᴏɴʟʏ ᴜsᴇ ᴛʜᴇ Aᴅᴍɪɴs ᴏғ Cʜᴀᴛ ᴀɴᴅ ᴍᴀᴋᴇ Sᴜʀᴇ Bᴏᴛ ᴀɴᴅ ᴀssɪsᴛᴀɴᴛ ɪs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ's
"""
buttons_tgl = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^tgl$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_tgl,
        reply_markup=InlineKeyboardMarkup(buttons_tgl),
        disable_web_page_preview=True,
    )


text_tgr = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Tᴇʟᴇɢʀᴀᴘʜ:

ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs

ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ:

々 /tgm: ᴜᴘʟᴏᴀᴅ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.
々 /tgt: sᴀᴍᴇ ᴀs /tgm.
々 /telegraph: sᴀᴍᴇ ᴀs /tgm.
々 /tl: sᴀᴍᴇ ᴀs /tgm.

ᴇxᴀᴍᴘʟᴇ:
- ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜ /tgm ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ.

ɴᴏᴛᴇ:
ʏᴏᴜ ᴍᴜsᴛ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ ғᴏʀ ᴛʜᴇ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴡᴏʀᴋ.
"""
buttons_tgr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^tgr$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_tgr,
        reply_markup=InlineKeyboardMarkup(buttons_tgr),
        disable_web_page_preview=True,
    )


text_tt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Tᴛs:

ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ

ᴜsᴇ ᴛʜᴇ /tts ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ɪɴᴛᴏ sᴘᴇᴇᴄʜ.

々 /tts <ᴛᴇxᴛ>: ᴄᴏɴᴠᴇʀᴛs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ ɪɴ ʜɪɴᴅɪ.

ᴇxᴀᴍᴘʟᴇ:
々 /tts Namaste Duniya

ɴᴏᴛᴇ:
ᴍᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴀғᴛᴇʀ ᴛʜᴇ /tts ᴄᴏᴍᴍᴀɴᴅ.
"""
buttons_tt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^tt$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_tt,
        reply_markup=InlineKeyboardMarkup(buttons_tt),
        disable_web_page_preview=True,
    )
