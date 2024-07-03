from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Comparing GPT and Claude", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction Text
        intro_text = Text(
            "Two powerful AI models: OpenAI's GPT & Anthropic's Claude", font_size=36
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # Comparison Visualization
        comparison_text = Text(
            "Imagine these models as two brilliant students in a classroom,", font_size=30
        ).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(comparison_text))
        self.wait(1)

        comparison_detail = Text(
            "each with their own unique strengths and ways of thinking.", font_size=30
        ).next_to(comparison_text, DOWN, buff=0.5)
        self.play(Write(comparison_detail))
        self.wait(1)

        # Background Timeline
        timeline_title = Text("Timeline of Development", font_size=36).next_to(comparison_detail, DOWN, buff=1)
        self.play(Write(timeline_title))
        self.wait(1)

        timeline = self.create_timeline().next_to(timeline_title, DOWN, buff=0.5)
        self.play(FadeIn(timeline))
        self.wait(2)

        # Key Milestones
        gpt_milestones = [
            ("GPT-1", "June 2018"),
            ("GPT-2", "February 2019"),
            ("GPT-3", "June 2020"),
        ]

        claude_milestones = [
            ("Claude v1", "April 2021"),
            ("Claude v2", "September 2022"),
        ]

        gpt_entries = self.create_milestones(gpt_milestones, LEFT, timeline)
        claude_entries = self.create_milestones(claude_milestones, RIGHT, timeline)

        for entry in gpt_entries + claude_entries:
            self.play(Write(entry))
            self.wait(1)

        # End Scene
        conclusion_text = Text("Exploring the unique strengths of GPT and Claude.", font_size=36).to_edge(DOWN)
        self.play(Write(conclusion_text))
        self.wait(2)

    def create_timeline(self):
        line = Line(LEFT * 5, RIGHT * 5, color=WHITE)
        start = Dot(LEFT * 5, color=YELLOW)
        end = Dot(RIGHT * 5, color=YELLOW)
        return VGroup(line, start, end)

    def create_milestones(self, milestones, direction, timeline):
        entries = []
        for milestone, date in milestones:
            point = Dot(color=YELLOW)
            point.next_to(timeline[0].point_from_proportion(0.5), direction, buff=2)
            name = Text(f"{milestone}\n({date})", font_size=24)
            name.next_to(point, direction, buff=0.5)
            entries.append(VGroup(point, name))
        return entries