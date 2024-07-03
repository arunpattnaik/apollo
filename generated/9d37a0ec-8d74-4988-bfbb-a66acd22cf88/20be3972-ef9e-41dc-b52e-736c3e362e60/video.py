from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Welcome to Matrix Algebra", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text = Text("Imagine matrices as a way to organize and manipulate data,", font_size=24).next_to(title, DOWN, buff=0.5)
        intro_text_2 = Text("like a spreadsheet but with superpowers.", font_size=24).next_to(intro_text, DOWN, buff=0.3)
        self.play(Write(intro_text), Write(intro_text_2))
        self.wait(2)

        # Introduction to 2x2 matrix
        matrix_intro_text = Text("Let's start with the basics.", font_size=30).next_to(intro_text_2, DOWN, buff=1.0)
        self.play(Write(matrix_intro_text))
        self.wait(1)

        # Simple 2x2 matrix
        matrix_elements = [
            [Text("a11"), Text("a12")], 
            [Text("a21"), Text("a22")]
        ]
        grid = VGroup(
            *[
                VGroup(*matrix_elements[i]).arrange(RIGHT, buff=0.5)
                for i in range(2)
            ]
        ).arrange(DOWN, buff=0.5).scale(1.2).to_edge(LEFT, buff=1.5)
        self.play(FadeIn(grid))
        self.wait(1)

        # Elements annotation
        element_positions = {
            "a11": matrix_elements[0][0],
            "a12": matrix_elements[0][1],
            "a21": matrix_elements[1][0],
            "a22": matrix_elements[1][1]
        }

        element_annotations = VGroup(
            *[Text(position, font_size=28).set_color(BLUE).next_to(element, DOWN) 
              for position, element in element_positions.items()]
        )

        # Display the elements
        for element in element_annotations:
            self.play(Write(element))
        
        self.wait(2)

        # Ready to explore more? Let's go!
        ready_text_1 = Text("Ready to explore more?", font_size=34).shift(DOWN*2.5)
        ready_text_2 = Text("Let's go!", font_size=34).next_to(ready_text_1, DOWN)
        self.play(Write(ready_text_1))
        self.play(Write(ready_text_2))
        self.wait(3)