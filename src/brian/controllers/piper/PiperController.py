from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Optional

from util.logg import logInfo, logError

from . import DotController

class PiperStatus(Enum):
    SUCCESS = "success"
    ERROR = "error"
    RETRY = "retry" # aka try retry again
    FALLBACK = "fallback"

@dataclass
class PiperResult:
    status: PiperStatus
    data: Any
    error: Optional[Exception] = None
    metadata: Optional[Dict] = None

class PiperStage(ABC):

    @abstractmethod
    async def process(self, data: Any) -> PiperResult:
        pass

    async def handleError(self, error: Exception) -> PiperResult:
        return PiperResult(
                status=PiperStatus.ERROR,
                data=None,
                error=error
        )

# main claude piper stages

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

class PiperController:

    def __init__(self):
        self.dotController = DotController() # l8r sk8r
        
        self.stages = []
        self.retryLimit = 3

    def addStage(self, stage: PiperStage):
        self.stages.append(stage)

    async def execute(self, inputData: Any) -> PiperResult:
        currentData = inputData
        retryCount = 0

        for stage in self.stages:
            while retryCount < self.retryLimit:
                result = await stage.process(currentData)

                if result.status == PiperStatus.SUCCESS:
                    currentData = result.data
                    break
                elif result.status == PiperStatus.RETRY:
                    retryCount += 1
                    continue
                elif result.status == PiperStatus.FALLBACK:
                    return await self.handleFallback(result)
                else:
                    return result

            retryCount = 0

        return PiperResult(
            status=PiperStatus.SUCCESS,
            data=currentData
        )

    async def handleFallback(self, result: PiperResult) -> PiperResult:
        return result # what we do here, is we rewrite the fallback, back, back -- iykyk


