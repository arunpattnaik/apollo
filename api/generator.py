import uuid
import os
import asyncio
import subprocess

from client import client
from tts import speech_client
from logger import logger
from dotenv import load_dotenv
from config import GENERATOR_PROMPT, MAX_ITERATIONS, PATH
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip, ImageClip, CompositeVideoClip
from moviepy.audio.AudioClip import AudioClip

load_dotenv()

class Generator:
    def __init__(self, scene_transcriptions):
        self.scene_transcriptions = {uuid.uuid4(): scene_transcription for scene_transcription in scene_transcriptions}
        self.video_id = str(uuid.uuid4())
    
    def get_scene_path(self, scene_id, video_id):
        return f"{GENERATIONS_PATH}/{video_id}/{scene_id}/{VIDEO_INTERNAL_PATH}"
    
    def get_audio_path(self, scene_id, video_id):
        return f"{GENERATIONS_PATH}/{video_id}/{scene_id}/audio.wav"
    
    