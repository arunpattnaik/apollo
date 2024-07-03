from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Basketball Scoring Breakdown", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Field goal explanation
        field_goal_text = Text("Field Goal: 2 or 3 points", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(field_goal_text))
        self.wait(1)
        
        two_points_text = Text("2 points if inside 3-point line", font_size=28, color=BLUE).next_to(field_goal_text, DOWN, buff=0.5, aligned_edge=LEFT)
        three_points_text = Text("3 points if outside 3-point line", font_size=28, color=GREEN).next_to(two_points_text, DOWN, aligned_edge=LEFT)
        self.play(Write(two_points_text), Write(three_points_text))
        self.wait(2)

        # Free throw explanation
        free_throw_text = Text("Free Throw: 1 point", font_size=32).next_to(three_points_text, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(free_throw_text))
        self.wait(1)

        # Animating the 3-point shot
        court = self.create_basketball_court().shift(DOWN*2)
        self.play(FadeIn(court))
        self.wait(1)
        
        player = Dot(point=[-2, -1, 0])  # Position the player behind the three-point line
        ball = Circle(radius=0.1, color=ORANGE).next_to(player, UP, buff=0.1)
        hoop = Circle(radius=0.3, color=RED).shift(RIGHT*3 + UP*2)
        
        self.play(FadeIn(player), FadeIn(ball), FadeIn(hoop))
        
        ball_trajectory = ArcBetweenPoints(start=ball.get_center(), end=hoop.get_center(), angle=TAU / 4)
        self.play(MoveAlongPath(ball, ball_trajectory), rate_func=linear)
        self.wait(1)
        
        score_text = Text("3 Points!", font_size=36, color=GREEN).next_to(hoop, UP)
        self.play(Write(score_text))
        self.wait(2)

        # Explanation about teamwork
        teamwork_text = Text("Scoring involves passing, dribbling, and teamwork", font_size=28).next_to(score_text, DOWN, buff=1)
        self.play(Write(teamwork_text))
        self.wait(3)

        # End Scene
        self.play(FadeOut(title), FadeOut(field_goal_text), FadeOut(two_points_text), FadeOut(three_points_text),
                  FadeOut(free_throw_text), FadeOut(court), FadeOut(player), FadeOut(ball), FadeOut(hoop),
                  FadeOut(score_text), FadeOut(teamwork_text))
        self.wait(1)

    def create_basketball_court(self):
        court = VGroup()
        
        half_court_line = Line(LEFT*5 + DOWN*2, RIGHT*5 + DOWN*2, color=WHITE)
        three_point_arc = Arc(radius=3, angle=-PI, start_angle=-PI/2).shift(DOWN*3)
        center_circle = Circle(radius=0.5, color=WHITE).shift(DOWN*2)

        court.add(half_court_line, three_point_arc, center_circle)
        return court