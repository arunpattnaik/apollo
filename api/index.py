import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from api.transcriber import Transcriber
from api.generator import Generator
from fastapi.responses import StreamingResponse

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    text: str

@app.get("/api/python")
def root():
    return {"message": "Apollo, live!"}

@app.post("/api/generate")
async def generate(request: VideoRequest):
    text = request.text
    transcriber = Transcriber()
    transcriptions = await transcriber.generate(text, emotions="enthusiastic")
    generator = Generator(transcriptions)
    video_id = await generator.generate_all_scenes()
    return {"video_id": video_id, "text": "\n".join(transcriptions)}

@app.get("/api/videos/{video_id}")
async def get_video(video_id: str):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_directory, ".."))
    video_path = os.path.join(project_root, "generated", video_id, "final_video.mp4")
    def iterfile():
        with open(video_path, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="video/mp4")