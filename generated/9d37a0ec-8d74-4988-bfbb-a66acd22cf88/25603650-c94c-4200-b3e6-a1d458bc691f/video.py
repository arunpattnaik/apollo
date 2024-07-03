from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Scalar Multiplication", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Scalar multiplication description
        description = Text("Multiplying each element of a matrix by a scalar", font_size=30).next_to(title, DOWN)
        self.play(Write(description))
        self.wait(2)

        # Original matrix
        original_matrix = self.matrix_obj([[1, 2], [3, 4]], LEFT * 2)
        original_label = Text("Original Matrix", font_size=24).next_to(original_matrix, DOWN)
        self.play(Write(original_matrix), Write(original_label))
        self.wait(2)

        # Scalar to multiply by
        scalar_text = Text("Scalar: 3", font_size=36).next_to(original_matrix, RIGHT, buff=1)
        self.play(Write(scalar_text))
        self.wait(1)

        # Resulting matrix
        resulting_matrix = self.matrix_obj([[3, 6], [9, 12]], RIGHT * 2)
        resulting_label = Text("Resulting Matrix", font_size=24).next_to(resulting_matrix, DOWN)
        self.play(Write(resulting_matrix), Write(resulting_label))
        self.wait(2)

        # Arrow from original to resulting matrix
        arrow = Arrow(original_matrix.get_right(), resulting_matrix.get_left(), buff=0.5)
        self.play(GrowArrow(arrow))
        self.wait(2)

        # Scaling analogy
        analogy_text = Text("Scaling the Matrix", font_size=36).to_edge(DOWN)
        self.play(Write(analogy_text))
        self.wait(3)

        # End Scene
        self.play(FadeOut(title), FadeOut(description), FadeOut(original_matrix), FadeOut(original_label),
                  FadeOut(scalar_text), FadeOut(resulting_matrix), FadeOut(resulting_label), FadeOut(arrow),
                  FadeOut(analogy_text))
        self.wait(1)

    def matrix_obj(self, values, position):
        rows = len(values)
        cols = len(values[0])
        elements = VGroup(*[Text(str(values[i][j]), font_size=36) for i in range(rows) for j in range(cols)])
        elements.arrange_in_grid(rows, cols, buff=1).move_to(position)
        bracket_y = max([ele.get_y() for ele in elements]) - min([ele.get_y() for ele in elements])
        bracket_x = max([ele.get_x() for ele in elements]) - min([ele.get_x() for ele in elements])
        left_bracket = Line(start=[-0.5, -bracket_y/2, 0], end=[-0.5, bracket_y/2, 0], stroke_width=4)
        right_bracket = Line(start=[bracket_x/2 + 0.5, -bracket_y/2, 0], end=[bracket_x/2 + 0.5, bracket_y/2, 0], stroke_width=4)
        brackets = VGroup(left_bracket, right_bracket).move_to(position)
        return VGroup(elements, brackets)