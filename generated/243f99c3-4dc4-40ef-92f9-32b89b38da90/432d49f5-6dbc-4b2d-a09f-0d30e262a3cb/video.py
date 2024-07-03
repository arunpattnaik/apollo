from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Welcome to Next.js", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text = Text(
            "Today, we're diving into the world of Next.js,"
            "\na powerful framework for building React applications.",
            font_size=30
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Toolbox metaphor
        toolbox_text = Text(
            "Imagine you have a toolbox",
            font_size=30
        ).next_to(intro_text, DOWN, buff=0.5)
        tools_text = Text(
            "filled with all the best tools to create a dynamic,\nfast, and SEO-friendly website.",
            font_size=30
        ).next_to(toolbox_text, DOWN, buff=0.5)
        self.play(Write(toolbox_text))
        self.wait(1)
        self.play(Write(tools_text))
        self.wait(2)

        # Next.js offering
        nextjs_offers_text = Text("That's what Next.js offers!", font_size=30, color=GREEN).next_to(tools_text, DOWN, buff=0.5)
        self.play(Write(nextjs_offers_text))
        self.wait(2)

        # Simple React App
        react_app_text = Text("Simple React App", font_size=35, color=WHITE).shift(LEFT*3 + UP*2)
        react_app_box = Rectangle(width=5, height=3, color=WHITE).surround(react_app_text)
        react_group = VGroup(react_app_text, react_app_box)

        self.play(FadeIn(react_group))
        self.wait(1)

        # Transforming it using Next.js
        transform_text = Text("Transform it using Next.js", font_size=30, color=YELLOW).shift(RIGHT*2 + UP*2)
        arrow = Arrow(start=react_group.get_right(), end=transform_text.get_left(), buff=0.5)
        
        self.play(Write(transform_text), GrowArrow(arrow))
        self.wait(1)

        # Final Next.js App
        nextjs_app_text = Text("Next.js App", font_size=35, color=WHITE).shift(RIGHT*2 + DOWN*1)
        nextjs_app_box = Rectangle(width=5, height=3, color=WHITE).surround(nextjs_app_text)
        nextjs_group = VGroup(nextjs_app_text, nextjs_app_box)
        
        self.play(FadeIn(nextjs_group))
        self.wait(3)

        # End Scene
        ready_text = Text("Ready? Let's get started!", font_size=30, color=RED).next_to(nextjs_group, DOWN, buff=1)
        self.play(Write(ready_text))
        self.wait(2)