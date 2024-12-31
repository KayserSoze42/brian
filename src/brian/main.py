import asyncio

from controllers.piper import setupBasicPiperPipe
from controllers.speech import tgram

if __name__ == "__main__":

    # piper stuff, will move each and everything just leave the mouse sir

    # i say ma'am

    # leave the mouse-ah

    piperPipe = setupBasicPiperPipe()

    # tgram init and run

    asyncio.run(tgram.main())
