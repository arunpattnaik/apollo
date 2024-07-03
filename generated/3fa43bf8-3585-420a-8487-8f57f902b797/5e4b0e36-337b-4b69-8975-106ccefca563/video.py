from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("SpaceX's Falcon Rockets", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Falcon 1 introduction
        falcon_1_intro = Text("Falcon 1: SpaceX's First Rocket", font_size=36).next_to(title, DOWN, buff=0.5)
        self.play(Write(falcon_1_intro))
        self.wait(1)

        # Diagram of Falcon 1 and key components
        falcon_1_diagram = self.create_falcon_1_diagram().scale(0.5).next_to(falcon_1_intro, DOWN, buff=0.5)
        self.play(FadeIn(falcon_1_diagram))
        self.wait(2)

        # Key components of Falcon 1
        components = [
            ("First Stage", UP*1.5),
            ("Second Stage", UP*0.5),
            ("Payload Fairing", DOWN*0.5),
        ]

        for component, shift in components:
            text = Text(component, font_size=24).next_to(falcon_1_diagram, shift)
            self.play(Write(text))
            self.wait(1)

        # Success of Falcon 1
        falcon_1_success = Text("In 2008, Falcon 1 successfully reached orbit.", font_size=30).next_to(falcon_1_diagram, DOWN, buff=1)
        self.play(Write(falcon_1_success))
        self.wait(2)

        # Transition to Falcon 9
        falcon_9_intro = Text("Falcon 9: A Reusable Rocket", font_size=36).next_to(falcon_1_success, DOWN, buff=1)
        self.play(Write(falcon_9_intro))
        self.wait(1)

        # Falcon 9 launch animation
        falcon_9 = self.create_falcon_9().scale(0.5).to_edge(LEFT)
        self.play(FadeIn(falcon_9))
        self.wait(1)

        launch_path = Line(falcon_9.get_bottom(), falcon_9.get_bottom() + UP*6, color=WHITE)
        self.play(MoveAlongPath(falcon_9, launch_path, run_time=3))
        self.wait(1)

        # Delivery of payload
        payload = self.create_payload().scale(0.3).next_to(falcon_9, RIGHT, buff=1)
        self.play(FadeIn(payload))
        self.wait(1)

        # Falcon 9 returning to Earth
        return_path = Line(falcon_9.get_top(), falcon_9.get_top() + DOWN*6, color=WHITE)
        self.play(MoveAlongPath(falcon_9, return_path, run_time=3))
        self.wait(1)

        # Reusability statement
        reusability_text = Text("Reusability makes space travel more affordable and sustainable", font_size=30).next_to(falcon_9_intro, DOWN, buff=1)
        self.play(Write(reusability_text))
        self.wait(3)

    def create_falcon_1_diagram(self):
        falcon_1 = VGroup()
        
        # First Stage
        first_stage = Rectangle(width=0.5, height=2.5, color=WHITE, fill_opacity=1).shift(UP*0.75)
        
        # Second Stage
        second_stage = Rectangle(width=0.4, height=1.5, color=WHITE, fill_opacity=1).next_to(first_stage, UP, buff=0.1)
        
        # Payload Fairing
        payload_fairing = Polygon(
            [-0.2, 0, 0], [0.2, 0, 0], [0, 0.5, 0],
            color=WHITE, fill_opacity=1
        ).next_to(second_stage, UP, buff=0)
        
        falcon_1.add(first_stage, second_stage, payload_fairing)
        return falcon_1

    def create_falcon_9(self):
        falcon_9 = VGroup()

        # First Stage
        first_stage = Rectangle(width=0.6, height=4, color=WHITE, fill_opacity=1).shift(UP*2.5)
        
        # Second Stage
        second_stage = Rectangle(width=0.5, height=2, color=WHITE, fill_opacity=1).next_to(first_stage, UP, buff=0.1)
        
        # Payload Fairing
        payload_fairing = Polygon(
            [-0.25, 0, 0], [0.25, 0, 0], [0, 1, 0],
            color=WHITE, fill_opacity=1
        ).next_to(second_stage, UP, buff=0)

        # Grid Fins on First Stage
        grid_fins = [
            Square(side_length=0.3, color=GRAY, fill_opacity=1).move_to(first_stage.get_corner(DOWN+LEFT) + UP*0.5 + RIGHT*0.1),
            Square(side_length=0.3, color=GRAY, fill_opacity=1).move_to(first_stage.get_corner(DOWN+RIGHT) + UP*0.5 + LEFT*0.1),
            Square(side_length=0.3, color=GRAY, fill_opacity=1).move_to(first_stage.get_corner(UP+LEFT) + DOWN*0.5 + RIGHT*0.1),
            Square(side_length=0.3, color=GRAY, fill_opacity=1).move_to(first_stage.get_corner(UP+RIGHT) + DOWN*0.5 + LEFT*0.1),
        ]

        falcon_9.add(first_stage, second_stage, payload_fairing, *grid_fins)
        return falcon_9

    def create_payload(self):
        payload = VGroup()
        main_body = Rectangle(width=0.4, height=0.6, color=BLUE, fill_opacity=1)
        side_panels = [
            Rectangle(width=0.2, height=0.6, color=YELLOW, fill_opacity=1).next_to(main_body, LEFT, buff=0.05),
            Rectangle(width=0.2, height=0.6, color=YELLOW, fill_opacity=1).next_to(main_body, RIGHT, buff=0.05),
        ]
        payload.add(main_body, *side_panels)
        return payload