from os import getenv

from collections import defaultdict
from typing import Union, List, Dict, Any

from anthropic import AsyncAnthropic

from util.logg import logInfo, logError
from configs.prompts import SYSTEM_GROK

class GrokController:

    def __init__(self):

        X_AI_API_KEY = getenv("X_AI_API_KEY")

        if X_AI_API_KEY is None:
            logError("error getting grok api key from ev")
            raise

        self.GROK_MODEL = "grok-2-1212" # is-even harder here for noer

        self.grokClient = AsyncAnthropic(api_key=X_AI_API_KEY, base_url="https://api.x.ai")

        self.MAX_RETRIES = 3
        self.MAX_HISTORY = 10
        self.RETRY_DELAY = 1

        self.grokConvos = defaultdict(list)

    async def getGroker(self, prompt: Union[str, List[Dict[str, Any]]]) -> str:
        """
        grok guider, hardly knower
        """

        msgs = []

        msgs.append({   
            "role": "assistant", "content": SYSTEM_GROK
        })

        msgs.append({
            "role": "user", "content": prompt
        })

        for attempt in range(self.MAX_RETRIES):
            try:
                response = await self.grokClient.messages.create(
                        model=self.GROK_MODEL,
                        max_tokens=1024,
                        messages=msgs
                )
                grokResponse = ""
                for content in response.content:
                    if hasattr(content, 'type') and content.type == 'text':
                        grokResponse = content.text

                    return grokResponse
            except Exception as e:
                if attempt == self.MAX_RETRIES - 1:
                    logError(f"failed to communicate with gRoK after {self.MAX_RETRIES} attempts: {e}")
                    raise

        return "sry, not sry v3"
