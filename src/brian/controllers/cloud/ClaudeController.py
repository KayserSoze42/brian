from os import getenv

from collections import defaultdict
from typing import Union, List, Dict, Any

from anthropic import AsyncAnthropic

from brian.util.logg import logInfo, logError
from brian.configs.prompts import SYSTEM_CLAUDE

class ClaudeController:

    def __init__(self):
        print("heyo")

        self.ANTHROPIC_API_KEY = getenv("ANTHROPIC_API_KEY")

        if getenv("ANTHROPIC_API_KEY") is None:
            logError("error getting grok api key from ev")
            raise

        self.CLAUDE_MODEL = "claude-3-haiku-20240307" # we go hardcode for noe

        self.MAX_RETRIES = 3
        self.MAX_HISTORY = 10
        self.RETRY_DELAY = 1

        self.conversations = defaultdict(list)

        self.claudeClient = AsyncAnthropic(api_key=self.ANTHROPIC_API_KEY)

    async def getClouderer(self, prompt: Union[str, List[Dict[str, Any]]]) -> str:
        """
        idk, juju voodoo ppl
        """

        msgs = []

        msgs.append({
            "role": "user",
            "content": prompt
            })

        for attempt in range(self.MAX_RETRIES):

            try:
                logInfo(f"try try {attempt}")
                response = await self.claudeClient.messages.create(
                        model=self.CLAUDE_MODEL,
                        max_tokens=1024,
                        system=SYSTEM_CLAUDE,
                        messages=msgs
                        )

                claudeResponse = ""

                for content in response.content:
                    if hasattr(content, 'type') and content.type == 'text':
                        claudeResponse = content.text

                    return claudeResponse

            except Exception as e:
                if attempt == self.MAX_RETRIES - 1:
                    logError(f"failed to communicate with cLaUdEv2 after {self.MAX_RETRIES} attempts: {e}")
                    raise

        return "sry, not sry v1"

        
