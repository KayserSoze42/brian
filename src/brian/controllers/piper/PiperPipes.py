from util import logInfo, logError

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

# popped up the dope cope pipes

async def setupBasicPiperPipe() -> PiperController:

    piper = PiperController()

    piper.addStage(InputValStage()) # staged juan

    return piper


