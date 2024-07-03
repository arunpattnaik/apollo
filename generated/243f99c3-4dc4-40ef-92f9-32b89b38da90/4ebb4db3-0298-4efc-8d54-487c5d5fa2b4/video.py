from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Static Site Generation (SSG)", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to SSG
        intro_text = Text("Generate HTML at build time for instant load times", font_size=28).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Content-heavy sites examples
        examples_text = Text("Perfect for content-heavy sites like blogs or e-commerce stores", font_size=28).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(examples_text))
        self.wait(2)

        # Example of how SSG works
        example_text = Text("Example of SSG with Next.js", font_size=32).next_to(examples_text, DOWN, buff=0.7).set_color(YELLOW)
        self.play(Write(example_text))
        self.wait(1)

        # SSG Process Visualization
        build_process_text = Text("Build Process", font_size=28).shift(UP*1.5 + LEFT*3)
        self.play(Write(build_process_text))
        
        build_box = Rectangle(height=3, width=3, color=BLUE).next_to(build_process_text, DOWN, buff=0.5)
        build_code = Text("Next.js Code", font_size=20).move_to(build_box.get_center())
        build_group = VGroup(build_box, build_code)
        self.play(FadeIn(build_box), FadeIn(build_code))
        
        arrow = Arrow(start=build_box.get_right(), end=ORIGIN, buff=0.5)
        self.play(GrowArrow(arrow))

        static_html_text = Text("Generated Static HTML", font_size=28).next_to(arrow, RIGHT, buff=0.5)
        html_box = Rectangle(height=3, width=3, color=GREEN).next_to(static_html_text, DOWN, buff=0.5)
        html_content = Text("Static Page", font_size=20).move_to(html_box.get_center())
        html_group = VGroup(html_box, html_content)

        self.play(Write(static_html_text), FadeIn(html_box), FadeIn(html_content))
        self.wait(2)

        # CDN and fast load times
        cdn_text = Text("Served via CDN", font_size=28).next_to(html_group, DOWN, buff=1).set_color(YELLOW)
        self.play(Write(cdn_text))
        self.wait(1)

        fast_load_text = Text("Blazing-fast load times", font_size=28).next_to(cdn_text, DOWN, buff=0.5)
        self.play(Write(fast_load_text))
        self.wait(1)

        # Flexibility and performance benefits
        summary_text = Text("Next.js: Flexibility of React + Performance of SSR and SSG", font_size=32).next_to(fast_load_text, DOWN, buff=1).set_color(GREEN)
        self.play(Write(summary_text))
        self.wait(3)

        # End Scene
        goodbye_text = Text("Happy coding!", font_size=36).next_to(summary_text, DOWN, buff=1).set_color(RED)
        self.play(Write(goodbye_text))
        self.wait(3)