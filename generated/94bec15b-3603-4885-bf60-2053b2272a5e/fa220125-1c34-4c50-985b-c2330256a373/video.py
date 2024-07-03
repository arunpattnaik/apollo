from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("The Apollo Program: A Bold Challenge", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # President Kennedy Speech
        kennedy_speech = Text("In 1961, President John F. Kennedy challenged the nation...", font_size=28).next_to(title, DOWN, buff=0.5)
        self.play(Write(kennedy_speech))
        self.wait(2)

        # Showing President Kennedy
        president_kennedy = self.create_president_kennedy().scale(0.8).to_edge(LEFT)
        self.play(FadeIn(president_kennedy))
        self.wait(2)

        # Kennedy's famous speech
        famous_speech = Text('"...to land a man on the Moon and return him safely to Earth before the decade was out."', font_size=20, slant=ITALIC).next_to(president_kennedy, RIGHT, buff=1)
        self.play(Write(famous_speech))
        self.wait(2)

        # Astronaut Alan Shepard
        astronaut_intro = Text("At the time, the U.S. had only just sent its first astronaut, Alan Shepard, into space.", font_size=28).next_to(famous_speech, DOWN, buff=0.5)
        self.play(Write(astronaut_intro))
        self.wait(2)

        astronaut_shepard = self.create_astronaut_shepard().scale(0.7).next_to(astronaut_intro, DOWN, buff=0.5)
        self.play(FadeIn(astronaut_shepard))
        self.wait(2)

        # Engineers and Scientists working
        engineers_intro = Text("This challenge ignited a spark of innovation and determination.", font_size=28).next_to(astronaut_shepard, DOWN, buff=0.75)
        self.play(Write(engineers_intro))
        self.wait(2)

        engineers_image = self.create_engineers().scale(0.6).next_to(engineers_intro, DOWN, buff=0.5)
        self.play(FadeIn(engineers_image))
        self.wait(2)

        # Designing rockets, testing spacecraft
        designing_rockets = Text("Designing rockets, and testing spacecraft,", font_size=28).next_to(engineers_image, DOWN, buff=0.5)
        self.play(Write(designing_rockets))
        self.wait(2)

        apollo_program = Text("the Apollo program was born out of this spirit of exploration and ambition.", font_size=28).next_to(designing_rockets, DOWN, buff=0.5)
        self.play(Write(apollo_program))
        self.wait(2)

    def create_president_kennedy(self):
        # Simplified representation of President John F. Kennedy
        kennedy = VGroup()
        head = Circle(radius=0.5, color=WHITE).shift(UP*1.5)
        body = Rectangle(width=0.8, height=1.5, color=WHITE).next_to(head, DOWN, buff=0)
        podium = Rectangle(width=1.2, height=1, color=GRAY).next_to(body, DOWN, buff=0)

        kennedy.add(head, body, podium)
        return kennedy

    def create_astronaut_shepard(self):
        # Simplified representation of Alan Shepard
        astronaut = VGroup()
        helmet = Circle(radius=0.5, color=WHITE).shift(UP*1.5)
        suit = Rectangle(width=0.7, height=1.5, color=WHITE).next_to(helmet, DOWN, buff=0)
        arm_left = Line(start=[-0.35, 0, 0], end=[-0.7, -0.5, 0], color=WHITE)
        arm_right = Line(start=[0.35, 0, 0], end=[0.7, -0.5, 0], color=WHITE)
        leg_left = Line(start=[-0.2, -1.5, 0], end=[-0.2, -2, 0], color=WHITE)
        leg_right = Line(start=[0.2, -1.5, 0], end=[0.2, -2, 0], color=WHITE)

        astronaut.add(helmet, suit, arm_left, arm_right, leg_left, leg_right)
        return astronaut

    def create_engineers(self):
        # Simplified representation of engineers and scientists working
        engineers = VGroup()
        engineer1 = Rectangle(width=0.5, height=1.5, color=BLUE).shift(LEFT*1.5)
        engineer2 = Rectangle(width=0.5, height=1.5, color=RED).shift(ORIGIN)
        engineer3 = Rectangle(width=0.5, height=1.5, color=GREEN).shift(RIGHT*1.5)

        engineers.add(engineer1, engineer2, engineer3)
        return engineers