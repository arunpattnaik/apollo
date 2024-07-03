from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("The Future of SpaceX: Making Life Multiplanetary", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Vision of Mars
        mars_vision_text = Text("A Vision of Mars", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(mars_vision_text))
        self.wait(1)
        
        # Mars with habitats and Starships
        mars_scene = self.create_mars_scene().next_to(mars_vision_text, DOWN, buff=0.5)
        self.play(FadeIn(mars_scene))
        self.wait(2)

        # Vision statement
        vision_statement = Text("SpaceX's Goal: A Self-Sustaining Colony on Mars", font_size=28).next_to(mars_scene, DOWN, buff=0.5)
        self.play(Write(vision_statement))
        self.wait(2)

        # Key points about SpaceX mission
        technology_text = Text("Advancements in Technology", font_size=24).next_to(vision_statement, DOWN, buff=0.5)
        engineering_text = Text("Breakthroughs in Engineering", font_size=24).next_to(technology_text, DOWN, buff=0.3)
        cooperation_text = Text("International Cooperation", font_size=24).next_to(engineering_text, DOWN, buff=0.3)
        self.play(Write(technology_text))
        self.wait(0.5)
        self.play(Write(engineering_text))
        self.wait(0.5)
        self.play(Write(cooperation_text))
        self.wait(1.5)

        # Encouraging message
        encouragement_text = Text("Look up at the stars tonight, the journey to other worlds is already underway!", font_size=28).next_to(cooperation_text, DOWN, buff=0.5)
        self.play(Write(encouragement_text))
        self.wait(2)

        # End scene
        thanks_text = Text("Keep dreaming big, and maybe you'll be part of this adventure!", font_size=32).next_to(encouragement_text, DOWN, buff=1)
        self.play(Write(thanks_text))
        self.wait(3)

    def create_mars_scene(self):
        mars_scene = VGroup()

        # Mars planet
        mars = Circle(radius=3, color=RED, fill_opacity=0.5).shift(LEFT*4)
        
        # Habitats
        habitats = VGroup(
            Rectangle(width=1.5, height=1, color=GRAY, fill_opacity=1).shift(LEFT*3.5 + DOWN*1.5),
            Rectangle(width=1.2, height=0.8, color=GRAY, fill_opacity=1).next_to(mars, RIGHT, buff=0.5).shift(UP*1.5),
            Rectangle(width=1, height=0.6, color=GRAY, fill_opacity=1).next_to(mars, RIGHT, buff=1).shift(DOWN*1.5)
        )

        # Starships
        starship_shapes = self.create_starship().next_to(mars, DOWN, buff=3)
        
        mars_scene.add(mars, habitats, starship_shapes)
        return mars_scene

    def create_starship(self):
        starship = VGroup()
        
        # Body
        body = Rectangle(height=1.5, width=0.5, color=WHITE, fill_opacity=1).rotate(PI/2)
        
        # Wings/Fins
        left_fin = Polygon(
            [0, 0, 0], [-0.25, -0.75, 0], [0.25, -0.75, 0], 
            color=WHITE, fill_opacity=1
        ).move_to(body.get_left() + LEFT * 0.25)
        
        right_fin = left_fin.copy().move_to(body.get_right() + RIGHT * 0.25)
        
        # Adding Elements to Starship
        starship.add(body, left_fin, right_fin)
        return starship