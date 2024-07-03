from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Welcome to Vercel", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text("Imagine you have a brilliant idea for a website or web application, and you want to share it with the world. But how do you get it from your computer to the internet?", font_size=32).scale(0.5).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(3)

        # Diagram explanation
        diagram_explanation = Text("That's where Vercel comes in.", font_size=36).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(diagram_explanation))
        self.wait(2)

        # Diagram elements
        developer_computer = self.create_developer_computer().scale(1.2).shift(LEFT*3)
        internet = self.create_internet().scale(1.2).shift(RIGHT*3)
        vercel_logo = self.create_vercel_logo().scale(0.8).move_to(ORIGIN)

        developer_text = Text("Developer's Computer", font_size=24).next_to(developer_computer, DOWN)
        internet_text = Text("The Internet", font_size=24).next_to(internet, DOWN)
        vercel_text = Text("Vercel", font_size=24).next_to(vercel_logo, DOWN)

        self.play(FadeIn(developer_computer), Write(developer_text))
        self.play(FadeIn(internet), Write(internet_text))
        self.play(FadeIn(vercel_logo), Write(vercel_text))
        self.wait(2)

        # Bridge visualization
        arrow_from_dev_to_vercel = Arrow(start=developer_computer.get_right(), end=vercel_logo.get_left(), buff=0.1, color=BLUE)
        arrow_from_vercel_to_internet = Arrow(start=vercel_logo.get_right(), end=internet.get_left(), buff=0.1, color=GREEN)

        self.play(GrowArrow(arrow_from_dev_to_vercel))
        self.play(GrowArrow(arrow_from_vercel_to_internet))
        self.wait(3)

        # Ending scene
        self.play(FadeOut(title), FadeOut(intro_text), FadeOut(diagram_explanation), 
                  FadeOut(developer_computer), FadeOut(developer_text), FadeOut(internet), 
                  FadeOut(internet_text), FadeOut(vercel_logo), FadeOut(vercel_text), 
                  FadeOut(arrow_from_dev_to_vercel), FadeOut(arrow_from_vercel_to_internet))
        self.wait(1)

    def create_developer_computer(self):
        # Developer computer SVG creation
        dev_computer = VGroup()
        screen = Rectangle(width=3, height=2, color=WHITE, fill_color=BLUE_E, fill_opacity=0.5) 
        base = Rectangle(width=3, height=0.5, color=WHITE, fill_color=BLUE_E, fill_opacity=0.5).next_to(screen, DOWN, buff=0)
        dev_computer.add(screen, base)
        return dev_computer

    def create_internet(self):
        # Internet SVG creation
        internet = VGroup()
        earth = Circle(radius=1, color=WHITE, fill_opacity=0.5).set_fill(BLUE_E)
        lines = VGroup(
            Line(start=[-1, 0, 0], end=[1, 0, 0], color=WHITE),
            Line(start=[0, 1, 0], end=[0, -1, 0], color=WHITE),
            Line(start=[-0.7, 0.7, 0], end=[0.7, -0.7, 0], color=WHITE),
            Line(start=[-0.7, -0.7, 0], end=[0.7, 0.7, 0], color=WHITE)
        )
        internet.add(earth, lines)
        return internet

    def create_vercel_logo(self):
        # Vercel logo SVG creation
        vercel_logo = VGroup()
        triangle = Polygon(
            [0, 1, 0], [-0.87, -0.5, 0], [0.87, -0.5, 0],
            color=WHITE, fill_opacity=1
        ).set_stroke(width=0).set_fill(WHITE)
        vercel_logo.add(triangle)
        return vercel_logo