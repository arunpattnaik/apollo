from anthropic import AsyncAnthropic
import os
class AsyncAnthropicClient:
    def __init__(self, api_key: str):
        self.chat = AsyncAnthropic(api_key=api_key)
        
client = AsyncAnthropicClient(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)