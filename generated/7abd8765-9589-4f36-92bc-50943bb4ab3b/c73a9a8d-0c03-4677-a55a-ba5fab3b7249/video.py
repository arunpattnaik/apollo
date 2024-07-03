from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Challenges in Creating AGI", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Brain illustration
        brain_image = self.create_brain().scale(2).shift(UP)
        self.play(FadeIn(brain_image))
        self.wait(1)

        # Highlight different brain regions
        memory_region = self.create_brain_region("Memory", color=BLUE, position=3*LEFT + UP)
        language_region = self.create_brain_region("Language", color=GREEN, position=RIGHT + 2*UP)
        decision_region = self.create_brain_region("Decision-making", color=RED, position=RIGHT + 0.5*DOWN)

        self.play(FadeIn(memory_region), FadeIn(language_region), FadeIn(decision_region))
        self.wait(1)

        # Explanation of brain regions
        memory_text = Text("Memory", font_size=24).next_to(memory_region, LEFT)
        language_text = Text("Language", font_size=24).next_to(language_region, RIGHT)
        decision_text = Text("Decision-making", font_size=24).next_to(decision_region, RIGHT)

        self.play(Write(memory_text), Write(language_text), Write(decision_text))
        self.wait(2)

        # Researchers are studying these regions
        study_text = Text("Researchers are studying these regions to understand how they work together.", font_size=24).shift(DOWN * 2.5)
        self.play(Write(study_text))
        self.wait(2)

        # Mimicking processes
        mimicking_text = Text("By mimicking these processes, we hope to create machines that can think and learn like humans.", font_size=24).next_to(study_text, DOWN, buff=0.5)
        self.play(Write(mimicking_text))
        self.wait(2)

        # Puzzle analogy
        puzzle_text = Text("It's a bit like trying to solve a giant, complex puzzle.", font_size=24).next_to(mimicking_text, DOWN, buff=0.5)
        self.play(Write(puzzle_text))
        self.wait(2)

    def create_brain(self):
        brain = VGroup()
        brain.add(
            Ellipse(width=4, height=5, color=WHITE, fill_opacity=0.3)
        )
        return brain

    def create_brain_region(self, label, color, position):
        region = VGroup()
        region.add(
            Circle(radius=0.5, color=color, fill_opacity=0.8).move_to(position)
        )
        region.add(
            Text(label, font_size=18, color=BLACK).move_to(position)
        )
        return region