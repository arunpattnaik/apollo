from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Next.js: Transforming React Applications", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text = Text(
            "Next.js: A powerful framework for building React applications.",
            font_size=30
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # Toolbox metaphor
        toolbox_text = Text(
            "Next.js is like a toolbox for React developers.",
            font_size=30
        ).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(toolbox_text))
        self.wait(1)

        toolbox_image = self.create_toolbox().next_to(toolbox_text, DOWN, buff=0.5)
        self.play(FadeIn(toolbox_image))
        self.wait(1)

        # Simple React app visualization
        react_app_text = Text(
            "Simple React App",
            font_size=24
        ).shift(LEFT * 3 + UP * 2)
        self.play(Write(react_app_text))
        self.wait(1)

        react_app_image = self.create_react_app().next_to(react_app_text, DOWN, buff=0.5)
        self.play(FadeIn(react_app_image))
        self.wait(1)

        # Transforming using Next.js
        transforming_text = Text("Transforming using Next.js", font_size=24, color=BLUE).next_to(react_app_image, RIGHT, buff=1)
        arrow = Arrow(LEFT, RIGHT, buff=0.5).next_to(react_app_image, RIGHT)
        
        self.play(Write(transforming_text), FadeIn(arrow))
        self.wait(1)

        next_js_app_text = Text("Next.js App", font_size=24).next_to(arrow, RIGHT, buff=1)
        self.play(Write(next_js_app_text))
        self.wait(1)
        
        next_js_app_image = self.create_next_js_app().next_to(next_js_app_text, DOWN, buff=0.5)
        self.play(FadeIn(next_js_app_image))
        self.wait(2)

        # End Scene
        ready_text = Text("Ready? Let's get started!", font_size=36).to_edge(DOWN, buff=1)
        self.play(Write(ready_text))
        self.wait(3)

    def create_toolbox(self):
        toolbox = VGroup()
        
        # Toolbox shape
        base = Rectangle(width=4, height=2, color=RED).shift(DOWN * 0.5)
        lid = Rectangle(width=4.2, height=0.5, color=RED).next_to(base, UP, buff=0)
        handle = Line(UP * 0.5, DOWN * 0.5, color=RED).move_to(lid.get_top())
        
        # Tools inside toolbox
        hammer = Line(start=DOWN, end=UP, color=GRAY).next_to(base.get_left(), buff=-0.3)
        wrench = Line(start=DOWN, end=UP, color=GRAY).next_to(base.get_right(), buff=-0.3)
        
        toolbox.add(base, lid, handle, hammer, wrench)
        return toolbox

    def create_react_app(self):
        react_app = VGroup()
        
        # App window
        window = Rectangle(width=4, height=3, color=BLUE, fill_opacity=0.5)
        text = Text("React App", font_size=20, color=BLACK).move_to(window.get_center())
        
        react_app.add(window, text)
        return react_app

    def create_next_js_app(self):
        next_js_app = VGroup()
        
        # App window with a slightly different shape or features
        window = Rectangle(width=4, height=3, color=GREEN, fill_opacity=0.5)
        text = Text("Next.js App", font_size=20, color=BLACK).move_to(window.get_center())
        
        next_js_app.add(window, text)
        return next_js_app