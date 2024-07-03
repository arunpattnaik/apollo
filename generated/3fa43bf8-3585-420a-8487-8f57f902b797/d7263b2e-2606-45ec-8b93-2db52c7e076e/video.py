from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Exploring the World of SpaceX", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text = Text("SpaceX: Making Space Exploration a Reality", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # Drawing SpaceX text logo
        spacex_logo = self.create_spacex_text_logo().scale(1.5).to_edge(LEFT, buff=1)
        self.play(FadeIn(spacex_logo))
        self.wait(1)

        # Major Milestones Timeline
        timeline_title = Text("Major Milestones", font_size=36).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(timeline_title))
        self.wait(1)

        milestones = [
            ("2002", "SpaceX founded"),
            ("2008", "First privately funded spacecraft to reach orbit"),
            ("2010", "First privately developed spacecraft to return from orbit"),
            ("2012", "First privately funded spacecraft to dock with the ISS"),
            ("2020", "First crewed mission to the ISS"),
        ]

        timeline = VGroup()
        for i, (year, event) in enumerate(milestones):
            year_text = Text(year, font_size=24, color=YELLOW)
            event_text = Text(event, font_size=20)
            milestone = VGroup(year_text, event_text).arrange(DOWN, aligned_edge=LEFT)
            milestone.shift(DOWN * i * 1.5 + DOWN * 0.5).to_edge(RIGHT, buff=1)
            timeline.add(milestone)

        self.play(LaggedStartMap(FadeIn, timeline, lag_ratio=0.5))
        self.wait(2)

        # Transition to deeper explanation
        journey_text = Text("How did SpaceX achieve these feats?", font_size=32).next_to(timeline_title, DOWN, buff=1.5)
        self.play(Write(journey_text))
        self.wait(2)

        # End Scene
        self.play(FadeOut(title), FadeOut(intro_text), FadeOut(spacex_logo), FadeOut(timeline_title), 
                  FadeOut(timeline), FadeOut(journey_text))
        self.wait(1)

    def create_spacex_text_logo(self):
        logo_text = Text("SpaceX", font_size=64, color=BLUE)
        return logo_text