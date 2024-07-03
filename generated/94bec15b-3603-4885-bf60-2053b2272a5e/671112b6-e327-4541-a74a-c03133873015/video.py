from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("The Apollo Space Missions", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text1 = Text(
            "Welcome, space enthusiasts!", font_size=36
        ).next_to(title, DOWN, buff=0.5)
        intro_text2 = Text(
            "Today, we're diving into one of the most thrilling chapters in human history:",
            font_size=36,
        ).next_to(intro_text1, DOWN)
        intro_text3 = Text(
            "the Apollo Space Missions.", font_size=36
        ).next_to(intro_text2, DOWN)

        self.play(Write(intro_text1))
        self.play(Write(intro_text2))
        self.play(Write(intro_text3))
        self.wait(2)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
        # Earth and Moon
        earth = Circle(radius=1, color=BLUE, fill_opacity=1).shift(LEFT*3)
        moon = Circle(radius=0.5, color=WHITE, fill_opacity=1).shift(RIGHT*3)
        earth_label = Text("Earth", font_size=24).next_to(earth, DOWN)
        moon_label = Text("Moon", font_size=24).next_to(moon, DOWN)

        # Dotted Line (Journey)
        journey_line = DashedLine(earth.get_right(), moon.get_left(), color=YELLOW)

        self.play(
            FadeIn(earth),
            FadeIn(moon),
            Write(earth_label),
            Write(moon_label),
            Create(journey_line),
        )
        self.wait(2)

        # Apollo Missions Briefing
        apollo_text = Text(
            "Apollo Missions: \nTurning the dream of landing on the Moon into reality.",
            font_size=28,
        ).next_to(journey_line, DOWN*1.5).set_color(YELLOW)

        self.play(Write(apollo_text))
        self.wait(2)

        # Question - How did it all begin?
        begin_text = Text(
            "But how did it all begin? Let's find out!", font_size=32
        ).next_to(apollo_text, DOWN*1.5)

        self.play(Write(begin_text))
        self.wait(2)

        # End Scene
        self.play(
            *[
                FadeOut(mob)
                for mob in self.mobjects
            ]
        )
        self.wait(1)