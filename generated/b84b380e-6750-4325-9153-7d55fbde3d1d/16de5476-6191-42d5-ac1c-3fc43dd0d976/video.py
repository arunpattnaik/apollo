from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Collaboration with Vercel", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Collaboration description
        collaboration_text = Text("Vercel makes it easy to work with your team.", font_size=32)
        self.play(Write(collaboration_text))
        self.wait(2)

        # Developers working together
        developers_box = self.create_developers_box().shift(DOWN*1)
        self.play(FadeIn(developers_box))
        self.wait(2)

        # Version control integration
        version_control = Text(
            "Integrates with GitHub, GitLab, and Bitbucket",
            font_size=32
        ).next_to(developers_box, DOWN, buff=1)
        self.play(Write(version_control))
        self.wait(1)

        # Automatic deployment
        deployment_text = Text("Automatic deployment with each change", font_size=32).next_to(version_control, DOWN, buff=0.5)
        self.play(Write(deployment_text))
        self.wait(2)

        # End Scene
        end_text = Text("Keeps everyone on the same page, ensuring smooth operations.", font_size=32).next_to(deployment_text, DOWN, buff=0.5)
        self.play(Write(end_text))
        self.wait(3)

    def create_developers_box(self):
        box = VGroup()
        box_rect = Rectangle(width=10, height=4, color=WHITE)

        # Developer 1 with preview URL
        dev1 = Text("Developer 1", font_size=24).shift(LEFT*3 + UP*1)
        preview1 = Text("Preview URL 1", font_size=20, color=BLUE).next_to(dev1, DOWN, buff=0.2)

        # Developer 2 with preview URL
        dev2 = Text("Developer 2", font_size=24).shift(UP*1)
        preview2 = Text("Preview URL 2", font_size=20, color=BLUE).next_to(dev2, DOWN, buff=0.2)

        # Developer 3 with preview URL
        dev3 = Text("Developer 3", font_size=24).shift(RIGHT*3 + UP*1)
        preview3 = Text("Preview URL 3", font_size=20, color=BLUE).next_to(dev3, DOWN, buff=0.2)
        
        box.add(box_rect, dev1, preview1, dev2, preview2, dev3, preview3)
        return box