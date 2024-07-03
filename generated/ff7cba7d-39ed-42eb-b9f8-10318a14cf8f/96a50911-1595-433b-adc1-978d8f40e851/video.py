from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Key Basketball Rules and Terms", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Dribbling
        dribbling_text = Text("Dribbling", font_size=36).shift(UP*2.5)
        dribbling_desc = Text("Players move the ball around the court by bouncing it.", font_size=24).next_to(dribbling_text, DOWN)
        self.play(Write(dribbling_text), Write(dribbling_desc))
        self.wait(2)
        
        ball = Circle(radius=0.5, color=ORANGE).shift(LEFT*3)
        hand = VGroup(Line([0, 0.5, 0], [0, -0.5, 0], color=WHITE), Circle(radius=0.1, color=WHITE)).next_to(ball, UP, buff=0.1)
        self.play(FadeIn(ball, hand))
        self.wait(1)

        self.play(StartDribbling(ball, hand, bounce_height=1), run_time=2.5)
        self.wait(1)
        self.play(FadeOut(ball, hand))

        # Passing
        passing_text = Text("Passing", font_size=36).shift(DOWN*0.5)
        passing_desc = Text("Throwing the ball to a teammate.", font_size=24).next_to(passing_text, DOWN)
        self.play(Write(passing_text), Write(passing_desc))
        self.wait(2)
        
        ball = Circle(radius=0.5, color=ORANGE).shift(LEFT*3)
        self.play(FadeIn(ball))
        self.wait(1)
        
        trajectory = Line(ball.get_center(), ball.get_center() + RIGHT*6, color=WHITE, stroke_width=4)
        self.play(ShowPassing(ball, trajectory), run_time=2.5)
        self.wait(1)
        self.play(FadeOut(ball))

        # Shooting
        shooting_text = Text("Shooting", font_size=36).shift(DOWN*4)
        shooting_desc = Text("Scoring points by getting the ball through the hoop.", font_size=24).next_to(shooting_text, DOWN)
        self.play(Write(shooting_text), Write(shooting_desc))
        self.wait(2)
        
        hoop = Circle(radius=0.75, color=RED).shift(RIGHT*3 + UP*2)
        ball = Circle(radius=0.5, color=ORANGE).shift(LEFT*3 + DOWN*2)
        self.play(FadeIn(hoop, ball))
        self.wait(1)
        
        trajectory = ArcBetweenPoints(ball.get_center(), hoop.get_center(), angle=-PI/3, color=WHITE, stroke_width=4)
        self.play(ShowShooting(ball, trajectory), run_time=2.5)
        self.wait(1)
        self.play(FadeOut(ball, hoop))

        # Fouls
        fouls_text = Text("Fouls", font_size=36).shift(UP*2)
        fouls_desc = Text("Violations of the rules", font_size=24).shift(DOWN).next_to(fouls_text, DOWN)
        personal_foul_desc = Text("Illegal physical contact with an opponent.", font_size=24).shift(DOWN*1).next_to(fouls_desc, DOWN)
        self.play(Write(fouls_text), Write(fouls_desc), Write(personal_foul_desc))
        self.wait(2)

        # End Scene
        basics_text = Text("Understanding these basics will help you follow the action more closely.", font_size=28).shift(DOWN*3)
        self.play(Write(basics_text))
        self.wait(3)

# Custom animation for dribbling ball
def StartDribbling(ball, hand, bounce_height):
    return Succession(
        ApplyMethod(ball.shift, DOWN*bounce_height/2, rate_func=there_and_back),
        ApplyMethod(ball.shift, UP*bounce_height/2, rate_func=there_and_back),
        ApplyMethod(hand.shift, DOWN*bounce_height/2, rate_func=there_and_back),
        ApplyMethod(hand.shift, UP*bounce_height/2, rate_func=there_and_back)
    )

# Custom animation for passing the ball
def ShowPassing(ball, trajectory):
    return Succession(
        MoveAlongPath(ball, trajectory),
        FadeOut(ball)
    )

# Custom animation for shooting the ball
def ShowShooting(ball, trajectory):
    return Succession(
        MoveAlongPath(ball, trajectory),
        FadeOut(ball)
    )