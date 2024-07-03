from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("The Legacy of Apollo Missions", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Timeline header
        timeline_header = Text("Apollo Missions Timeline", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(timeline_header))
        self.wait(1)

        # Create timeline
        timeline = self.create_timeline().next_to(timeline_header, DOWN, buff=0.5)
        self.play(Write(timeline))
        self.wait(2)

        # Highlighting different missions
        apollo_12 = self.create_mission("Apollo 12", "November 1969")
        apollo_12.next_to(timeline, DOWN, buff=0.5).to_edge(LEFT)
        self.play(FadeIn(apollo_12))
        self.wait(1)

        apollo_15 = self.create_mission("Apollo 15", "July 1971")
        apollo_15.next_to(apollo_12, RIGHT, buff=1)
        self.play(FadeIn(apollo_15))
        self.wait(1)

        apollo_17 = self.create_mission("Apollo 17", "December 1972")
        apollo_17.next_to(apollo_15, RIGHT, buff=1)
        self.play(FadeIn(apollo_17))
        self.wait(2)

        # Outro
        outro_text = Text(
            "The legacy of the Apollo program lives on. It paved the way for future space exploration "
            "and inspired generations to dream big. Thank you for joining me on this journey. "
            "Keep reaching for the stars!",
            font_size=24,
        ).next_to(apollo_17, DOWN, buff=1).shift(LEFT*2)
        self.play(Write(outro_text))
        self.wait(3)

    def create_timeline(self):
        line = Line(LEFT * 6, RIGHT * 6, color=WHITE)
        # Markers for each Apollo mission from 12 to 17
        for i, mission in enumerate(range(12, 18)):
            dot = Dot().move_to(LEFT * 5 + RIGHT * i * 2)
            label = Text(f"Apollo {mission}", font_size=18).next_to(dot, DOWN)
            self.add(dot, label)
        return line

    def create_mission(self, mission_name, date_text):
        mission = VGroup()
        name = Text(mission_name, font_size=24, weight=BOLD).to_edge(UP)
        date = Text(date_text, font_size=20).next_to(name, DOWN)
        mission.add(name, date)
        return mission