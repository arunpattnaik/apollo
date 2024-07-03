from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("How Vercel Makes Web Development Smooth", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction Text
        intro_text = Text("Vercel integrates seamlessly with modern web frameworks like Next.js, React, and more.", font_size=30).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Framework Logos
        react_logo = self.create_logo("React", hex_color="#61DAFB").scale(0.5).shift(LEFT*4 + UP)
        nextjs_logo = self.create_logo("Next.js", hex_color="#000000").scale(0.5).next_to(react_logo, RIGHT, buff=1)
        vue_logo = self.create_logo("Vue", hex_color="#4FC08D").scale(0.5).next_to(nextjs_logo, RIGHT, buff=1)
        vercel_logo = self.create_logo("Vercel", hex_color="#000000").scale(0.6).shift(DOWN*1.5)

        self.play(FadeIn(react_logo), FadeIn(nextjs_logo), FadeIn(vue_logo))
        self.wait(1)

        # Connecting Frameworks to Vercel
        react_arrow = Arrow(react_logo.get_bottom(), vercel_logo.get_top(), buff=0.1, color=WHITE)
        nextjs_arrow = Arrow(nextjs_logo.get_bottom(), vercel_logo.get_top(), buff=0.1, color=WHITE)
        vue_arrow = Arrow(vue_logo.get_bottom(), vercel_logo.get_top(), buff=0.1, color=WHITE)
        
        self.play(Write(react_arrow), Write(nextjs_arrow), Write(vue_arrow), FadeIn(vercel_logo))
        self.wait(2)

        # Features Text
        features_text = Text("Optimizes for performance and scalability", font_size=28).next_to(vercel_logo, DOWN, buff=1)
        server_side_text = Text("Server-side Rendering", font_size=24).shift(LEFT*3 + DOWN*3)
        static_site_text = Text("Static Site Generation", font_size=24).next_to(server_side_text, RIGHT, buff=1.5)
        edge_functions_text = Text("Edge Functions", font_size=24).next_to(static_site_text, RIGHT, buff=1.5)
        
        self.play(Write(features_text))
        self.wait(1)

        self.play(FadeIn(server_side_text), FadeIn(static_site_text), FadeIn(edge_functions_text))
        self.wait(2)

    def create_logo(self, text, hex_color):
        logo = VGroup()
        circle = Circle(color=hex_color, fill_opacity=1).set_height(1)
        label = Text(text[0], font_size=48, color=WHITE).move_to(circle.get_center())
        logo.add(circle, label)
        return logo