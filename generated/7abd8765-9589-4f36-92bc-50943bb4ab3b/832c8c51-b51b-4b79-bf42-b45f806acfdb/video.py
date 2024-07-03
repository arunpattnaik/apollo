from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Future and Ethical Considerations of AGI", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Timeline Base
        timeline = Line(LEFT * 5 + DOWN * 2, RIGHT * 5 + DOWN * 2)
        self.play(Create(timeline))
        
        # First AGI Prototype
        agi_prototype = Text('First AGI Prototype', font_size=24).next_to(timeline, UP, buff=0.5).shift(LEFT * 3)
        agi_prototype_dot = Dot(agi_prototype.get_bottom(), color=RED)
        self.play(FadeIn(agi_prototype), Create(agi_prototype_dot))

        # AGI in Everyday Life
        agi_everyday = Text('AGI in Everyday Life', font_size=24).next_to(timeline, UP, buff=0.5).shift(RIGHT * 3)
        agi_everyday_dot = Dot(agi_everyday.get_bottom(), color=RED)
        self.play(FadeIn(agi_everyday), Create(agi_everyday_dot))

        self.wait(2)

        # Potential Benefits
        benefits_text = Text("Potential Benefits of AGI", font_size=32).to_edge(LEFT).shift(UP * 0.5)
        self.play(Write(benefits_text))

        medicine_benefit = Text("Medicine", font_size=28, color=BLUE).next_to(benefits_text, DOWN, buff=0.5).shift(RIGHT * 0.5)
        education_benefit = Text("Education", font_size=28, color=BLUE).next_to(medicine_benefit, DOWN, buff=0.5)
        self.play(Write(medicine_benefit), Write(education_benefit))

        self.wait(2)

        # Ethical Considerations
        ethical_text = Text("Ethical Considerations", font_size=32).to_edge(RIGHT).shift(UP * 0.5)
        self.play(Write(ethical_text))

        decisions_concern = Text("AGI Decisions", font_size=28, color=YELLOW).next_to(ethical_text, DOWN, buff=0.5).shift(LEFT * 0.5)
        human_values_concern = Text("Aligning with Human Values", font_size=28, color=YELLOW).next_to(decisions_concern, DOWN, buff=0.5)
        self.play(Write(decisions_concern), Write(human_values_concern))

        self.wait(2)

        # Ending
        thanks_text = Text("Thanks for joining me today,\nand I can't wait to see where your curiosity takes you next!", font_size=36).to_edge(DOWN)
        self.play(Write(thanks_text))
        self.wait(3)