from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Welcome to the World of NBA Basketball!", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text("Dive into what makes this sport so thrilling", font_size=30).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # Basics text
        basics_text = Text("Let's start with the basics.", font_size=32).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(basics_text))
        self.wait(1)

        # Show basketball court
        court = self.create_basketball_court().scale(0.7).shift(DOWN*1)
        self.play(FadeIn(court))
        self.wait(2)

        # Objective of the game text
        objective_text1 = Text("The objective is simple:", font_size=30).next_to(court, UP, buff=0.5)
        objective_text2 = Text("Score more points by shooting through the opponent's hoop", font_size=24).next_to(objective_text1, DOWN, buff=0.5)
        self.play(Write(objective_text1))
        self.play(Write(objective_text2))
        self.wait(2)

        # Teams and players text
        teams_text = Text("Each team has five players on the court", font_size=28).next_to(court, DOWN, buff=0.5)
        self.play(Write(teams_text))
        self.wait(1)

        # Players moving the ball and creating scoring opportunities
        players_text = Text("They work together to move the ball and create scoring opportunities", font_size=24).next_to(teams_text, DOWN, buff=0.5)
        self.play(Write(players_text))
        self.wait(2)

        # Transition to breakdown of key elements
        breakdown_text = Text("Now, let's break down some key elements of the game.", font_size=30).to_edge(DOWN)
        self.play(Write(breakdown_text))
        self.wait(2)

    def create_basketball_court(self):
        court = VGroup()

        # Court outline
        outline = Rectangle(width=10, height=5, color=WHITE)
        center_circle = Circle(radius=0.75, color=WHITE).move_to(outline.get_center())
        
        # Hoops
        hoop_left = Circle(radius=0.2, color=ORANGE).move_to(outline.get_left() + RIGHT * 0.5)
        hoop_right = Circle(radius=0.2, color=ORANGE).move_to(outline.get_right() + LEFT * 0.5)
        
        # Key areas
        key_left = Rectangle(width=1.5, height=3, color=WHITE).move_to(outline.get_left() + RIGHT * 1.75)
        key_right = Rectangle(width=1.5, height=3, color=WHITE).move_to(outline.get_right() + LEFT * 1.75)
        
        # Adding elements to court
        court.add(outline, center_circle, hoop_left, hoop_right, key_left, key_right)
        return court