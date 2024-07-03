from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Matrix Addition", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Matrix A
        matrix_A = MobjectTable(
            [[Text("2"), Text("3")],
             [Text("4"), Text("1")]],
            include_outer_lines=True,
            h_buff=1,
            v_buff=1
        ).shift(LEFT*3 + UP*1)
        matrix_A_label = Text("A=").next_to(matrix_A, LEFT)
        self.play(FadeIn(matrix_A), Write(matrix_A_label))
        self.wait(1)

        # Matrix B
        matrix_B = MobjectTable(
            [[Text("1"), Text("2")],
             [Text("3"), Text("4")]],
            include_outer_lines=True,
            h_buff=1,
            v_buff=1
        ).shift(RIGHT*3 + UP*1)
        matrix_B_label = Text("B=").next_to(matrix_B, LEFT)
        self.play(FadeIn(matrix_B), Write(matrix_B_label))
        self.wait(1)

        # Plus sign
        plus = Text("+").move_to(UP*1)
        self.play(Write(plus))
        self.wait(1)
        
        # Highlighting the matrix elements
        self.highlight_addition(matrix_A, matrix_B)
        self.wait(2)
        
        # Resulting Matrix C
        result_matrix = MobjectTable(
            [[Text("3"), Text("5")],
             [Text("7"), Text("5")]],
            include_outer_lines=True,
            h_buff=1,
            v_buff=1
        ).shift(DOWN*2)
        result_matrix_label = Text("A + B = ").next_to(result_matrix, LEFT)
        self.play(FadeIn(result_matrix), Write(result_matrix_label))
        self.wait(2)

    def highlight_addition(self, matrix_A, matrix_B):
        arrows = VGroup()
        for i in range(2):
            for j in range(2):
                a_element = matrix_A.get_cell((i, j))
                b_element = matrix_B.get_cell((i, j))
                a_copy = a_element.copy().set_color(YELLOW)
                b_copy = b_element.copy().set_color(YELLOW)
                
                self.play(Transform(a_element.copy(), a_copy))
                self.play(Transform(b_element.copy(), b_copy))
                self.wait(0.5)
        self.wait(2)