from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("SpaceX's Starship", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text(
            "Starship is designed to be a fully reusable\nspacecraft capable of carrying humans to Mars and beyond.",
            font_size=28
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Rendering of Starship
        starship = self.create_starship().scale(0.6).shift(DOWN*0.5)
        self.play(FadeIn(starship))
        self.wait(1)

        # Two stages text
        stages_text = Text(
            "Starship consists of two stages:",
            font_size=32
        ).next_to(starship, DOWN, buff=0.5)
        self.play(Write(stages_text))
        self.wait(1)

        # Super Heavy booster and Starship spacecraft text
        super_heavy_text = Text("1. Super Heavy Booster", font_size=28, color=RED).next_to(stages_text, DOWN, buff=0.5, aligned_edge=LEFT)
        starship_spacecraft_text = Text("2. Starship Spacecraft", font_size=28, color=BLUE).next_to(super_heavy_text, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(super_heavy_text), Write(starship_spacecraft_text))
        self.wait(2)

        # Super Heavy booster description
        booster_description = Text(
            "The Super Heavy booster provides the initial thrust\nneeded to escape Earth's gravity.",
            font_size=24
        ).next_to(super_heavy_text, DOWN, buff=1, aligned_edge=LEFT)
        self.play(Write(booster_description))
        self.wait(2)

        # Starship spacecraft description
        spacecraft_description = Text(
            "The Starship spacecraft is designed for long-duration space travel.",
            font_size=24
        ).next_to(starship_spacecraft_text, DOWN, buff=1, aligned_edge=LEFT)
        self.play(Write(spacecraft_description))
        self.wait(2)

        # Future vision text
        vision_text = Text(
            "Imagine a future where humans can travel to other planets\nand even establish colonies. That's the vision behind Starship.",
            font_size=28
        ).to_edge(DOWN)
        self.play(Write(vision_text))
        self.wait(2)

        # End Scene
        self.play(FadeOut(title), FadeOut(intro_text), FadeOut(starship), FadeOut(stages_text), 
                  FadeOut(super_heavy_text), FadeOut(starship_spacecraft_text), FadeOut(booster_description), 
                  FadeOut(spacecraft_description), FadeOut(vision_text))
        self.wait(1)

    def create_starship(self):
        starship = VGroup()
        
        # Body of the spacecraft
        body = RoundedRectangle(corner_radius=0.5, height=5.5, width=1.5, color=GRAY, fill_opacity=1)
        
        # Nose cone
        nose_cone = Polygon(
            [-0.75, 2.75, 0], [0.75, 2.75, 0], [0, 4.5, 0],
            color=GRAY, fill_opacity=1
        )
        
        # Fins
        left_fin = Polygon(
            [-0.75, -2.0, 0], [-1.5, -3, 0], [-0.75, -3, 0],
            color=GRAY, fill_opacity=1
        )
        right_fin = Polygon(
            [0.75, -2.0, 0], [1.5, -3, 0], [0.75, -3, 0],
            color=GRAY, fill_opacity=1
        )
        
        # Super Heavy booster
        booster = RoundedRectangle(corner_radius=0.5, height=7, width=1.75, color=LIGHT_GRAY, fill_opacity=1).shift(DOWN*4.5)
        
        starship.add(booster, body, nose_cone, left_fin, right_fin)
        return starship