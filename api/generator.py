import uuid
import os
import asyncio
import subprocess

from api.client import client
from api.tts import speech_client
from api.logger import logger
from dotenv import load_dotenv
from api.config import GENERATOR_PROMPT, MAX_ITERATIONS, PATH, VOICE_ID, LLM_MODEL
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip, ImageClip, CompositeVideoClip
from moviepy.audio.AudioClip import AudioClip

load_dotenv()

VIDEO_INTERNAL_PATH = "videos/video/480p15/video.mp4"

class Generator:
    def __init__(self, scene_transcriptions):
        self.scene_transcriptions = {uuid.uuid4(): scene_transcription for scene_transcription in scene_transcriptions}
        self.video_id = str(uuid.uuid4())
    
    def get_scene_path(self, scene_id, video_id):
        return f"{PATH}/{video_id}/{scene_id}/{VIDEO_INTERNAL_PATH}"
    
    def get_audio_path(self, scene_id, video_id):
        return f"{PATH}/{video_id}/{scene_id}/audio.wav"
    
    def render_scene(self, scene_id):
        command = f"manim render -ql {PATH}/{self.video_id}/{scene_id}/video.py -o video --media_dir {PATH}/{self.video_id}/{scene_id}"
        
        print(f"Running command: {command}")

        try:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            logger.info(f"Command output: {result.stdout}")
            return True, ""
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.strip()
            return False, f"Command failed with exit code {e.returncode}. Error: {error_message}"
        except Exception as e:
            return False, str(e)
    
    async def generate_speech(self, scene_id, video_id):
        """
        Generates speech for the scene with the given scene id
        :param scene_id: Scene id (string)
        :param video_id: Video id (string)
        """
        scene_transcription = self.scene_transcriptions[scene_id]
        synthesis = await speech_client.synthesize(scene_transcription, voice=VOICE_ID, format='wav', temperature=0.3)
        audio_path = f"{PATH}/{video_id}/{scene_id}/audio.wav"
        if not os.path.exists(f"{PATH}/{video_id}/{scene_id}"):
            os.makedirs(f"{PATH}/{video_id}/{scene_id}")
        with open(audio_path, 'wb') as audio_file:
            audio_file.write(synthesis['audio'])
        
        logger.info(f"Successfully generated speech for scene {scene_id}")
        return scene_id
    
    async def generate_manim(self, scene_id):
        """
        Generates manim code from the scene description
        :param scene_description: Scene description (string)
        :return: scene_id (string)
        """
        iteration = 0
        scene_transcription = self.scene_transcriptions[scene_id]
        messages = [{
            "role": "system", "content": GENERATOR_PROMPT
        }, {
            "role": "user", "content": scene_transcription
        }]

        while iteration < MAX_ITERATIONS:
            response = await client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages
            )
            logger.info(f"Generated response: {response}")
            
            # get output from last message
            output = response.choices[0].message.content

            # strip code block markdown
            output = output.strip("```")

            logger.info(f"Generated code: {output}")

            # append output to messages
            messages.append({"role": "assistant", "content": output})

            # put code in a file
            try:
                if not os.path.exists(f"{PATH}/{self.video_id}/{scene_id}"):
                    os.makedirs(f"{PATH}/{self.video_id}/{scene_id}")
                with open(f"{PATH}/{self.video_id}/{scene_id}/video.py", "w") as f:
                    f.write(output)
            except Exception as e:
                logger.error(f"Error writing to file: {e}")
                return None

            render_output = self.render_scene(scene_id)

            logger.info(f"Status for scene {scene_id}: {render_output}")

            # note render_output is either True or (False, string)
            if render_output[0]:
                logger.info(f"Scene {scene_id} was rendered successfully")
                return scene_id
            
            # scene was not rendered successfully
            # add error message to messages
            messages.append({"role": "user", "content": f"Error: {render_output[1]}"})
            iteration += 1
            
        return None
    
    def combine_manim_and_speech(self, scene_id, video_id):
        """
        Combines the manim code and speech synthesis for the scene with the given scene id
        :param scene_id: Scene id (string)
        :param manim_result: Manim code (string)
        :param speech_result: Speech synthesis (string)
        """
        scene_path = self.get_scene_path(scene_id, video_id)
        audio_path = self.get_audio_path(scene_id, video_id)

        video = VideoFileClip(scene_path)
        audio = AudioFileClip(audio_path)

        # Get durations
        video_duration = video.duration
        audio_duration = audio.duration

        logger.info(f"Video duration: {video_duration}, Audio duration: {audio_duration}")

        # If audio is shorter than video, append silence
        if audio_duration < video_duration:
            silence_duration = video_duration - audio_duration
            silence = AudioClip(lambda t: 0, duration=silence_duration)
            audio = CompositeAudioClip([audio, silence.set_start(audio_duration)])
        
        # If audio is longer than video, extend the video by holding the last frame
        elif audio_duration > video_duration:
            logger.warning("Audio is longer than video, extending video by holding the last frame")
            last_frame = video.get_frame(video_duration - 0.1)
            frozen_clip = ImageClip(last_frame).set_duration(audio_duration - video_duration)
            video = CompositeVideoClip([video, frozen_clip.set_start(video_duration)])
            video = video.set_duration(audio_duration)

        # Ensure both clips have the same duration
        final_duration = min(video.duration, audio.duration)
        video = video.subclip(0, final_duration)
        audio = audio.subclip(0, final_duration)

        # Composite the video with the audio
        final_clip = video.set_audio(audio)

        # Write the final video with audio
        # wipe scene file
        os.remove(scene_path)

        final_clip.write_videofile(scene_path, codec="libx264")

        # Step 3: Profit
        # Close the clips to free up system resources
        video.close()
        audio.close()
        final_clip.close()

        logger.info(f"Successfully added audio to scene {scene_id}")
        
    def combine_video_scenes(self):
        """
        Combines all the video scenes into a single video
        """
        scene_ids = []
        video_clips = []

        for scene_id in self.scene_transcriptions.keys():
            scene_path = self.get_scene_path(scene_id, self.video_id)
            if os.path.exists(scene_path):
                video_clips.append(VideoFileClip(scene_path))
                scene_ids.append(scene_id)
            else:
                logger.error(f"Video file does not exist at path: {scene_path}")

        if not video_clips:
            logger.error("No scenes were successfully generated.")
            return None

        final_video = concatenate_videoclips(video_clips)
        final_video_path = f"{PATH}/{self.video_id}/final_video.mp4"
        final_video.write_videofile(final_video_path, codec="libx264")

        logger.info(f"Final video path: {final_video_path}")
        return final_video_path

    async def generate_all_scenes(self):
        """
        Generates manim code for all scenes and stitches them together into a single video.
        :return: Path to the final stitched video.
        """
        tasks = []
        for scene_id, transcription in self.scene_transcriptions.items():
            manim_task = asyncio.create_task(self.generate_manim(scene_id))
            speech_task = asyncio.create_task(self.generate_speech(scene_id, self.video_id))
            tasks.append((manim_task, speech_task))

        # Wait for all tasks to complete
        results = await asyncio.gather(*(asyncio.gather(*task_pair[:2]) for task_pair in tasks))

        logger.info(f"Results: {results}")

        for (manim_result, speech_result), scene_id in zip(results, self.scene_transcriptions.keys()):
            if manim_result is None or speech_result is None:
                logger.error(f"Scene {scene_id} was not generated successfully")
                continue
            self.combine_manim_and_speech(scene_id, self.video_id)

        self.combine_video_scenes()
        return self.video_id

async def main():
    examples = [
        "Welcome everyone! Today we're diving into a topic that can often be a source of excitement and curiosity for many: how to start investing in stocks. Have you ever wondered how people make money in the stock market or felt overwhelmed by where to begin? That's exactly what we'll cover today. Let's break it down to understand what stocks are, why you might want to invest in them, and how to get started. Before we start, imagine the screen displaying a bustling stock exchange floor, with numbers and charts constantly changing. That's the essence of why we need to talk about stocks.",
        
        "First, let's discuss the concept of 'stocks'. In the context of investing, a stock represents a share in the ownership of a company. When you own a stock, you own a piece of that company. Stocks are also known as equities. Imagine the screen showing an image of a certificate labeled 'Stock Ownership' and another image showing different company logos. Investing in stocks means you are buying a small part of a company with the hope that the company grows and becomes more valuable over time.",
        
        "So, how do you actually start investing in stocks? The first step is to open a brokerage account. This is an account that allows you to buy and sell stocks. There are many online brokers to choose from, each offering different features and fee structures. Imagine the screen showing a list of popular online brokerage platforms with checkmarks next to features like 'Low Fees', 'User-Friendly Interface', and 'Educational Resources'. Once you've chosen a broker, you can fund your account by transferring money from your bank account.",
        
        "Now, let's get to the heart of why investing in stocks can be rewarding. Many times, the potential for growth and income is what attracts investors. For example, when you buy stocks of a company that grows over time, the value of your shares increases, and you can make a profit by selling them at a higher price. Imagine the screen showing a graph of a stock's price rising over several years, highlighting points where an investor could buy low and sell high. Additionally, some companies pay dividends, which are a share of the profits distributed to shareholders. This can provide a steady income stream on top of any capital gains.",
        
        "Finally, let's wrap up with some practical tips. One common approach to start investing is to diversify your portfolio, which means spreading your investments across different stocks to reduce risk. On the screen, we show a pie chart illustrating a diversified portfolio with slices representing different industries like technology, healthcare, and finance. It's also important to do your research and understand the companies you're investing in. Many brokers offer tools and resources to help you make informed decisions. By understanding the basics and starting with a solid plan, you'll be well on your way to successful investing. Thanks for joining me today, and happy investing!"
    ]

    sg = Generator(examples)
    await sg.generate_all_scenes()

if __name__ == "__main__":
    asyncio.run(main())