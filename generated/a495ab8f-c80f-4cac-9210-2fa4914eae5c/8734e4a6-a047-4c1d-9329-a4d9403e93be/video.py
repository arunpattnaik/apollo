from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Summary of NVIDIA vs Groq", font_size=46).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Comparisons
        nvidia_header = Text("NVIDIA GPUs", font_size=40, color=BLUE).to_edge(LEFT, buff=1).shift(DOWN*1)
        groq_header = Text("Groq TSP", font_size=40, color=GREEN).to_edge(RIGHT, buff=1).shift(DOWN*1)
        
        self.play(Write(nvidia_header), Write(groq_header))
        self.wait(1)

        # NVIDIA points
        nvidia_points = VGroup(
            Text("Versatile", font_size=30),
            Text("Broad applicability", font_size=30),
            Text("Supports wide range of AI models", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(nvidia_header, DOWN, buff=0.5)

        # Groq points
        groq_points = VGroup(
            Text("High performance", font_size=30),
            Text("Specialized solutions", font_size=30),
            Text("Efficiency in specific tasks", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(groq_header, DOWN, buff=0.5)

        self.play(Write(nvidia_points), Write(groq_points))
        self.wait(2)

        # Conclusion
        conclusion_text = Text(
            "Understanding these differences can help you make informed decisions about which technology to use for your AI projects.",
            font_size=32,
            color=YELLOW
        ).shift(DOWN*1.5)
        self.play(Write(conclusion_text))
        self.wait(2)

        # Ending text
        thanks_text = Text(
            "Thanks for joining me today!",
            font_size=36
        ).next_to(conclusion_text, DOWN, buff=1)

        hope_text = Text(
            "I hope you found this comparison as fascinating as I did!",
            font_size=36
        ).next_to(thanks_text, DOWN, buff=0.5)

        self.play(Write(thanks_text))
        self.play(Write(hope_text))
        self.wait(3)