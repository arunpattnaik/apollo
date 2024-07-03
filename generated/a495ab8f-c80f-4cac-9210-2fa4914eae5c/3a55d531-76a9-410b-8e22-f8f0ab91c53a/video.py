from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Comparing NVIDIA GPUs and Groq's TSP", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction of NVIDIA GPUs
        nvidia_intro = Text("NVIDIA's GPUs are versatile for research and development.", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(nvidia_intro))
        self.wait(2)

        # Chart Comparing Versatility
        chart_title = Text("Versatility Comparison", font_size=36).next_to(nvidia_intro, DOWN, buff=1)
        self.play(Write(chart_title))
        self.wait(1)

        # Create bars in the chart
        nvidia_bar = Rectangle(height=3, width=1, fill_color=BLUE, fill_opacity=1).next_to(chart_title, DOWN, buff=1).shift(LEFT*2)
        groq_bar = Rectangle(height=2, width=1, fill_color=GREEN, fill_opacity=1).next_to(nvidia_bar, RIGHT, buff=1)

        nvidia_label = Text("NVIDIA", font_size=24).next_to(nvidia_bar, DOWN)
        groq_label = Text("Groq", font_size=24).next_to(groq_bar, DOWN)

        self.play(GrowFromEdge(nvidia_bar, DOWN))
        self.play(GrowFromEdge(groq_bar, DOWN))
        self.play(Write(nvidia_label), Write(groq_label))
        self.wait(2)

        # Introduction of Groq's TSP
        groq_intro = Text("Groq's TSP is optimized for speed and efficiency.", font_size=32).next_to(chart_title, DOWN, buff=3)
        self.play(Write(groq_intro))
        self.wait(2)

        # Mentioning specific scenarios
        scenarios_text = Text("Ideal for scenarios like autonomous driving and high-frequency trading.", font_size=30).next_to(groq_intro, DOWN, buff=0.5)
        self.play(Write(scenarios_text))
        self.wait(2)

        # Conclusion about strengths and use cases
        conclusion_text = Text("Each has its strengths; the best choice depends on application needs.", font_size=30).next_to(scenarios_text, DOWN, buff=1)
        self.play(Write(conclusion_text))
        self.wait(3)

        # End Scene
        self.play(FadeOut(title), FadeOut(nvidia_intro), FadeOut(chart_title), FadeOut(nvidia_bar), FadeOut(groq_bar), 
                  FadeOut(nvidia_label), FadeOut(groq_label), FadeOut(groq_intro), FadeOut(scenarios_text), FadeOut(conclusion_text))
        self.wait(1)