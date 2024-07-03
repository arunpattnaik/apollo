from manim import *

class VideoScene(Scene):
    def construct(self):
        title = Text("Matrix Multiplication", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Matrices as arrays of numbers
        matrix_A = self.create_matrix([[1, 2, 3], [4, 5, 6]], 2, 3)
        matrix_B = self.create_matrix([[7, 8], [9, 10], [11, 12]], 3, 2)
        matrix_A.next_to(ORIGIN, LEFT, buff=1.5)
        matrix_B.next_to(ORIGIN, RIGHT, buff=1.5)
        self.play(FadeIn(matrix_A), FadeIn(matrix_B))
        self.wait(1)

        # First calculation
        self.highlight_and_calculate(matrix_A, matrix_B, [1, 2, 3], [7, 9, 11], [0, 0], 58)
        self.wait(2)

        # Second calculation
        self.highlight_and_calculate(matrix_A, matrix_B, [1, 2, 3], [8, 10, 12], [0, 1], 64)
        self.wait(2)

        # Third calculation
        self.highlight_and_calculate(matrix_A, matrix_B, [4, 5, 6], [7, 9, 11], [1, 0], 139)
        self.wait(2)

        # Fourth calculation
        self.highlight_and_calculate(matrix_A, matrix_B, [4, 5, 6], [8, 10, 12], [1, 1], 154)
        self.wait(2)

        # Final result
        final_result = self.create_matrix([[58, 64], [139, 154]], 2, 2).next_to(ORIGIN, RIGHT, buff=3.5)
        self.play(FadeIn(final_result))
        self.wait(2)

        # End scene
        self.play(FadeOut(title), FadeOut(matrix_A), FadeOut(matrix_B), FadeOut(final_result))
        self.wait(1)

    def create_matrix(self, values, rows, cols):
        matrix = VGroup()
        for i in range(rows):
            row = VGroup()
            for j in range(cols):
                element = Text(str(values[i][j]), font_size=36)
                if j == 0:
                    element.next_to(ORIGIN, RIGHT)
                else:
                    element.next_to(row[j-1], RIGHT, buff=0.5)
                row.add(element)
            if i == 0:
                row.next_to(ORIGIN, DOWN)
            else:
                row.next_to(matrix[i-1], DOWN, buff=0.5)
            matrix.add(row)
        return matrix

    def highlight_and_calculate(self, matrix_A, matrix_B, row, col, pos, result):
        row_A = VGroup(*[matrix_A[pos[0]][i] for i in range(3)])
        col_B = VGroup(*[matrix_B[j][pos[1]] for j in range(3)])

        self.play(*[Indicate(elem, color=BLUE) for elem in row_A])
        self.play(*[Indicate(elem, color=RED) for elem in col_B])
        
        # Show result calculation
        calc_text = Text(
            f"{row[0]} * {col[0]} + {row[1]} * {col[1]} + {row[2]} * {col[2]} = {result}", 
            font_size=24
        ).next_to(matrix_B, DOWN)
        self.play(Write(calc_text))
        self.wait(1)
        
        # Update result matrix
        result_pos = ORIGIN + (pos[0] * DOWN + pos[1] * RIGHT) * 0.6
        result_element = Text(str(result), font_size=36).move_to(result_pos).next_to(matrix_A, RIGHT, buff=1.5).shift(DOWN*pos[0])

        self.play(Write(result_element))
        self.play(FadeOut(calc_text))