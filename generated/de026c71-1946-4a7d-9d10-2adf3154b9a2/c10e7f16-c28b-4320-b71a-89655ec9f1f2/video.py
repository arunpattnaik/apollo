from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Introducing Next.js", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Feature Points
        features = [
            "Server-Side Rendering",
            "Static Site Generation",
            "File-Based Routing",
            "API Routes"
        ]

        feature_texts = VGroup(
            *[Text(feature, font_size=36, color=BLUE).shift(DOWN * i * 0.6) for i, feature in enumerate(features)]
        ).next_to(title, DOWN, buff=1)

        features_title = Text("Next.js Features:", font_size=40, color=YELLOW).next_to(title, DOWN, buff=0.5)
        self.play(Write(features_title))

        for feature_text in feature_texts:
            self.play(Write(feature_text))
            self.wait(0.5)

        # Swiss Army Knife Metaphor
        metaphor_text = Text("Next.js: The Swiss Army Knife for Web Development", font_size=32, color=GREEN).next_to(feature_texts, DOWN, buff=1)
        self.play(Write(metaphor_text))
        self.wait(2)

        swiss_army_knife = self.create_swiss_army_knife().scale(0.8).next_to(metaphor_text, DOWN, buff=0.5)
        self.play(FadeIn(swiss_army_knife))
        self.wait(2)

        # End with Thank You message
        thanks_text = Text("Thanks for watching, and happy coding!", font_size=36).next_to(swiss_army_knife, DOWN, buff=1)
        self.play(Write(thanks_text))
        self.wait(3)

    def create_swiss_army_knife(self):
        knife = VGroup()
        
        # Knife handle
        handle = Rectangle(width=4, height=1, fill_color=RED, fill_opacity=1, stroke_color=WHITE)
        
        # Blade
        blade = Polygon(
            [0, 0, 0], [2, 0.5, 0], [2, -0.5, 0], [0, -1, 0],
            color=GRAY, fill_opacity=1, stroke_color=WHITE
        ).next_to(handle, LEFT, buff=0)
        
        knife.add(handle, blade)
        return knife