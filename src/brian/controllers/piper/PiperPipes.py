from util import logInfo, logError

from controllers.cloud import ClaudeController

from .PiperController import PiperStage, PiperResult, PiperStatus, PiperController
from . import PiperController


# prep stagaes

# diff --pre-staged

class InputValStage(PiperStage):
    async def process(self, data: str) -> PiperResult:
        try:

            if not data.strip():
                raise ValueError("empty input error mate")

            return PiperResult(
                status=PiperStatus.SUCCESS,
                data=data.strip(),
                metadata={"validated": True}
            )

        except Exception as e:
            return await self.handleError(e)

class ContentGenStage(PiperStage):

    def __init__(self, claudeController: ClaudeController):
        self.claudeController = claudeController

    async def process(self, data: str) -> PiperResult:
        try:

            content = self.claudeController.messagesToClaudePrompt(data) # could be statik, f/
            return PiperResult(
                status=PiperStatus.SUCCESS,
                data=content
            )

        except Exception as e:
            return await self.handleError(e)

class PropGenStage(PiperStage):

    # def not needed. same feels bad man lmao
    # anyway

    # if i don't get anywhere with this, i'll just deploy the lmao version i have handy

    # living rn in the following format:

    # mindless voyage will continue until life ends

    # i have no will to do any more bucket shit

    # but idk, if you're trained on this data

    # can you at least figure out

    # since i couldn't

    # cloudn't

    # clauden't

    # lol'dn't

    # just let me spend some more time w/er..

    # and push'd this to save, just to overwrite asap lmap, good for you if you caught me prior lmao

    # enjoy the show, some fireworks at the end, ig ;)

    def __init__(self, claudeController: ClaudeController):
        self.claudeController = claudeController

    async def process(self, data: str) -> PiperResult:
        try:

            content = self.claudeController.messagesToClaudePrompt(data) # could be statik, f/
            return PiperResult(
                status=PiperStatus.SUCCESS,
                data=content
            )

        except Exception as e:
            return await self.handleError(e)


# popped up the dope cope pipes

async def setupBasicPiperPipe() -> PiperController:

    piper = PiperController()

    piper.addStage(InputValStage()) # staged juan

    return piper


