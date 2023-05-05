from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
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


😼 Develoved by </b><a href='https://t.me/OwnNeko'>ꭙ 𝙉𝙚𝙠𝙤 ꭙ</a>
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            ("Help & Commands", callback_data="help"),
            InlineKeyboardButton("Tutup", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("Tentang Saya", callback_data="about"),
            InlineKeyboardButton("Tutup", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:
@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.
 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='ttps://t.me/OwnNeko'>ꭙ 𝙉𝙚𝙠𝙤 ꭙ</a>


😼 Develoved by </b><a href='https://t.me/OwnNeko'>ꭙ 𝙉𝙚𝙠𝙤 ꭙ</a>
"""
   TALLENT = ""'
   <a href='https://t.me/DeaPilo'>𝘿𝙚𝙖 ꭙ 𝙉𝙚𝙠𝙤</a>
   """
    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]
