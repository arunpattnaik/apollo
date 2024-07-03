from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Elon Musk and Twitter: A Fascinating Topic", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text = Text("Today, we're diving into a fascinating topic: Elon Musk and Twitter.", font_size=28).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Elon Musk introduction
        elon_intro_text = Text("Elon Musk, the visionary behind companies like Tesla and SpaceX, has a unique relationship with Twitter.", font_size=24).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(elon_intro_text))
        self.wait(2)

        # Elon Musk details
        elon_details_text = Text("Let's start by understanding who Elon Musk is and why his tweets matter.", font_size=24).next_to(elon_intro_text, DOWN, buff=0.5)
        self.play(Write(elon_details_text))
        self.wait(2)

        # Images of Tesla, SpaceX, Elon Musk
        tesla_image = self.create_tesla_car().scale(0.5).to_edge(LEFT)
        spacex_image = self.create_spacex_rocket().scale(0.5).next_to(tesla_image, RIGHT, buff=1)
        elon_image = self.create_elon_musk().scale(0.5).to_edge(RIGHT)

        self.play(FadeIn(tesla_image), FadeIn(spacex_image), FadeIn(elon_image))
        self.wait(2)

        # Elon Musk's presence on Twitter
        twitter_text = Text("Elon Musk is known for his innovative ideas and ambitious projects, but he's also known for his active presence on Twitter.", font_size=22).next_to(elon_details_text, DOWN, buff=0.5)
        self.play(Write(twitter_text))
        self.wait(3)

        # Why does this matter?
        why_matter_text = Text("So, why does this matter? Let's find out!", font_size=26).next_to(twitter_text, DOWN, buff=0.5)
        self.play(Write(why_matter_text))
        self.wait(3)

    def create_tesla_car(self):
        car = VGroup()
        car.add(
            Rectangle(width=3, height=1, color=BLUE, fill_opacity=1),
            Circle(radius=0.2, color=BLACK, fill_opacity=1).shift(LEFT*1.2 + DOWN*0.7),
            Circle(radius=0.2, color=BLACK, fill_opacity=1).shift(RIGHT*1.2 + DOWN*0.7)
        )
        return car

    def create_spacex_rocket(self):
        rocket = VGroup()
        rocket_body = Polygon(
            [0, 0, 0], [0.5, 2, 0], [0.3, 2.5, 0], [-0.3, 2.5, 0], [-0.5, 2, 0],
            color=WHITE, fill_opacity=1
        )
        rocket_fins = VGroup(
            Polygon(
                [-0.5, 0, 0], [-1, -1, 0], [0.5, 0, 0],
                color=RED, fill_opacity=1
            ),
            Polygon(
                [0.5, 0, 0], [1, -1, 0], [-0.5, 0, 0],
                color=RED, fill_opacity=1
            )
        )
        rocket.add(rocket_body, rocket_fins)
        return rocket

    def create_elon_musk(self):
        elon = VGroup()
        face = Circle(radius=0.5, color=WHITE, fill_opacity=1)
        eyes = VGroup(
            Circle(radius=0.06, color=BLACK, fill_opacity=1).shift(LEFT*0.2 + UP*0.1),
            Circle(radius=0.06, color=BLACK, fill_opacity=1).shift(RIGHT*0.2 + UP*0.1)
        )
        mouth = Polygon(
            [-0.2, -0.1, 0], [0.2, -0.1, 0], [0, -0.2, 0],
            color=BLACK, fill_opacity=1
        )
        elon.add(face, eyes, mouth)
        return elon