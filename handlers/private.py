import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/067c81b8a975f5b57f865.jpg",
        caption=f"""**𝗛𝗘𝗟𝗟𝗢 𝗕𝗜𝗥𝗢𝗢✨🥰𝗶𝗠 𝗞𝗜𝗡𝗚 𝗠𝗨𝗦𝗜𝗖 𝗣𝗟𝗔𝗬𝗘𝗥 🎧 𝗔𝗗𝗗 𝗣𝗔𝗡𝗜𝗞𝗢 🥂 𝗦𝗢𝗡𝗚𝗦 𝗞𝗘𝗧𝗨𝗞𝗢 💫 𝗔𝗡𝗬 𝗤𝗨𝗦 𝗼𝗿 𝗜𝗦𝗦𝗨𝗘𝗦 𝗣𝗠 𝗩𝗔 𝗠𝗔𝗖𝗛𝗜 𝗣𝗔𝗧𝗛𝗨 𝗣𝗔𝗡𝗜𝗞𝗔𝗟𝗔𝗠 @iMzaynKING ✨✌️**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰⚡️𝐎ᴡɴᴇʀ⚡️❱", url=f"https://t.me/Imzaynking")
               ],
                [
                    InlineKeyboardButton(
                        "❰💙𝐂ʜᴀɴɴᴇʟ❤️❱", url=f"https://t.me/KING_BIOz")
               ], 
                [
                    InlineKeyboardButton(
                        "❰⭕️𝐒ᴜᴘᴘᴏʀᴛ⭕️❱", url=f"https://t.me/TAMIL_CHATBOX")
               ],
                [
                    InlineKeyboardButton(
                        "❰📚𝐂ᴏᴍᴍᴀɴᴅs 𝐇ᴇʟᴘ📚❱", url=f"https://telegra.ph/-04-09-1257")
                ]
                
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7262b66b1b936e3bd826e.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰💫𝐒ᴏᴜʀᴄᴇ💕❱", url=f"https://t.me/iMzaynKING")
                ]
            ]
        ),
    )
