from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Next.js", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction Text
        intro_text = Text(
            "Today, we're diving into the world of Next.js, a powerful framework for building React applications.",
            font_size=32
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Tool metaphor
        toolbox_text = Text(
            "Imagine a toolbox filled with the best tools for creating a dynamic, fast, and SEO-friendly website.",
            font_size=28
        ).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(toolbox_text))
        self.wait(2)

        toolbox = self.create_toolbox().scale(0.75).next_to(toolbox_text, DOWN, buff=0.75)
        self.play(FadeIn(toolbox))
        self.wait(2)

        # Next.js comparison
        comparison_text = Text(
            "Next.js offers server-side rendering (SSR) and static site generation (SSG), making your app faster and more efficient.",
            font_size=28
        ).next_to(toolbox, DOWN, buff=0.75)
        self.play(Write(comparison_text))
        self.wait(2)

        # Traditional React app
        react_box = self.create_app_box("Traditional React App", ["Client-Side Rendering"], LEFT * 3)
        self.play(FadeIn(react_box))
        self.wait(2)

        # Next.js app
        nextjs_box = self.create_app_box("Next.js App", ["Server-Side Rendering", "Static Site Generation"], RIGHT * 3)
        self.play(FadeIn(nextjs_box))
        self.wait(2)

        # End Scene
        self.play(
            FadeOut(title),
            FadeOut(intro_text),
            FadeOut(toolbox_text),
            FadeOut(comparison_text),
            FadeOut(toolbox),
            FadeOut(react_box),
            FadeOut(nextjs_box)
        )
        self.wait(1)

    def create_toolbox(self):
        toolbox = VGroup()
        
        box = Rectangle(width=6, height=3, color=BLUE)
        label = Text("Toolbox", font_size=24, color=WHITE).move_to(box.get_center())
        
        toolbox.add(box, label)
        return toolbox
    
    def create_app_box(self, title_text, features, position):
        box = VGroup()
        
        outer_box = Rectangle(width=6, height=4, color=WHITE).move_to(position)
        title = Text(title_text, font_size=20, color=BLUE).next_to(outer_box.get_top(), DOWN, buff=0.2)
        
        features_list = VGroup()
        for i, feature in enumerate(features):
            feature_text = Text(feature, font_size=18).next_to(outer_box.get_top(), DOWN * (i + 2), buff=0.2, aligned_edge=LEFT)
            features_list.add(feature_text)
        
        box.add(outer_box, title, features_list)
        return box
