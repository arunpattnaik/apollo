import json
import asyncio
import os

from client import client
from logger import logger
from config import LLM_MODEL, TRANSCRIBER_PROMPT_TEMPLATE, MAX_ITERATIONS

class Transcriber:
    def __init__(self):
        self.scenes = []
    
    def populate_transcriptions_array(self, transcriptions):
        transcriptions_split_left = '[' + '['.join(transcriptions.split('[')[1:])
        transcriptions_split_right = ']'.join(transcriptions_split_left.split(']')[:-1]) + ']'
        self.scenes = list(json.loads(transcriptions_split_right))
    
    async def generate(self, topic, emotions):
        iteration = 0
        messages = [{
            "role": "system", "content": TRANSCRIBER_PROMPT_TEMPLATE.substitute(emotions=emotions)
        }, {
            "role": "user", "content": topic
        }]
        
        while iteration < MAX_ITERATIONS:
            response = await client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages,
                temperature=round(iteration/MAX_ITERATIONS, 1)
            )            
            output = response.choices[0].message.content.strip().strip('python').strip("```")

            logger.info(f"Generated transcript: {output}")

            messages.append({"role": "assistant", "content": output})
            try:
                self.scene_transcriptions = list(json.loads(output))
                return self.scene_transcriptions
            except Exception as e:
                try:
                    self.populate_transcriptions_array(output)
                    return 
                except Exception as e:
                    messages.append({"role": "user", "content": f"Error: Did not follow correct format. Please create an array of strings for scenes."})
            iteration += 1

if __name__ == "__main__":
    topic = input("Enter user topic: ")
    transcriber = Transcriber()
    asyncio.run(transcriber.generate(topic, "happy"))
    logger.info(transcriber.scene_transcriptions)