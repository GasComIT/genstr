from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

If you don't trust me, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram and telethon string session. Use the below buttons to know more!

By @krakinz
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π₯ Start Generating Session π₯", callback_data="generate")],
        [InlineKeyboardButton(text="π  Return Home π ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("π₯ Start Generating Session π₯", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("π₯ Start Generating Session π₯", callback_data="generate")],
        [InlineKeyboardButton("π¦ Support Chat π¦", url="https://telegram.dog/krakinzc")],
        [
            InlineKeyboardButton("How to Use β", callback_data="help"),
            InlineKeyboardButton("πͺ About πͺ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ More Amazing bots β₯", url="https://telegram.dog/KrakinzBot")],
    ]

    # Help Message
    HELP = """
Β» Click the below button or use /generate command to start generating session!
Β» Click the required button; [Pyrogram/Telethon]
Β» Enter the required variables when asked.

BTW, if you donβt trust me, you can host [one] like me using my source code provided in my about page; [/about]
"""

    # About Message
    ABOUT = """
**β’ About Me β’** 

β’ A telegram bot to generate pyrogram and telethon string session...

Β» Source Code : [Click Here](https://github.com/krakinz/genstr)

Β» Framework : [Pyrogram](docs.pyrogram.org)

Β» Language : [Python](www.python.org)

Β» Support Chat : [Krakinz Channel](https://telegram.me/krakinzc)
    """
