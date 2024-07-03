from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Apollo 11: First Moon Landing", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Lunar Module Landing
        lunar_module_text = Text("Lunar Module 'Eagle' Landing", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(lunar_module_text))
        self.wait(1)

        lunar_module_image = self.create_lunar_module().scale(0.5).next_to(lunar_module_text, DOWN, buff=0.5)
        self.play(FadeIn(lunar_module_image))
        self.wait(2)

        # Astronaut Names
        astronauts_text = Text("Neil Armstrong and Buzz Aldrin", font_size=32).next_to(lunar_module_image, DOWN, buff=0.5)
        self.play(Write(astronauts_text))
        self.wait(1)

        # Armstrong's Famous Quote
        quote_text = Text("'One small step for man,\n one giant leap for mankind.'", font_size=28, color=BLUE).next_to(astronauts_text, DOWN, buff=0.5)
        self.play(Write(quote_text))
        self.wait(2)

        # Astronauts on the Moon
        moon_scene_text = Text("Astronauts conducting experiments,\ncollecting samples, and planting the American flag", font_size=28).next_to(quote_text, DOWN, buff=0.5)
        self.play(Write(moon_scene_text))
        self.wait(1)

        moon_scene_image = self.create_moon_scene().scale(0.6).next_to(moon_scene_text, DOWN, buff=0.5)
        self.play(FadeIn(moon_scene_image))
        self.wait(2)

        # Human Ingenuity and Perseverance
        ingenuity_text = Text("A testament to human ingenuity and perseverance", font_size=30, color=YELLOW).next_to(moon_scene_image, DOWN, buff=0.5)
        self.play(Write(ingenuity_text))
        self.wait(3)

    def create_lunar_module(self):
        lunar_module = VGroup()
        
        # Create the body of the Lunar Module
        body = Polygon([0, 1, 0], [-0.5, -1, 0], [0.5, -1, 0], color=GRAY, fill_opacity=1)
        legs = VGroup(
            Line([0.5, -1, 0], [1, -2, 0], color=GRAY),
            Line([-0.5, -1, 0], [-1, -2, 0], color=GRAY),
            Line([0.5, -1, 0], [0.5, -1.5, 0], color=GRAY),
            Line([-0.5, -1, 0], [-0.5, -1.5, 0], color=GRAY),
            Line([0.75, -2, 0], [1.5, -2.5, 0], color=GRAY),
            Line([-0.75, -2, 0], [-1.5, -2.5, 0], color=GRAY)
          )
        ladder = Line([0, -1, 0], [0, -2, 0], color=WHITE)

        lunar_module.add(body, legs, ladder)
        return lunar_module

    def create_moon_scene(self):
        moon_scene = VGroup()

        # Astronauts
        astronaut1 = self.create_astronaut().shift(LEFT*2)
        astronaut2 = self.create_astronaut().shift(RIGHT*2)
        
        # American Flag
        flag_pole = Line([0, -1, 0], [0, 1, 0], color=WHITE)
        flag = Polygon([0, 0.5, 0], [1, 0.5, 0], [1, 0, 0], [0, 0, 0], color=RED, fill_opacity=1)
        flag_group = VGroup(flag_pole, flag).shift(UP)

        # Experiment Tools
        tool1 = Rectangle(width=0.3, height=0.3, color=BLUE).shift(LEFT*1 + DOWN*0.5)
        tool2 = Rectangle(width=0.3, height=0.3, color=GREEN).shift(RIGHT*1 + DOWN*0.5)

        moon_scene.add(astronaut1, astronaut2, flag_group, tool1, tool2)
        return moon_scene

    def create_astronaut(self):
        astronaut = VGroup()

        head = Circle(radius=0.2, color=WHITE, fill_opacity=1).shift(UP*0.5)
        body = Rectangle(width=0.3, height=0.6, color=WHITE, fill_opacity=1).shift(DOWN*0.25)
        left_arm = Line([-0.3, 0.3, 0], [-0.5, -0.2, 0], color=WHITE)
        right_arm = Line([0.3, 0.3, 0], [0.5, -0.2, 0], color=WHITE)
        left_leg = Line([-0.1, -0.3, 0], [-0.3, -0.8, 0], color=WHITE)
        right_leg = Line([0.1, -0.3, 0], [0.3, -0.8, 0], color=WHITE)

        astronaut.add(head, body, left_arm, right_arm, left_leg, right_leg)
        return astronaut