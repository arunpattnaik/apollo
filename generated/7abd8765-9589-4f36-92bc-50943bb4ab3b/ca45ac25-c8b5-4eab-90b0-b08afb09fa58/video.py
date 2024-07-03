from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Building Blocks of AGI", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Pyramid base: Data
        data_layer = Rectangle(width=8, height=1, color=BLUE, fill_opacity=0.5).shift(DOWN*2.5)
        data_text = Text("Data", font_size=28).move_to(data_layer.get_center())
        self.play(FadeIn(data_layer), Write(data_text))
        self.wait(1)

        # Pyramid middle: Machine Learning Models
        ml_layer = Rectangle(width=6, height=1, color=GREEN, fill_opacity=0.5).next_to(data_layer, UP, buff=0)
        ml_text = Text("Machine Learning Models", font_size=28).move_to(ml_layer.get_center())
        self.play(FadeIn(ml_layer), Write(ml_text))
        self.wait(1)

        # Pyramid top: Advanced Capabilities
        adv_layer = Rectangle(width=4, height=1, color=RED, fill_opacity=0.5).next_to(ml_layer, UP, buff=0)
        adv_text = Text("Advanced Capabilities", font_size=28).move_to(adv_layer.get_center())
        self.play(FadeIn(adv_layer), Write(adv_text))
        self.wait(1)

        # Description of layers
        description_text = Text("""
            - At the base, we have data – lots and lots of data.
            - This data is used to train machine learning models, which form the next layer.
            - These models learn patterns and make predictions.
            - But for AGI, we need more than just pattern recognition.
            - We need reasoning, problem-solving, and even creativity.
            - The top layer of our pyramid represents these advanced capabilities.
            - Achieving AGI means integrating all these layers seamlessly.
        """, font_size=24).next_to(adv_layer, UP, buff=0.5)
        self.play(Write(description_text))
        self.wait(5)

        # End Scene
        end_text = Text("It's like building a brain from scratch!", font_size=36).next_to(adv_layer, DOWN, buff=1.5)
        self.play(Write(end_text))
        self.wait(3)
        self.wait(1)