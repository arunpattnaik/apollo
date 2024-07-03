from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("What Makes Next.js Special?", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introductory Text
        intro_text = Text("Next.js is built on top of React and adds amazing features:", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # SSR and SSG features
        features_text = Text("Server-Side Rendering (SSR) and Static Site Generation (SSG)", font_size=28).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(features_text))
        self.wait(2)

        # Comparison of Basic React app and Next.js app
        react_box = Rectangle(color=BLUE, width=5, height=3).shift(LEFT*3 + DOWN*1)
        nextjs_box = Rectangle(color=GREEN, width=5, height=3).shift(RIGHT*3 + DOWN*1)

        react_text = Text("Basic React App", font_size=24).move_to(react_box.get_center())
        nextjs_text = Text("Next.js App", font_size=24).move_to(nextjs_box.get_center())

        self.play(Create(react_box), Create(nextjs_box))
        self.play(Write(react_text), Write(nextjs_text))
        self.wait(1)

        # Adding SSR and SSG labels to Next.js box
        ssr_label = Text("SSR", font_size=24, color=YELLOW).next_to(nextjs_box, UP, buff=0.2)
        ssg_label = Text("SSG", font_size=24, color=ORANGE).next_to(ssr_label, RIGHT, buff=0.5)

        self.play(Write(ssr_label), Write(ssg_label))
        self.wait(1)

        # Pre-rendering comparison (HTML files)
        react_html_text = Text("No pre-rendering", font_size=18).next_to(react_box, DOWN, buff=0.2)
        nextjs_html_text = Text("Pre-rendered pages", font_size=18).next_to(nextjs_box, DOWN, buff=0.2)

        self.play(Write(react_html_text), Write(nextjs_html_text))
        self.wait(2)

        # Summary Text
        summary_text = Text("Next.js helps your website load faster and perform better in search engines!", font_size=28).next_to(features_text, DOWN, buff=2)
        self.play(Write(summary_text))
        self.wait(3)

        # End Scene
        self.play(FadeOut(title), FadeOut(intro_text), FadeOut(features_text), FadeOut(react_box), FadeOut(nextjs_box),
                  FadeOut(react_text), FadeOut(nextjs_text), FadeOut(ssr_label), FadeOut(ssg_label), FadeOut(react_html_text), 
                  FadeOut(nextjs_html_text), FadeOut(summary_text))
        self.wait(1)