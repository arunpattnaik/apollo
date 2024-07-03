from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Welcome to the World of NBA Basketball!", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text = Text("What makes NBA basketball so thrilling?", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # Show basketball court
        court = self.create_basketball_court().scale(3).shift(DOWN*0.5)
        self.play(FadeIn(court))
        self.wait(1)

        # Explain court sections
        midcourt_line = Line(court.get_left(), court.get_right(), color=YELLOW)
        self.play(Create(midcourt_line))
        self.wait(1)

        court_text = Text("Court Divided by Midcourt Line", font_size=28).next_to(midcourt_line, UP, buff=1)
        self.play(Write(court_text))
        self.wait(1)

        # Explain scoring and defending
        basket_text_left = Text("Defend", font_size=24).next_to(court.get_left(), LEFT, buff=1)
        basket_text_right = Text("Score", font_size=24).next_to(court.get_right(), RIGHT, buff=1)
        self.play(Write(basket_text_left), Write(basket_text_right))
        self.wait(2)

        # Simplified game objective
        objective_text = Text("Objective: Score more points than the opponent", font_size=28).shift(DOWN*3)
        self.play(Write(objective_text))
        self.wait(2)

        # More excitement to the game
        more_text = Text("But there's so much more to it than that!", font_size=32).next_to(objective_text, DOWN, buff=0.5)
        self.play(Write(more_text))
        self.wait(2)

    def create_basketball_court(self):
        court = VGroup()
        # Court outline
        court_outline = Rectangle(width=10, height=5, color=WHITE)
        court.add(court_outline)

        # Midcourt line
        midcourt_line = Line(court_outline.get_top(), court_outline.get_bottom(), color=YELLOW)
        court.add(midcourt_line)

        # Hoops
        left_hoop = Circle(radius=0.3, color=RED).shift(LEFT*5)
        right_hoop = Circle(radius=0.3, color=RED).shift(RIGHT*5)
        court.add(left_hoop, right_hoop)

        # Paint areas
        left_paint = VGroup(
            Line(LEFT*4 + UP*1.5, LEFT*4 + DOWN*1.5, color=BLUE),
            Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.2).shift(LEFT*4)
        )
        right_paint = VGroup(
            Line(RIGHT*4 + UP*1.5, RIGHT*4 + DOWN*1.5, color=BLUE),
            Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.2).shift(RIGHT*4)
        )
        court.add(left_paint, right_paint)

        return court
