from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("NVIDIA vs Groq: AI Hardware Giants", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introductory Text
        intro_text = Text(
            "Today, we're diving into an exciting comparison between two giants in the world of AI hardware: NVIDIA and Groq.",
            font_size=28,
            t2c={'NVIDIA': YELLOW, 'Groq': GREEN}
        ).next_to(title, DOWN, buff=0.5).shift(UP*0.5)
        self.play(Write(intro_text))
        self.wait(3)

        # Both companies pushing boundaries
        pushing_boundaries_text = Text(
            "Both companies are pushing the boundaries of what's possible with machine learning and artificial intelligence, but they do so in very different ways.",
            font_size=28
        ).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(pushing_boundaries_text))
        self.wait(3)

        # NVIDIA and Groq Logos
        nvidia_logo = self.create_nvidia_logo().scale(0.5).to_edge(LEFT, buff=2)
        groq_logo = self.create_groq_logo().scale(0.5).to_edge(RIGHT, buff=2)
        self.play(FadeIn(nvidia_logo), FadeIn(groq_logo))
        self.wait(3)

        # Setting the stage text
        stage_text = Text("Let's start by understanding the basics of each company's approach.", font_size=32).next_to(pushing_boundaries_text, DOWN, buff=0.5)
        self.play(Write(stage_text))
        self.wait(3)

    def create_nvidia_logo(self):
        # Create a simplified NVIDIA logo
        nvidia_logo = VGroup()
        n = Text("NVIDIA", font_size=64, color=YELLOW).move_to(ORIGIN)
        nvidia_logo.add(n)
        return nvidia_logo

    def create_groq_logo(self):
        # Create a simplified Groq logo
        groq_logo = VGroup()
        g = Text("Groq", font_size=64, color=GREEN).move_to(ORIGIN)
        groq_logo.add(g)
        return groq_logo