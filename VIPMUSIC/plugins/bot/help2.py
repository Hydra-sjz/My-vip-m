from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VIPMUSIC import app as Bot

# =============START_CMD====================
TEXT_ST = (
    "👋😄__Hello {},__\n\n"
    "<blockquote> Welcome to the 🎈𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡! This is a powerful⚡🌪️ bot for Telegram.</blockquote>\n\n"
    "**__Click help to know how to use me!__**"
)
BUTTONS_ST = [
    [
        InlineKeyboardButton("Channel 📢", url="https://t.me/XBOTS_X"),
        InlineKeyboardButton("Commands 📚", callback_data="help"),
        InlineKeyboardButton("About 💡", callback_data="abot"),
        InlineKeyboardButton("Sudo 👥", callback_data="sudo"),
    ],
    [InlineKeyboardButton("❌", callback_data="close")],
]


@Bot.on_callback_query(filters.regex("^home$"))
async def st_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_ST.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_ST),
        disable_web_page_preview=True,
    )


# ==============================MAIN_HELP_CMD====================
# ==============================MAIN_HELP_CMD====================
# ==============================MAIN_HELP_CMD====================
TEXT_HP = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP = [
    [
        InlineKeyboardButton("Acᴛɪᴠᴇ", callback_data="act"),
        InlineKeyboardButton("Adᴍɪɴ", callback_data="adm"),
        InlineKeyboardButton("Auᴛʜ", callback_data="aut"),
    ],
    [
        InlineKeyboardButton("Aᴅᴠɪᴄᴇ", callback_data="adv"),
        InlineKeyboardButton("Aᴘᴘʀᴏᴠᴇ", callback_data="apr"),
        InlineKeyboardButton("B-ʟɪsᴛ", callback_data="blt"),
    ],
    [
        InlineKeyboardButton("Boᴛ", callback_data="bt"),
        InlineKeyboardButton("Bᴀɴ", callback_data="bn"),
        InlineKeyboardButton("Bᴏᴛs", callback_data="bts"),
    ],
    [
        InlineKeyboardButton("Bᴏᴛsᴄʜᴋ", callback_data="bsk"),
        InlineKeyboardButton("Cʜᴀᴛ Ai", callback_data="ai"),
        InlineKeyboardButton("Deᴠ", callback_data="dv"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings5"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("❯", callback_data="settings2"),
    ],
]
@Bot.on_message(filters.command("help2") & filters.private)
async def hp_handler(bot, message):
    await message.reply_text(
        text=TEXT_HP.format(message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP),
        quote=True,
    )

@Bot.on_callback_query(filters.regex("^settings$"))
async def help_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_HP.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP),
        disable_web_page_preview=True,
    )


TEXT_HP2 = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP2 = [
    [
        InlineKeyboardButton("Filters", callback_data="flt"),
        InlineKeyboardButton("Fɪɢʟᴇᴛ", callback_data="fgl"),
        InlineKeyboardButton("Fᴀᴋᴇ", callback_data="fk"),
    ],
    [
        InlineKeyboardButton("Fᴏɴᴛ", callback_data="fon"),
        InlineKeyboardButton("Fᴜɴ", callback_data="fn"),
        InlineKeyboardButton("G-ᴄᴀsᴛ", callback_data="gt"),
    ],
    [
        InlineKeyboardButton("Gʀᴏᴜᴘ Lɪɴᴋ", callback_data="gl"),
        InlineKeyboardButton("Gᴀʟɪ", callback_data="gli"),
        InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="src"),
    ],
    [
        InlineKeyboardButton("Gᴏᴏᴅʙʏᴇ", callback_data="gdy"),
        InlineKeyboardButton("Hɪsᴛᴏʀʏ", callback_data="hsr"),
        InlineKeyboardButton("Hᴀsʜᴛᴀɢ", callback_data="htg"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("❯", callback_data="settings3"),
    ],
]
@Bot.on_callback_query(filters.regex("^settings2$"))
async def help_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_HP2.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP2),
        disable_web_page_preview=True,
    )


TEXT_HP3 = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP3 = [
    [
        InlineKeyboardButton("Acᴛɪᴠᴇ", callback_data="act"),
        InlineKeyboardButton("Adᴍɪɴ", callback_data="adm"),
        InlineKeyboardButton("Auᴛʜ", callback_data="aut"),
    ],
    [
        InlineKeyboardButton("Aᴅᴠɪᴄᴇ", callback_data="adv"),
        InlineKeyboardButton("Aᴘᴘʀᴏᴠᴇ", callback_data="apr"),
        InlineKeyboardButton("B-ʟɪsᴛ", callback_data="blt"),
    ],
    [
        InlineKeyboardButton("Boᴛ", callback_data="bt"),
        InlineKeyboardButton("Bᴀɴ", callback_data="bn"),
        InlineKeyboardButton("Bᴏᴛs", callback_data="bts"),
    ],
    [
        InlineKeyboardButton("Bᴏᴛsᴄʜᴋ", callback_data="bsk"),
        InlineKeyboardButton("Cʜᴀᴛ Ai", callback_data="ai"),
        InlineKeyboardButton("Deᴠ", callback_data="dv"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings2"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("❯", callback_data="settings4"),
    ],
]
@Bot.on_callback_query(filters.regex("^settings3$"))
async def help_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_HP3.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP3),
        disable_web_page_preview=True,
    )


TEXT_HP4 = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP4 = [
    [
        InlineKeyboardButton("Acᴛɪᴠᴇ", callback_data="act"),
        InlineKeyboardButton("Adᴍɪɴ", callback_data="adm"),
        InlineKeyboardButton("Auᴛʜ", callback_data="aut"),
    ],
    [
        InlineKeyboardButton("Aᴅᴠɪᴄᴇ", callback_data="adv"),
        InlineKeyboardButton("Aᴘᴘʀᴏᴠᴇ", callback_data="apr"),
        InlineKeyboardButton("B-ʟɪsᴛ", callback_data="blt"),
    ],
    [
        InlineKeyboardButton("Boᴛ", callback_data="bt"),
        InlineKeyboardButton("Bᴀɴ", callback_data="bn"),
        InlineKeyboardButton("Bᴏᴛs", callback_data="bts"),
    ],
    [
        InlineKeyboardButton("Bᴏᴛsᴄʜᴋ", callback_data="bsk"),
        InlineKeyboardButton("Cʜᴀᴛ Ai", callback_data="ai"),
        InlineKeyboardButton("Deᴠ", callback_data="dv"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings3"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("❯", callback_data="setting5"),
    ],
]
@Bot.on_callback_query(filters.regex("^settings4$"))
async def help_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_HP4.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP4),
        disable_web_page_preview=True,
    )


TEXT_HP5 = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP5 = [
    [
        InlineKeyboardButton("Acᴛɪᴠᴇ", callback_data="act"),
        InlineKeyboardButton("Adᴍɪɴ", callback_data="adm"),
        InlineKeyboardButton("Auᴛʜ", callback_data="aut"),
    ],
    [
        InlineKeyboardButton("Aᴅᴠɪᴄᴇ", callback_data="adv"),
        InlineKeyboardButton("Aᴘᴘʀᴏᴠᴇ", callback_data="apr"),
        InlineKeyboardButton("B-ʟɪsᴛ", callback_data="blt"),
    ],
    [
        InlineKeyboardButton("Boᴛ", callback_data="bt"),
        InlineKeyboardButton("Bᴀɴ", callback_data="bn"),
        InlineKeyboardButton("Bᴏᴛs", callback_data="bts"),
    ],
    [
        InlineKeyboardButton("Bᴏᴛsᴄʜᴋ", callback_data="bsk"),
        InlineKeyboardButton("Cʜᴀᴛ Ai", callback_data="ai"),
        InlineKeyboardButton("Deᴠ", callback_data="dv"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings4"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("❯", callback_data="settings"),
    ],
]
@Bot.on_callback_query(filters.regex("^settings5$"))
async def help_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_HP5.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP5),
        disable_web_page_preview=True,
    )


# =============================EXTRA_CMD================================
# =============================EXTRA_CMD================================

text_act = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Acᴛɪᴠᴇ:

々 /ac - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ ʙᴏᴛ.

々 /activevoice - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴀɴᴅ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.

々 /activevideo - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.

々 /stats - Cʜᴇᴄᴋ Bᴏᴛs Sᴛᴀᴛs
"""
buttons_act = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^act$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_act,
        reply_markup=InlineKeyboardMarkup(buttons_act),
        disable_web_page_preview=True,
    )


text_adm = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Adᴍɪɴ:
c sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.

々 /pause ᴏʀ /cpause - Pᴀᴜsᴇ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /resume ᴏʀ /cresume - Rᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ ᴍᴜsɪᴄ.
々 /mute ᴏʀ /cmute - Mᴜᴛᴇ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /unmute ᴏʀ /cunmute - Uɴᴍᴜᴛᴇ ᴛʜᴇ ᴍᴜᴛᴇᴅ ᴍᴜsɪᴄ.
々 /skip ᴏʀ /cskip - Sᴋɪᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /stop ᴏʀ /cstop - Sᴛᴏᴘ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /shuffle ᴏʀ /cshuffle - Rᴀɴᴅᴏᴍʟʏ sʜᴜғғʟᴇs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪsᴛ.
々 /seek ᴏʀ /cseek - Fᴏʀᴡᴀʀᴅ Sᴇᴇᴋ ᴛʜᴇ ᴍᴜsɪᴄ ᴛᴏ ʏᴏᴜʀ ᴅᴜʀᴀᴛɪᴏɴ.
々 /seekback ᴏʀ /cseekback - Bᴀᴄᴋᴡᴀʀᴅ Sᴇᴇᴋ ᴛʜᴇ ᴍᴜsɪᴄ ᴛᴏ ʏᴏᴜʀ ᴅᴜʀᴀᴛɪᴏɴ.
々 /reboot - Rᴇʙᴏᴏᴛ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ.

々 /skip ᴏʀ /cskip [Nᴜᴍʙᴇʀ (ᴇxᴀᴍᴘʟᴇ: 𝟹)] - Sᴋɪᴘs ᴍᴜsɪᴄ ᴛᴏ ᴀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ǫᴜᴇᴜᴇᴅ ɴᴜᴍʙᴇʀ. Exᴀᴍᴘʟᴇ: /skip 𝟹 ᴡɪʟʟ sᴋɪᴘ ᴍᴜsɪᴄ ᴛᴏ ᴛʜɪʀᴅ ǫᴜᴇᴜᴇᴅ ᴍᴜsɪᴄ ᴀɴᴅ ᴡɪʟʟ ɪɢɴᴏʀᴇ 𝟷 ᴀɴᴅ 𝟸 ᴍᴜsɪᴄ ɪɴ ǫᴜᴇᴜᴇ.
々 /loop ᴏʀ /cloop [ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ] ᴏʀ [Nᴜᴍʙᴇʀs ʙᴇᴛᴡᴇᴇɴ 𝟷-𝟷𝟶] - Wʜᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ, ʙᴏᴛ ʟᴏᴏᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ ᴛᴏ 𝟷-𝟷𝟶 ᴛɪᴍᴇs ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. Dᴇғᴀᴜʟᴛ ᴛᴏ 𝟷𝟶 ᴛɪᴍᴇs.
"""
buttons_adm = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^adm$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_adm,
        reply_markup=InlineKeyboardMarkup(buttons_adm),
        disable_web_page_preview=True,
    )


text_aut = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Auᴛʜ:

Aᴜᴛʜ Usᴇʀs ᴄᴀɴ ᴜsᴇ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.

々 /auth [Usᴇʀɴᴀᴍᴇ] - Aᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.

々 /unauth [Usᴇʀɴᴀᴍᴇ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.

々 /authusers - Cʜᴇᴄᴋ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
"""
buttons_aut = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^aut$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_aut,
        reply_markup=InlineKeyboardMarkup(buttons_aut),
        disable_web_page_preview=True,
    )


text_adv = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Aᴅᴠɪᴄᴇ:

々 /advice - Gᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ
々 /astronomical - ᴛᴏ ɢᴇᴛ ᴛᴏᴅᴀʏ's ᴀsᴛʀᴏɴᴏᴍɪᴄᴀʟ  ғᴀᴄᴛ
"""
buttons_adv = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^adv$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_adv,
        reply_markup=InlineKeyboardMarkup(buttons_adv),
        disable_web_page_preview=True,
    )


text_apr = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Aᴘᴘʀᴏᴠᴇ:

Tʜɪs ᴍᴏᴅᴜʟᴇ ʜᴇʟᴘs ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴄᴄᴇᴘᴛ ᴄʜᴀᴛ ɪᴏɪɴ ʀᴇǫᴜᴇsᴛ sᴇɴᴅ ʙʏ ᴀ ᴜsᴇʀ ᴛʜʀᴏᴜɢʜ ɪɴᴠɪᴛᴀᴛɪᴏɴ ʟɪɴᴋ ᴏғ ʏᴏᴜʀ ɢʀᴏᴜᴘ

Mᴏᴅᴇs:
ᴡʜᴇɴ ʏᴏᴜ sᴇɴᴅ /autoapprove ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʏᴏᴜ sᴇᴇ ᴛᴜʀɴ ᴏɴ ʙᴜᴛᴛᴏɴ ɪғ ᴀᴜᴛᴛᴏᴘʀᴏᴠᴇ ɴᴏᴛ ᴇɴᴀʙʟᴇᴅ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ ɪғ ᴀʟʀᴇᴅʏ ᴛᴜʀɴᴇᴅ ᴏɴ ʏᴏᴜ ᴡɪʟʟ sᴇ ᴛᴡᴏ ᴍᴏᴅᴇs ᴛʜᴀᴛ's ᴀʀᴇ ʙᴇʟᴏᴡ ᴀɴᴅ ʜɪs ᴜsᴀsɢᴇ


々 Automatic - ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴄᴄᴇᴘᴛs ᴄʜᴀᴛ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ.

々 Manual - ᴀ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ ʙʏ ᴛᴀɢɢɪɴɢ ᴛʜᴇ ᴀᴅᴍɪɴs. ᴛʜᴇ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴄᴄᴇᴘᴛ ᴏʀ ᴅᴇᴄʟɪɴᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛs.

々 /clearpending ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴘᴇɴᴅɪɴɢ ᴜsᴇʀ ɪᴅ ғʀᴏᴍ ᴅʙ. ᴛʜɪs ᴡɪʟʟ ᴀʟʟᴏᴡ ᴛʜᴇ ᴜsᴇʀ ᴛᴏ sᴇɴᴅ ʀᴇǫᴜᴇsᴛ ᴀɢᴀɪɴ.
"""
buttons_apr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^apr$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_apr,
        reply_markup=InlineKeyboardMarkup(buttons_apr),
        disable_web_page_preview=True,
    )


text_blt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ B-ʟɪsᴛ:

々 /blacklistchat [ᴄʜᴀᴛ ɪᴅ] - Bʟᴀᴄᴋʟɪsᴛ ᴀɴʏ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ Mᴜsɪᴄ Bᴏᴛ
々 /whitelistchat [ᴄʜᴀᴛ ɪᴅ] - Wʜɪᴛᴇʟɪsᴛ ᴀɴʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ Mᴜsɪᴄ Bᴏᴛ
々 /blacklistedchat - Cʜᴇᴄᴋ ᴀʟʟ ʙʟᴏᴄᴋᴇᴅ ᴄʜᴀᴛs.

々 /block [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Pʀᴇᴠᴇɴᴛs ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴜsɪɴɢ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs.
々 /unblock [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ Bᴏᴛ's Bʟᴏᴄᴋᴇᴅ Lɪsᴛ.
々 /blockedusers - Cʜᴇᴄᴋ ʙʟᴏᴄᴋᴇᴅ Usᴇʀs Lɪsᴛs

ⓘ /gban [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Gʙᴀɴ ᴀ ᴜsᴇʀ ғʀᴏᴍ ʙᴏᴛ's sᴇʀᴠᴇᴅ ᴄʜᴀᴛ ᴀɴᴅ sᴛᴏᴘ ʜɪᴍ ғʀᴏᴍ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.
ⓘ /ungban [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ Bᴏᴛ's ɢʙᴀɴɴᴇᴅ Lɪsᴛ ᴀɴᴅ ᴀʟʟᴏᴡ ʜɪᴍ ғᴏʀ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ
ⓘ /gbannedusers - Cʜᴇᴄᴋ Gʙᴀɴɴᴇᴅ Usᴇʀs Lɪsᴛs
"""
buttons_blt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^blt$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_blt,
        reply_markup=InlineKeyboardMarkup(buttons_blt),
        disable_web_page_preview=True,
    )


text_bt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Boᴛ:

々 c sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.

々 /stats - Gᴇᴛ Tᴏᴘ 𝟷𝟶 Tʀᴀᴄᴋs Gʟᴏʙᴀʟ Sᴛᴀᴛs, Tᴏᴘ 𝟷𝟶 Usᴇʀs ᴏғ ʙᴏᴛ, Tᴏᴘ 𝟷𝟶 Cʜᴀᴛs ᴏɴ ʙᴏᴛ, Tᴏᴘ 𝟷𝟶 Pʟᴀʏᴇᴅ ɪɴ ᴀ ᴄʜᴀᴛ ᴇᴛᴄ ᴇᴛᴄ.

々 /sudolist - Cʜᴇᴄᴋ Sᴜᴅᴏ Usᴇʀs ᴏғ Bᴏᴛ

々 /lyrics [Mᴜsɪᴄ Nᴀᴍᴇ] - Sᴇᴀʀᴄʜᴇs Lʏʀɪᴄs ғᴏʀ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ Mᴜsɪᴄ ᴏɴ ᴡᴇʙ.

々 /player - Gᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ Pʟᴀʏɪɴɢ Pᴀɴᴇʟ.

々 /queue ᴏʀ /cqueue - Cʜᴇᴄᴋ Qᴜᴇᴜᴇ Lɪsᴛ ᴏғ Mᴜsɪᴄ.

    ⚡️Pʀɪᴠᴀᴛᴇ Bᴏᴛ:  
ⓘ /authorize [CHAT_ID] - Aʟʟᴏᴡ ᴀ ᴄʜᴀᴛ ғᴏʀ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.

ⓘ /unauthorize[CHAT_ID] - Dɪsᴀʟʟᴏᴡ ᴀ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.

ⓘ /authorized - Cʜᴇᴄᴋ ᴀʟʟ ᴀʟʟᴏᴡᴇᴅ ᴄʜᴀᴛs ᴏғ ʏᴏᴜʀ ʙᴏᴛ.
"""
buttons_bt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^bt$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_bt,
        reply_markup=InlineKeyboardMarkup(buttons_bt),
        disable_web_page_preview=True,
    )


text_bn = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Bᴀɴ:

/ban - Ban A User
/banall - Ban All Users
/sban - Delete all messages of user that sended in group and ban the user
/tban - Ban A User For Specific Time
/unban - Unban A User
/warn - Warn A User
/swarn - Delete all the message sended in group and warn the user
/rmwarns - Remove All Warning of A User
/warns - Show Warning Of A User
/kick - Kick A User
/skick - Delete the replied message kicking its sender
/purge - Purge Messages
/purge [n] - Purge "n" number of messages from replied message
/del - Delete Replied Message
/promote - Promote A Member
/fullpromote - Promote A Member With All Rights
/demote - Demote A Member
/pin - Pin A Message
/unpin - unpin a message
/unpinall - unpinall messages
/mute - Mute A User
/tmute - Mute A User For Specific Time
/unmute - Unmute A User
/zombies - Ban Deleted Accounts
/report | @admins | @admin - Report A Message To Admins.
"""
buttons_bn = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^bn$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_bn,
        reply_markup=InlineKeyboardMarkup(buttons_bn),
        disable_web_page_preview=True,
    )


text_bts = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Bᴏᴛs:

ʙᴏᴛs

々 /bots - ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ʙᴏᴛs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
"""
buttons_bts = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^bts$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_bts,
        reply_markup=InlineKeyboardMarkup(buttons_bts),
        disable_web_page_preview=True,
    )


text_bsk = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Bᴏᴛsᴄʜᴋ:

Dᴇsᴄʀɪᴘᴛɪᴏɴ:
Cʜᴇᴄᴋs ᴛʜᴇ ᴏɴɪɴᴇ sᴛᴀᴛᴜs ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ʙᴏᴛ ʙʏ sᴇɴᴅɪɴɢ ɪᴛ ᴀ /start ᴍᴇssᴀɢᴇ.

Usᴀɢᴇ:
/botschk Bᴏᴛ_Usᴇʀɴᴀᴍᴇ

Dᴇᴛᴀɪs:
々 Sᴇɴᴅs /start ᴛᴏ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ʙᴏᴛ ᴀɴᴅ ᴄʜᴇᴄᴋs ɪғ ɪᴛ ʀᴇsᴘᴏɴᴅs.
々 Dɪsᴘᴀʏs ᴛʜᴇ ʙᴏᴛ's sᴛᴀᴛᴜs ᴀs ᴇɪᴛʜᴇʀ ᴏɴɪɴᴇ ᴏʀ ᴏғғɪɴᴇ.

Exᴀᴍᴘᴇs:
々 /botschk @YᴏᴜʀBᴏᴛUsᴇʀɴᴀᴍᴇ: Cʜᴇᴄᴋs ɪғ @YᴏᴜʀBᴏᴛUsᴇʀɴᴀᴍᴇ ɪs ᴏɴɪɴᴇ ᴏʀ ᴏғғɪɴᴇ.

Nᴏᴛᴇs:
々 Tʜᴇ ʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇ ᴍᴜsᴛ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴀs ᴀɴ ᴀʀɢᴜᴍᴇɴᴛ.
々 Tʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴡɪ ᴅɪsᴘᴀʏ ᴀɴ ᴇʀʀᴏʀ ᴍᴇssᴀɢᴇ ɪғ ᴛʜᴇ ᴜsᴇʀɴᴀᴍᴇ ɪs ɪɴᴄᴏʀʀᴇᴄᴛ ᴏʀ ɪғ ᴛʜᴇʀᴇ ᴀʀᴇ ɪᴍɪᴛᴀᴛɪᴏɴs.

Oᴜᴛᴘᴜᴛ:
々 Dɪsᴘᴀʏs ᴛʜᴇ ʙᴏᴛ's ᴍᴇɴᴛɪᴏɴ ᴀɴᴅ ɪᴛs ᴏɴɪɴᴇ sᴛᴀᴛᴜs.
々 Sʜᴏᴡs ᴛʜᴇ ᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴛɪᴍᴇ.
"""
buttons_bsk = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^bsk$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_bsk,
        reply_markup=InlineKeyboardMarkup(buttons_bsk),
        disable_web_page_preview=True,
    )


text_ai = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Cʜᴀᴛ Ai:

々 /advice - ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ ʙʏ ʙᴏᴛ
々 /ai [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ᴄʜᴀᴛɢᴘᴛ's ᴀɪ
々 /gemini [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ɢᴇᴍɪɴɪ ᴀɪ
々 /bard [ǫᴜᴇʀʏ] -ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ʙᴀʀᴅ ᴀɪ
"""
buttons_ai = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^ai$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_ai,
        reply_markup=InlineKeyboardMarkup(buttons_ai),
        disable_web_page_preview=True,
    )


text_dv = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Deᴠ:

🔰Aᴅᴅ Aɴᴅ Rᴇᴍᴏᴠᴇ Sᴜᴅᴏ Usᴇʀ's:
々 /addsudo [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]
々 /delsudo [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]

🤖Bᴏᴛ Cᴏᴍᴍᴀɴᴅs:
ⓘ /restart - Rᴇsᴛᴀʀᴛ ʏᴏᴜʀ Bᴏᴛ. 
ⓘ /update , /gitpull - Uᴘᴅᴀᴛᴇ Bᴏᴛ.
ⓘ /speedtest - Cʜᴇᴄᴋ sᴇʀᴠᴇʀ sᴘᴇᴇᴅs
ⓘ /maintenance [ᴇɴᴀʙʟᴇ / ᴅɪsᴀʙʟᴇ]
ⓘ /logger [ᴇɴᴀʙʟᴇ / ᴅɪsᴀʙʟᴇ] - Bᴏᴛ ʟᴏɢs ᴛʜᴇ sᴇᴀʀᴄʜᴇᴅ ǫᴜᴇʀɪᴇs ɪɴ ʟᴏɢɢᴇʀ ɢʀᴏᴜᴘ.
ⓘ /get_log [Nᴜᴍʙᴇʀ ᴏғ Lɪɴᴇs] - Gᴇᴛ ʟᴏɢ ᴏғ ʏᴏᴜʀ ʙᴏᴛ ғʀᴏᴍ ʜᴇʀᴏᴋᴜ ᴏʀ ᴠᴘs. Wᴏʀᴋs ғᴏʀ ʙᴏᴛʜ.
ⓘ /autoend [ᴇɴᴀʙʟᴇ|ᴅɪsᴀʙʟᴇ] - Eɴᴀʙʟᴇ Aᴜᴛᴏ sᴛʀᴇᴀᴍ ᴇɴᴅ ᴀғᴛᴇʀ 𝟹 ᴍɪɴs ɪғ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ.
"""
buttons_dv = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^dv$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_dv,
        reply_markup=InlineKeyboardMarkup(buttons_dv),
        disable_web_page_preview=True,
    )


text_flt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Filters:

々 /filters To Get All The Filters In The Chat.
々 /filter [FILTER_NAME] To Save A Filter(reply to a message).

Supported filter types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.

To use more words in a filter use.
々 /filter Hey_there To filter "Hey there".

々 /stop [FILTER_NAME] To Stop A Filter.
々 /stopall To delete all the filters in a chat (permanently).

You can use markdown or html to save text too.

Checkout /markdownhelp to know more about formattings and other syntax.
"""
buttons_flt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^flt$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_flt,
        reply_markup=InlineKeyboardMarkup(buttons_flt),
        disable_web_page_preview=True,
    )


text_fgl = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Fɪɢʟᴇᴛ:

々 /figlet  - ᴄʀᴇᴀᴛᴇs ᴀ ғɪɢʟᴇᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
"""
buttons_fgl = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^fgl$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_fgl,
        reply_markup=InlineKeyboardMarkup(buttons_fgl),
        disable_web_page_preview=True,
    )


text_fk = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Fᴀᴋᴇ:

々 /fake [ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ ] - ᴛᴏ ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴅʀᴇss
"""
buttons_fk = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^fk$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_fk,
        reply_markup=InlineKeyboardMarkup(buttons_fk),
        disable_web_page_preview=True,
    )


text_fon = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Fᴏɴᴛ:

々 /font [text] - ᴄᴏɴᴠᴇʀᴛs sɪᴍᴩʟᴇ ᴛᴇxᴛ ᴛᴏ ʙᴇᴀᴜᴛɪғᴜʟ ᴛᴇxᴛ ʙʏ ᴄʜᴀɴɢɪɴɢ ɪᴛ's ғᴏɴᴛ.
"""
buttons_fon = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^fon$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_fon,
        reply_markup=InlineKeyboardMarkup(buttons_fon),
        disable_web_page_preview=True,
    )


text_fn = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Fᴜɴ:

ʜᴀᴠɪɴɢ ꜰᴜɴ:
々 /dice: Rᴏʟʟs ᴀ ᴅɪᴄᴇ.
々 /ludo: Pʟᴀʏ Lᴜᴅᴏ.
々 /dart: Tʜʀᴏᴡs ᴀ ᴅᴀʀᴛ.
々 /basket ᴏʀ /basketball: Pʟᴀʏs ʙᴀsᴋᴇᴛʙᴀʟʟ.
々 /football: Pʟᴀʏs ғᴏᴏᴛʙᴀʟʟ.
々 /slot ᴏʀ /jackpot: Pʟᴀʏs ᴊᴀᴄᴋᴘᴏᴛ.
々 /bowling: Pʟᴀʏs ʙᴏᴡʟɪɴɢ.
々 /bored: Gᴇᴛs ʀᴀɴᴅᴏᴍ ᴀᴄᴛɪᴠɪᴛʏ ɪғ ʏᴏᴜ'ʀᴇ ʙᴏʀᴇᴅ.
"""
buttons_fn = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^fn$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_fn,
        reply_markup=InlineKeyboardMarkup(buttons_fn),
        disable_web_page_preview=True,
    )


text_gt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ G-ᴄᴀsᴛ:

々 /broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] » ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴍᴏᴅᴇs:

-pin » ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.

-pinloud » ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴀɴᴅ sᴇɴᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴍᴇᴍʙᴇʀs.

-user » ʙʀᴏᴀᴅᴄᴀsᴛs ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.

-assistant » ʙʀᴏᴀᴅᴄᴀsᴛ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀssɪᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.

-nobot » ғᴏʀᴄᴇs ᴛʜᴇ ʙᴏᴛ ᴛᴏ ɴᴏᴛ ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ.

ᴇxᴀᴍᴩʟᴇ: /broadcast -user -assistant -pin ᴛᴇsᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ
"""
buttons_gt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^gt$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_gt,
        reply_markup=InlineKeyboardMarkup(buttons_gt),
        disable_web_page_preview=True,
    )


text_gl = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Gʀᴏᴜᴘ Lɪɴᴋ:

々 /ɢɪᴠᴇɪɴᴋ: Gᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ɪɴᴋ ғᴏʀ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛ.
々 /ɪɴᴋ ɢʀᴏᴜᴘ_ɪᴅ: Gᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀɴᴅ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴ ɪɴᴠɪᴛᴇ ɪɴᴋ ғᴏʀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ɢʀᴏᴜᴘ ID.
"""
buttons_gl = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^gl$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_gl,
        reply_markup=InlineKeyboardMarkup(buttons_gl),
        disable_web_page_preview=True,
    )


text_gli = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Gᴀʟɪ:

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʏ ғᴏʀ Pʀɪᴠᴀᴛᴇ ᴍᴇssᴀɢᴇ, Gᴏ Tᴏ Bᴏᴛ Pʀɪᴠᴀᴛᴇ Mᴇssᴀɢᴇ Aɴᴅ Tʏᴘᴇ /gai Cᴏᴍᴍᴀɴᴅ.

Fᴇᴀᴛᴜʀᴇs:
- Pʀᴏᴠɪᴅᴇs ʀᴀɴᴅᴏᴍ ᴀʙᴜsɪᴠᴇ ᴀɴɢᴜᴀɢᴇ (ɢᴀɪ) ᴡʜᴇɴ ᴜsᴇᴅ ɪɴ DMs.
- Dɪsᴘᴀʏs ᴀ ᴍᴇssᴀɢᴇ ɪɴᴅɪᴄᴀᴛɪɴɢ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʏ ғᴏʀ ᴘʀɪᴠᴀᴛᴇ ᴍᴇssᴀɢᴇs ᴡʜᴇɴ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs.

Cᴏᴍᴍᴀɴᴅ:
 /gai : Sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴀʙᴜsɪᴠᴇ ᴀɴɢᴜᴀɢᴇ (ɢᴀɪ) ᴡʜᴇɴ ᴜsᴇᴅ ɪɴ DMs.

Nᴏᴛᴇ: Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴛᴏ ᴘʀɪᴠᴀᴛᴇ ᴍᴇssᴀɢᴇs ᴏɴʏ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴ ᴅᴇᴄᴏʀᴜᴍ ɪɴ ɢʀᴏᴜᴘ ᴄʜᴀᴛs.
"""
buttons_gli = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^gli$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_gli,
        reply_markup=InlineKeyboardMarkup(buttons_gli),
        disable_web_page_preview=True,
    )


text_src = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Gᴏᴏɢʟᴇ:
々 /google [ǫᴜᴇʀʏ] - ᴛᴏ sᴇᴀʀᴄʜ ᴏɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ɢᴇᴛ ʀᴇsᴜʟᴛs
々 /app | /apps [ᴀᴘᴘ ɴᴀᴍᴇ] - ᴛᴏ ɢᴇᴛ ᴀᴘᴘ ɪɴғᴏ ᴛʜᴀᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴘʟᴀʏsᴛᴏʀᴇ
"""
buttons_src = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^src$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_src,
        reply_markup=InlineKeyboardMarkup(buttons_src),
        disable_web_page_preview=True,
    )


text_gdy = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Gᴏᴏᴅʙʏᴇ:

ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ɢᴏᴏᴅʙʏᴇ:
/setgoodbye - Rᴇᴘʟʏ ᴛʜɪs ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴀɪɴɪɴɢ ᴄᴏʀʀᴇᴄᴛ
ғᴏʀᴍᴀᴛ ғᴏʀ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ, ᴄʜᴇᴄᴋ ᴇɴᴅ ᴏғ ᴛʜɪs ᴍᴇssᴀɢᴇ.
/goodbye - Tᴏ ɢᴇᴛ ʏᴏᴜʀ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ
/goodbye  [ᴏɴ, ʏ, ᴛʀᴜᴇ, ᴇɴᴀʙʟᴇ, ᴛ] - ᴛᴏ ᴛᴜʀɴ ᴏɴ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇs
/goodbye [ᴏғғ, ɴ, ғᴀʟsᴇ, ᴅɪsᴀʙʟᴇ, ғ, ɴᴏ] - ᴛᴏ ᴛᴜʀɴ ᴏғғ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇs
/delgoodbye ᴏʀ /deletegoodbye ᴛᴏ ᴅᴇʟᴛᴇ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴛᴜʀɴ ᴏғғ ɢᴏᴏᴅʙʏᴇ
SetoodBye ->

Tᴏ sᴇᴛ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ɢɪғ ᴀs ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ. Aᴅᴅ ʏᴏᴜʀ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ ᴀs ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴘʜᴏᴛᴏ ᴏʀ ɢɪғ. Tʜᴇ ᴄᴀᴘᴛɪᴏɴ ᴍᴜsᴇ ʙᴇ ɪɴ ᴛʜᴇ ғᴏʀᴍᴀᴛ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
Fᴏʀ ᴛᴇxᴛ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ Jᴜsᴛ sᴇɴᴅ ᴛʜᴇ ᴛᴇxᴛ. Tʜᴇɴ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ
Tʜᴇ ғᴏʀᴍᴀᴛ sʜᴏᴜʟᴅ ʙᴇ sᴏᴍᴇᴛʜɪɴɢ ʟɪᴋᴇ ʙᴇʟᴏᴡ.
Hɪ {NAME} [{ID}] Wᴇʟᴄᴏᴍᴇ ᴛᴏ {GROUPNAME}

~ Tʜɪs sᴇᴘᴀʀᴀᴛᴇʀ (~) sʜᴏᴜʟᴅ ʙᴇ ᴛʜᴇʀᴇ ʙᴇᴛᴡᴇᴇɴ ᴛᴇxᴛ ᴀɴᴅ ʙᴜᴛᴛᴏɴs, ʀᴇᴍᴏᴠᴇ ᴛʜɪs ᴄᴏᴍᴍᴇɴᴛ ᴀʟsᴏ

Button=[Dᴜᴄᴋ, ʜᴛᴛᴘs://ᴅᴜᴄᴋᴅᴜᴄᴋɢᴏ.ᴄᴏᴍ]
Button2=[Gɪᴛʜᴜʙ, ʜᴛᴛᴘs://ɢɪᴛʜᴜʙ.ᴄᴏᴍ]
NOTES ->

Cʜᴇᴄᴋᴏᴜᴛ /markdownhelp ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ғᴏʀᴍᴀᴛᴛɪɴɢs ᴀɴᴅ ᴏᴛʜᴇʀ sʏɴᴛᴀx.
"""
buttons_gdy = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^gdy$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_gdy,
        reply_markup=InlineKeyboardMarkup(buttons_gdy),
        disable_web_page_preview=True,
    )


text_hsr = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Hɪsᴛᴏʀʏ: 

1. /sg ᴏʀ /history 
Dᴇsᴄʀɪᴘᴛɪᴏɴ:
Fᴇᴛᴄʜᴇs ᴀ ʀᴀɴᴅᴏᴍ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ʜɪsᴛᴏʀʏ.

Usᴀɢᴇ:
々 /sg [ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ/ʀᴇᴘʏ]

Dᴇᴛᴀɪs:
- Fᴇᴛᴄʜᴇs ᴀ ʀᴀɴᴅᴏᴍ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ ʜɪsᴛᴏʀʏ ᴏғ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ᴜsᴇʀ.
- Cᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴘʀᴏᴠɪᴅɪɴɢ ᴀ ᴜsᴇʀɴᴀᴍᴇ, ᴜsᴇʀ ID, ᴏʀ ʀᴇᴘʏɪɴɢ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴜsᴇʀ.
- Aᴄᴄᴇssɪʙᴇ ᴏɴʏ ʙʏ ᴛʜᴇ ʙᴏᴛ's ᴀssɪsᴛᴀɴᴛs.

Exᴀᴍᴘᴇs:
- /sg ᴜsᴇʀɴᴀᴍᴇ
- /sg ᴜsᴇʀ_ɪᴅ
- /sg [ʀᴇᴘʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]
"""
buttons_hsr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^hsr$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_hsr,
        reply_markup=InlineKeyboardMarkup(buttons_hsr),
        disable_web_page_preview=True,
    )


text_htg = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Hᴀsʜᴛᴀɢ:

ʜᴀsʜᴛᴀɢ ɢᴇɴᴇʀᴀᴛᴏʀ:

々 /hashtag [text]: Gᴇɴᴇʀᴀᴛᴇ ʜᴀsʜᴛᴀɢs ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
"""
buttons_htg = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^htg$"))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_htg,
        reply_markup=InlineKeyboardMarkup(buttons_htg),
        disable_web_page_preview=True,
    )


# =============================================================
# =============================================================

# ==============CLOSE===================
@Bot.on_callback_query(filters.regex("^close$"))
async def close_cb(bot, callback):
    await callback.answer("❌Closed the Module❌")
    await callback.message.delete()
    await callback.message.reply_to_message.delete()
