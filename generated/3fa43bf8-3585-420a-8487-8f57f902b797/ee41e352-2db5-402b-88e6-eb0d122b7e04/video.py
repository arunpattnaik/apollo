from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Achievements of the Dragon Spacecraft", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text("The Dragon is a family of spacecraft developed by SpaceX", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Dragon docking animation
        dragon_text = Text("Animation: Dragon docking with ISS", font_size=28).next_to(intro_text, DOWN, buff=1)
        self.play(Write(dragon_text))
        self.wait(2)

        # Create and animate Dragon docking with ISS
        iss = self.create_iss().scale(0.5).to_edge(LEFT).shift(DOWN*0.5)
        dragon = self.create_dragon().scale(0.3).to_edge(RIGHT).shift(UP*1.5)
        
        self.play(FadeIn(iss), FadeIn(dragon))
        self.wait(1)
        docking_trajectory = dragon.animate.shift(LEFT*5 + DOWN*1.5)
        self.play(docking_trajectory, run_time=5)
        self.wait(2)

        # Achievements of Dragon 1
        dragon1_text = Text("Dragon 1: First commercial spacecraft to deliver cargo to the ISS", font_size=28).next_to(dragon_text, DOWN, buff=2)
        self.play(Write(dragon1_text))
        self.wait(2)

        # Achievements of Dragon 2
        dragon2_text = Text("Dragon 2: Designed to carry astronauts", font_size=28).next_to(dragon1_text, DOWN, buff=1)
        self.play(Write(dragon2_text))
        self.wait(2)

        # Crew Dragon historical launch
        crew_dragon_text = Text("In 2020, Crew Dragon launched NASA astronauts to the ISS", font_size=28).next_to(dragon2_text, DOWN, buff=1)
        crew_dragon_subtext = Text("from American soil for the first time since the Space Shuttle program ended", font_size=24).next_to(crew_dragon_text, DOWN, buff=0.5)
        self.play(Write(crew_dragon_text))
        self.wait(1)
        self.play(Write(crew_dragon_subtext))
        self.wait(2)

        # Summary
        summary_text = Text("Commercial spaceflight and SpaceX's capability to safely transport humans to space", font_size=28).next_to(crew_dragon_subtext, DOWN, buff=1)
        self.play(Write(summary_text))
        self.wait(3)

    def create_iss(self):
        iss = VGroup()

        # Main body of ISS
        main_body = Rectangle(width=2, height=0.5, color=WHITE, fill_opacity=1)
        solar_panels = VGroup(
            Rectangle(width=0.2, height=1, color=BLUE, fill_opacity=1).next_to(main_body, LEFT, buff=0.1),
            Rectangle(width=0.2, height=1, color=BLUE, fill_opacity=1).next_to(main_body, RIGHT, buff=0.1)
        )
        
        iss.add(main_body, solar_panels)
        return iss

    def create_dragon(self):
        dragon = VGroup()

        # Main body of Dragon
        capsule_body = Polygon(
            [-0.5, 0, 0], [-0.25, 0.75, 0], [0.25, 0.75, 0], [0.5, 0, 0],
            color=WHITE, fill_opacity=1
        )
        trunk = Rectangle(width=0.5, height=1.25, color=GRAY, fill_opacity=1).next_to(capsule_body, DOWN, buff=0)
        
        dragon.add(capsule_body, trunk)
        return dragon
