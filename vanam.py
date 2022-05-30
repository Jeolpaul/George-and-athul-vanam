from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Jeol=Client(
    "Jeol Bot",
    bot_token="5330183223:AAER7GJRDm9ONrAkWo72eVZCFub-iFSZlsI",
    api_id="11271918",
    api_hash="1cd29c2b7e1df5f18aeaeafbf7ebf7cd"
)


IKKA_STRINGS = (
    "CAACAgUAAxkBAAIDUmIN8bqiD5DYQLjQzUwH7-1AsH0eAAJGBAAClj7wVxJlL3v8QuaoHgQ",
    "CAACAgUAAxkBAAIDVmIN8cCiVJZl05m0wiggUJaOvYarAAL5BAACo7lRVClze9Et3bCJHgQ",
    "CAACAgUAAxkBAAIDV2IN8cSKz20_0T-f7BlHVQfQYPu_AAKfAwACA4rwV01BOgyNllX1HgQ",
    "CAACAgUAAxkBAAIDWGIN8coT1jTnXpetiFOKVGZVCX78AAJLBAACrXgAAVTcB_E8ndEu0h4E",
    "CAACAgUAAxkBAAIDWWIN8c-GSo6HX8bmIvJOwDXG1pJ-AAJkBAACbYZIVIF7psBskaRiHgQ",
    "CAACAgUAAxkBAAIDWmIN8dfwrILfwAABBczAR4DoYxpkvAACvwUAAlNOSFRraTuQ8L5Qzx4E",
    "CAACAgUAAxkBAAIDXGIN8eN4RRZPSvKW5OcDhBGnF_qIAAJtBQACwq0JVAnAmIgTMZr6HgQ",
    "CAACAgUAAxkBAAIDeGIN8ke0Qm7S8rWAp5XRHtG21RP1AAJzBQACg5tAVL8bVAS2wafYHgQ",
    "CAACAgUAAxkBAAIDfGIN8lvvH0C9VGSLMV7fvxJ9L_r9AAIlBgACf4hJVA_SXDgpTipeHgQ",
    "CAACAgUAAxkBAAIDf2IN8nL54y-xsW_PGMX5T96e_ErnAAJiAwACjh3YV6f4T7ZwQqExHgQ",
    "CAACAgUAAxkBAAIDgmIN8oZFf70SfKUOl9nnk0Q0uIGPAAJjAwAC3-lRVqPrbp8AAeUBch4E",
    "CAACAgUAAxkBAAIDj2IN86K_5xEpxc00sVRoFLgNgvh_AALeAgACh49oVh2VB0KUEX3zHgQ",
    "CAACAgUAAxkBAAIDkmIN87LWn-56jo9wHTdifHsdBCAiAAJPAwACK4yZVlCyU1tXbk2YHgQ",
)

GEORGE_STRINGS = (
    "CAACAgUAAxkBAAIEWWKVEfYirClTVlhzH6DpPO6j9yr0AAJTAQACzmH-PxR3YTluUCHfHgQ",
    "CAACAgUAAxkBAAIEWGKVEfoFK84M6DfjjJX1u5V9xHx2AAJQAQACzmH-P_UNk16JrA4pHgQ",
    "CAACAgUAAxkBAAIEV2KVEgLnaaNf647mdoABHBgtlL2EAAJLAQACzmH-P6TF3YXdW-GRHgQ",
    "CAACAgUAAxkBAAIEVmKVEgeH_m5HQAAB15AJoHDxcohv8gACTAEAAs5h_j8_p5Us9h1BFB4E",
    "CAACAgUAAxkBAAIEVWKVEg8BXRYleawLAnK2WCiDZRWbAAJKAQACzmH-P01w7wKstoIqHgQ",
    "CAACAgUAAxkBAAIEVGKVEhiaAAEps3agBXrn8C-CDmhYzwACQAEAAs5h_j9NbOaKhUGqex4E",
    "CAACAgUAAxkBAAIEU2KVEh3e3NwuXlfc0QsI1NW2ewJtAAI2AQACzmH-PyULjEzNLlo6HgQ",
    "CAACAgUAAxkBAAIDeGIN8ke0Qm7S8rWAp5XRHtG21RP1AAJzBQACg5tAVL8bVAS2wafYHgQ",
    "CAACAgUAAxkBAAIDfGIN8lvvH0C9VGSLMV7fvxJ9L_r9AAIlBgACf4hJVA_SXDgpTipeHgQ",
    "CAACAgUAAxkBAAIEUmKVEiGY9fbU0ZRFHGIOS2EeYR7gAAIjAQACzmH-P8kaTu4rby6EHgQ",
    "CAACAgUAAxkBAAIDgmIN8oZFf70SfKUOl9nnk0Q0uIGPAAJjAwAC3-lRVqPrbp8AAeUBch4E",
    "CAACAgUAAxkBAAIDj2IN86K_5xEpxc00sVRoFLgNgvh_AALeAgACh49oVh2VB0KUEX3zHgQ",
    "CAACAgUAAxkBAAIDkmIN87LWn-56jo9wHTdifHsdBCAiAAJPAwACK4yZVlCyU1tXbk2YHgQ",
) 

@Jeol.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_sticker(
        sticker="CAACAgUAAxkBAAIBVWJ-WSUvU7wpjy_Xsks_-bkp_0TkAAJBBQACs5HYV3DqxafNLRz0JAQ",
    )


    await message.reply_text(
        text="Hello👋🏻 How are you Iam a Telegram Bot to Get Your user information.Type /help to know the commands",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Support", url="https://t.me/BETA_BOTSUPPORT"),
            InlineKeyboardButton("Updates", url="https://t.me/BETA_UPDATES")
            ],[
            InlineKeyboardButton("Developer", url="https://t.me/JP_Jeol")
            ]]
            )
        )

@Client.on_message(filters.command("ikka") &
    f_onw_fliter
)
async def ikka(bot, message):
    """ /ikka strings """
    effective_string = random.choice(IKKA_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(effective_string)
    else:
        await message.reply_sticker(effective_string)


@Client.on_message(filters.command("george") &
    f_onw_fliter
)
async def ikka(bot, message):
    """ /george strings """
    effective_string = random.choice(GEORGE_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(effective_string)
    else:
        await message.reply_sticker(effective_string)




@Jeol.on_message(filters.command("help"))
async def help_message(bot, message):
    await message.reply_photo(
        photo="https://telegra.ph//file/e937426b58e31a881c25f.jpg",
        caption="""Hey how can i help You. The Basic Commands is /id & /info.
If you have any questions join support
Group and ask🤍❤️
Thank you for using Beta""")



@Jeol.on_message(filters.command("id"))
async def id_message(bot, message):
    await message.reply_text(
    text = f"""
👁️‍🗨️DETAILS
○ID : {message.from_user.id}
○FIRST NAME : {message.from_user.first_name}
○LAST NAME : {message.from_user.last_name}
○USERNAME : @{message.from_user.username}
○MENTION : {message.from_user.mention}

THANK YOU FOR USING BETA🤍""")

@Jeol.on_message(filters.command("info"))
async def info_message(bot, message):
    await message.reply_text(
    text = f"""
👁️‍🗨️DETAILS
○ID : {message.from_user.id}
○FIRST NAME : {message.from_user.first_name}
○LAST NAME : {message.from_user.last_name}
○USERNAME : @{message.from_user.username}
○MENTION : {message.from_user.mention}

THANK YOU FOR USING BETA🤍""")





Jeol.run()
