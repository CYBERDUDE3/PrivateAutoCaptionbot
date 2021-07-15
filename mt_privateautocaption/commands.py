#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) PR0FESSOR-99

import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

USERNAME=Config.BOT_USERNAME

@Client.on_message(filters.private & filters.command("start"))
async def start(client, update):
    text = f"""<b> 👋Hello {update.from_user.mention}\n\nI am an AutoCaption bot\n\nAll you have to do is add me to your channel and I will show you my power\n\nFor more info check help Button\n\n© @Mo_Tech_YT</b>"""
    reply_markup =  InlineKeyboardMarkup(
                                         [[
        InlineKeyboardButton("help↗️", callback_data="heroku"),
        InlineKeyboardButton("🗣️Group", url="t.me/M_SRER_TECH_GROUP"),
        InlineKeyboardButton("Channel📢", url="t.me/M_STER_TECH")
        ]]
    )
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@Client.on_callback_query(filters.regex(r"^(heroku|about|motech)$"))
async def callback_data(client, update: CallbackQuery):

    query_data = update.data

    if query_data == "heroku":
        buttons = [[
            InlineKeyboardButton("🖥️ Tutorial Video 🖥️", url="https://youtu.be/p4Z9ZN1lZUk")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("❌️Close", callback_data="motech"),
            InlineKeyboardButton("About↗️", callback_data="about")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>🔻AutoCaption Bot🔻</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "about":
        buttons = [[
            InlineKeyboardButton("🗣️Group", url="t.me/mo_tech_Group"),
            InlineKeyboardButton("Channel📢", url="https://t.me/M_STER_TECH")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("🔙Back", callback_data="heroku")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>➪ Bot Name</b> AutoCaptionBot\n\n➪ <b>Framework : Pyrogram</b>\n\n➪<b> Language : Python</b>\n\n➪<b> Server : Heroku</b> \n\n<b>➪ Version : 2.0.1</b>\n\n<b>➪ Source Code  : <a href="https://github.com/PR0FESS0R-99/PrivateAutoCaption">Touch Me 🤗</a>\n\n➪ Developer :  @PR0FESS0R_99\n\n➪ Credits : <a href="https://github.com/PR0FESS0R-99/PrivateAutoCaption/blob/main/mt_privateautocaption/Credits.md">Credits</a></b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "motech":
        await update.message.delete()
