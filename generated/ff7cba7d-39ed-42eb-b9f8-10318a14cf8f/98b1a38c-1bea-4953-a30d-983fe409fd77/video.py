from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Flow of an NBA Game", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Quarters
        quarters_text = Text("NBA Game Quarters", font_size=36).shift(UP*2)
        self.play(Write(quarters_text))
        self.wait(1)

        # Visual representation of four quarters
        quarter_boxes = VGroup(*[
            Rectangle(width=3, height=1, color=WHITE) for _ in range(4)
        ])
        quarter_texts = VGroup(*[
            Text(f"Q{i+1}", font_size=24) for i in range(4)
        ])
        for i, (box, q_text) in enumerate(zip(quarter_boxes, quarter_texts)):
            box.move_to(UP).shift(DOWN*i)
            q_text.move_to(box.get_center())
        self.play(Create(quarter_boxes), Write(quarter_texts))
        self.wait(2)

        # Game Clock
        clock_text = Text("Game Clock: 12 minutes each", font_size=36).next_to(quarter_boxes, DOWN, buff=0.5)
        clock = self.create_clock().scale(0.5).next_to(clock_text, DOWN, buff=0.5)
        self.play(Write(clock_text))
        self.play(FadeIn(clock))
        self.wait(2)

        # Overtime
        overtime_text = Text("Overtime: Additional period when tied", font_size=36).shift(DOWN*2)
        self.play(Write(overtime_text))
        self.wait(2)

        # Timeouts
        timeouts_text = Text("Timeouts: Rest, Strategize, Stop the Clock", font_size=36).shift(DOWN*3)
        self.play(Write(timeouts_text))
        self.wait(2)

        # Coach Decisions
        coach_role_text = Text("Coaches make crucial game-changing decisions", font_size=28).next_to(timeouts_text, DOWN, buff=0.5)
        coach = self.create_coach().scale(0.5).next_to(coach_role_text, RIGHT, buff=0.5)
        self.play(Write(coach_role_text))
        self.play(FadeIn(coach))
        self.wait(2)

        # Dynamic Flow text
        dynamic_flow_text = Text("Dynamic Flow keeps the game exciting and unpredictable!", font_size=24).next_to(coach_role_text, DOWN, buff=1)
        self.play(Write(dynamic_flow_text))
        self.wait(3)

    def create_clock(self):
        # Create a simple clock representation
        clock = VGroup()
        clock.add(
            Circle(radius=1, color=WHITE),
            Line(start=[0, 0, 0], end=[0, 0.8, 0], color=WHITE),  # Minute hand
            Line(start=[0, 0, 0], end=[0.6, 0, 0], color=WHITE)   # Hour hand
        )
        return clock

    def create_coach(self):
        # Create a simple coach representation
        coach = VGroup()
        coach.add(
            Circle(radius=0.5, color=WHITE),                       # Head
            Line(start=[0, -0.5, 0], end=[0, -1.5, 0], color=WHITE),  # Body
            Line(start=[0, -1, 0], end=[-0.5, -1.5, 0], color=WHITE),  # Left leg
            Line(start=[0, -1, 0], end=[0.5, -1.5, 0], color=WHITE),   # Right leg
            Line(start=[0, -0.75, 0], end=[-0.5, -0.25, 0], color=WHITE),  # Left arm
            Line(start=[0, -0.75, 0], end=[0.5, -0.25, 0], color=WHITE)   # Right arm
        )
        return coach