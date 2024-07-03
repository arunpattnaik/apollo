from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Difference Between AGI and Narrow AI", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Column Titles
        narrow_ai_title = Text("Narrow AI", font_size=36, color=BLUE).to_edge(LEFT).shift(UP*2)
        agi_title = Text("AGI", font_size=36, color=GREEN).to_edge(RIGHT).shift(UP*2)
        self.play(Write(narrow_ai_title), Write(agi_title))
        self.wait(1)

        # Narrow AI Examples
        narrow_ai_examples = VGroup(
            Text("Facial Recognition", font_size=32),
            Text("Language Translation", font_size=32),
            Text("Playing Go", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(narrow_ai_title, DOWN, buff=0.5)
        
        for example in narrow_ai_examples:
            self.play(Write(example))
            self.wait(0.5)

        # AGI Description
        agi_description = VGroup(
            Text("Versatile and Adaptable", font_size=32),
            Text("Can transfer skills between tasks", font_size=32),
            Text("Understand human emotions", font_size=32),
            Text("Help with homework and more", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(agi_title, DOWN, buff=0.5)
        
        for description in agi_description:
            self.play(Write(description))
            self.wait(0.5)

        self.wait(2)