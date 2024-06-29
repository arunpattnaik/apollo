"use client";
import { cn } from "@/lib/utils";
import { Input } from "@nextui-org/react";
import { SendHorizontal } from "lucide-react";
import { FormEvent, useState } from "react";

export default function Home() {
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

  return (
    <main className="w-full px-10 h-screen max-h-screen flex items-center justify-center">
      <div className="flex flex-col space-y-6 mb-24">
        {videoId ? (
          <video
            src={`http://localhost:8000/api/videos/${videoId}/`}
            className="w-full h-full rounded-xl"
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
