from os import getenv

import io
import asyncio
import base64

from typing import Union

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ChatAction
from aiogram.exceptions import TelegramAPIError

from ...util import logg

from ..cloud import ClaudeController, GrokController

TELEGRAM_BOT_TOKEN = getenv("TELEGRAM-BOT-TOKEN")

if not TELEGRAM_BOT_TOKEN:
    logg.logError("error getting the telegram key from ev")
    raise

MAX_RETRIES = 3
RETRY_DELAY = 1

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

claudeController = ClaudeController()
grokController = GrokController()

# util funk yah

def getUserID(message: types.Message) -> int:
    """
    get user id safely lmao
    return chat id if user id none

    Args:
        message: telegram message object

    Returns:
        int: user or chat id
    """
    if message.from_user and message.from_user.id:
        return message.from_user.id
    return message.chat.id

async def downloadPhoto(message: types.Message) -> Union[io.BytesIO, None]:
    """
    download photo from message, and try try again

    Args:
        message: telegram message object w/ a photo

    Returns:
        BytesIO object w/ data or None
    """
    if not message.photo:
        return None

    photo = message.photo[-1] # blaze, high rez deez

    for attempt in range(MAX_RETRIES): # max tetrizz
        try:
            file = await bot.get_file(photo.file_id)
            photoBytes = io.BytesIO()
            await bot.download_file(str(file.file_path), photoBytes)
            photoBytes.seek(0)
            return photoBytes

        except TelegramAPIError as e:

            if attempt == MAX_RETRIES - 1:
                logg.logError(f"failed to download the photo after {MAX_RETRIES} attempts:\n{e}")
                return None
            await asyncio.sleep(RETRY_DELAY)

    return None

# command funks ya

@dp.message(Command("start"))
async def cmdStart(message: types.Message):
    """handles the start command"""

    userID = getUserID(message) # prepared for his and her story

    await message.answer(
            "hello"
            "talk to me"
    )

@dp.message(Command("help"))
async def cmdHelp(message: types.Message):
    """handles the help command"""

    helpText = \
            """
            help yourself
            """
    await message.answer(helpText)

# handle deez lats

@dp.message(F.text & ~F.command)
async def handleText(message: types.Message):
    """handle text messages""" # i cant even

    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.FIND_LOCATION)

        userID = getUserID(message)

        if message.text:

            response = await claudeController.getClouderer(
                message.text
            ) # claude be grok-king some foss ai here l8r

        else:
            response = "oh no, wait.."

        await message.answer(response)

    except TelegramAPIError as e:
        logg.logError(f"error be here in text: e", exci=True)
        await message.answer(
                "sry, i encountered an error"
                "try, try try again?"
        )

@dp.message(F.photo)
async def handlePhoto(message: types.Message):
    """handle photo messages"""

    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.RECORD_VIDEO)

        # download

        photoBytes = await downloadPhoto(message)
        if not photoBytes:
            await message.answer("sry, can't process the photo")
            return

        # convert to based
        photoB64 = base64.b64encode(photoBytes.read()).decode("UTF-8") # aka wtf-8

        # prepare statement

        # will be abstracted, i swear
        # and ye it's a threat
        messageContent = [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/jpeg",
                    "data": photoB64
                }
            }
        ]

        if message.caption:
            messageContent.append(
                    {
                        "type": "text",
                        "text": message.caption
                    }
            )
        else:
            messageContent.append(
                    {
                        "type": "text",
                        "text": "tell me what do you see"
                    }
            )

        response = ""

        await message.answer(response)

    except TelegramAPIError as e:
        logg.logError(f"error handling photo: {e}", exci=True)
        await message.answer(
                "sry, just couldn't the photo"
                "but do try try again?"
        )

async def main():

    """main funk yea"""
    logg.logInfo("ah ye")

    try:

        await dp.start_polling(bot)

    except:
        
        logg.logError("critical hit in the git")

    finally:
        
        logg.logInfo("oh, no")

if __name__ == "__main__": # oh my god its this thingy again lmao
    asyncio.run(main())
