import asyncio

from controllers.piper import PiperController, InputValStage
from controllers.speech import tgram

if __name__ == "__main__":

    # piper stuff, will move each and everything just leave the mouse sir

    # i say ma'am

    # leave the mouse-ah

    piperController = PiperController()

    piperController.addStage(InputValStage())

    # tgram init and run

    asyncio.run(tgram.main())
