from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("The Exciting World of Large Language Models", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to prompt
        intro_text = Text(
            "One exciting aspect of large language models is their ability to generate human-like text.",
            font_size=32
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Example prompt and generated text
        example_prompt = Text(
            "For example, if you give the model a prompt like:", font_size=28
        ).next_to(intro_text, DOWN, buff=0.5)
        prompt_text = Text(
            "'Once upon a time,'", font_size=32, color=BLUE
        ).next_to(example_prompt, DOWN, buff=0.3)
        generated_text = Text(
            "it can continue the story in a coherent and creative way.", font_size=28
        ).next_to(prompt_text, DOWN, buff=0.3)
        
        self.play(Write(example_prompt))
        self.wait(1)
        self.play(Write(prompt_text))
        self.wait(1)
        self.play(Write(generated_text))
        self.wait(2)

        # Visualizing the training process
        training_text = Text(
            "This is possible because the model has learned from vast amounts of text data,", font_size=28
        ).next_to(generated_text, DOWN, buff=0.5)
        nuance_text = Text(
            "capturing the nuances of language, grammar, and even some level of common sense.", font_size=28
        ).next_to(training_text, DOWN, buff=0.3)
        
        self.play(Write(training_text))
        self.wait(2)
        self.play(Write(nuance_text))
        self.wait(2)

        # Adding a visual representation of model learning
        brain_image = self.create_brain().scale(0.8).shift(DOWN*1)
        text_data_image = self.create_text_data().scale(0.8).shift(DOWN*2.2)
        arrows = VGroup(
            Arrow(start=brain_image.get_top(), end=text_data_image.get_center(), buff=0.3, color=YELLOW),
            Arrow(start=text_data_image.get_left(), end=brain_image.get_left(), buff=0.3, color=YELLOW),
            Arrow(start=text_data_image.get_right(), end=brain_image.get_right(), buff=0.3, color=YELLOW)
        )
        
        self.play(FadeIn(brain_image), FadeIn(text_data_image))
        self.play(*[GrowArrow(arrow) for arrow in arrows])
        self.wait(3)

    def create_brain(self):
        brain = VGroup()
        brain_outline = Circle(radius=1, color=GRAY, fill_color=WHITE, fill_opacity=1)
        details = VGroup()
        for _ in range(3):
            detail = Line(ORIGIN, RIGHT*0.5, color=GRAY).shift(DOWN*0.2 + LEFT*0.5 + UP*0.2 * _)
            details.add(detail)
        brain.add(brain_outline, details)
        return brain

    def create_text_data(self):
        text_data = VGroup()
        text_data.add(Text("Text Data 1", font_size=24).shift(UP))
        text_data.add(Text("Text Data 2", font_size=24))
        text_data.add(Text("Text Data 3", font_size=24).shift(DOWN))
        return text_data