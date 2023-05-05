from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /talent - Talent List
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk mengecek bot hidup
 └ /uptime - Untuk melihat status bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Untuk melihat logs bot
 ├ /setvar - Untuk mengatur var dengan command dibot
 ├ /delvar - Untuk menghapus var dengan command dibot
 ├ /getvar - Untuk melihat salah satu var dengan command dibot
 ├ /users - Untuk melihat statistik pengguna bot
 ├ /batch - Untuk membuat link lebih dari satu file
 ├ /speedtest - Untuk Mengetes kecepatan server bot
 └ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

<a href='https://t.me/OwnNeko'>ꭙ 𝙉𝙚𝙠𝙤 ꭙ</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="talent"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    TALENT = """
<b>Verifed Talent </b>



 ❏ Owner NekoManagement: @{}
 └ <a href='https://t.me/DeaPilo'>𝘿𝙚𝙖 ꭙ 𝙉𝙚𝙠𝙤</a>


 """
