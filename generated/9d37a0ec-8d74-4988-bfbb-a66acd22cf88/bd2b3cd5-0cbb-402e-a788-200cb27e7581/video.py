from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Identity and Inverse Matrices", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Identity Matrix Description
        identity_intro = Text("The Identity Matrix is like the number 1 in matrix algebra.", font_size=28).next_to(title, DOWN, buff=0.5)
        self.play(Write(identity_intro))
        self.wait(2)

        # Display Identity Matrix
        identity_matrix = Text("I = [[1, 0], [0, 1]]", font_size=28).next_to(identity_intro, DOWN, buff=1.5)
        self.play(Write(identity_matrix))
        self.wait(2)

        # Inverse Matrix Description
        inverse_intro = Text("The Inverse Matrix is like the reciprocal of a number.", font_size=28).next_to(identity_matrix, DOWN, buff=0.5)
        self.play(Write(inverse_intro))
        self.wait(2)

        # Display Example Matrix and Its Inverse
        example_matrix = Text("M = [[4, 7], [2, 6]]", font_size=28).shift(UP*0.5).to_edge(LEFT, buff=1)
        inverse_matrix = Text("M^-1 = [[0.6, -0.7], [-0.2, 0.4]]", font_size=28).next_to(example_matrix, RIGHT, buff=1)
        self.play(Write(example_matrix), Write(inverse_matrix))
        self.wait(2)

        # Display their Product
        product_matrix = Text("M * M^-1 = I", font_size=28).move_to(DOWN*2)
        self.play(Write(product_matrix))
        self.wait(2)

        # Explain the importance
        importance_text = Text("Multiplying a matrix by its inverse gives the identity matrix.", font_size=28).next_to(product_matrix, DOWN, buff=0.5)
        self.play(Write(importance_text))
        self.wait(3)