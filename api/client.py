import os
from groq import AsyncGroq

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))