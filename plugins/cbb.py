from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://settings'>ᴛʜɪꜱ ᴘᴇʀꜱᴏɴ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Adult_Infinity/4'>ᴀᴅᴜʟᴛ ɪɴғɪɴɪᴛʏ</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/MovieflixOcean'>ᴛᴇᴀᴍ xᴇᴏɴғʟɪx</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/TeamXeon'>xᴇᴏɴғʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n○ ᴀɴɪᴍᴇ  : <a href='https://t.me/Anime_Xeon'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/Adult_Infinity"),
                    InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url='https://t.me/Xeonflix')
                    ],
                    [
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/MovieflixOcean"),
                    InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url='https://t.me/SeriesFlixOcean')
                    ],
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/Adult_Infinity/4')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "buy_prem":
        await query.message.edit_text(
            text=f"👋 {query.from_user.username}\n\n🎖️ Available Plans :\n\n● {PRICE1} rs For 7 Days Prime Membership\n\n● {PRICE2} rs For 1 Month Prime Membership\n\n● {PRICE3} rs For 3 Months Prime Membership\n\n● {PRICE4} rs For 6 Months Prime Membership\n\n● {PRICE5} rs For 1 Year Prime Membership\n\n\n💵 UPI ID -  <code>{UPI_ID}</code>\n\n\n📸 QR - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ ({UPI_IMAGE_URL})\n\n♻️ If payment is not getting sent on above given QR code then inform admin, he will give you new QR code\n\n\n‼️ Must Send Screenshot after payment",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("Send Payment Screenshot(ADMIN) 📸", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
            )
