"use client";
import { cn } from "@/lib/utils";
import { Input, ScrollShadow } from "@nextui-org/react";
import { SendHorizontal } from "lucide-react";
import { FormEvent, useState } from "react";

type MainProps = {
  files: {
    folders: string[];
  };
};

export default function Main({ files }: MainProps) {
  const [value, setValue] = useState("");
  const [videoId, setVideoId] = useState("");

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch(`/api/generate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: value }),
      });
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      if (data) {
        setVideoId(data.video_id);
      }
    } catch (error) {
      console.log("Error fetching data:", error);
    }
    setValue("");
  };

  const handleFileClick = (file: string) => {
    setVideoId(file);
  };

  return (
    <main className="w-full px-10 h-screen max-h-screen flex flex-col items-center justify-center">
      <span className="flex text-xl font-semibold w-full justify-center absolute top-10">
        Generated content
      </span>
      <ScrollShadow
        size={15}
        className="w-full absolute overflow-y-scroll top-20 h-[20vh] md:h-[15vh] flex justify-center"
      >
        <div className="gap-2.5 grid grid-cols-3 px-10">
          {files.folders.map((file) => (
            <div
              onClick={() => handleFileClick(file)}
              key={file}
              className="p-2 border-[1px] rounded-xl hover:bg-neutral-200 bg-neutral-100 cursor-pointer shadow-sm"
            >
              {file}
            </div>
          ))}
        </div>
      </ScrollShadow>
      <div className="flex flex-col space-y-6 mb-24">
        {videoId ? (
          <video
            src={`http://localhost:8000/api/videos/${videoId}/`}
            className="w-full z-30 h-full mt-40 rounded-xl"
            controls
            autoPlay
          />
        ) : (
          <>
            <h2 className="text-3xl font-semibold">
              What do you want to learn today?
            </h2>
            <form onSubmit={handleSubmit}>
              <Input
                autoFocus
                size="lg"
                className="w-full max-w-xl"
                placeholder="Enter your topic"
                value={value}
                onChange={(e) => setValue(e.target.value)}
                endContent={
                  <SendHorizontal
                    onClick={handleSubmit}
                    className={cn(
                      value
                        ? "cursor-pointer"
                        : "cursor-not-allowed text-neutral-400",
                    )}
                  />
                }
              />
            </form>
          </>
        )}
      </div>
    </main>
  );
}
