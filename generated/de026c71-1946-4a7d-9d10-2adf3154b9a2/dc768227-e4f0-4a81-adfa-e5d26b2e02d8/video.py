from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("What Makes Next.js Special?", font_size=44).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to SSR
        ssr_intro = Text("One of its standout features is server-side rendering (SSR).", font_size=30).next_to(title, DOWN, buff=0.5)
        self.play(Write(ssr_intro))
        self.wait(2)

        # Explanation of SSR with Text
        ssr_explanation_part1 = Text("Normally, with a React app, the browser downloads a JavaScript file", font_size=28).next_to(ssr_intro, DOWN, buff=0.5)
        ssr_explanation_part2 = Text("and runs it to generate the HTML.", font_size=28).next_to(ssr_explanation_part1, DOWN)
        ssr_explanation_part3 = Text("But with SSR, the server generates the HTML", font_size=28).next_to(ssr_explanation_part2, DOWN, buff=0.5)
        ssr_explanation_part4 = Text("before sending it to the browser.", font_size=28).next_to(ssr_explanation_part3, DOWN)
        
        self.play(Write(ssr_explanation_part1))
        self.play(Write(ssr_explanation_part2))
        self.play(Write(ssr_explanation_part3))
        self.play(Write(ssr_explanation_part4))
        self.wait(2)

        # Performance and SEO benefits with SSR
        benefits_text = Text("This means faster load times and better SEO.", font_size=30).next_to(ssr_explanation_part4, DOWN, buff=0.5)
        self.play(Write(benefits_text))
        self.wait(2)

        # Displaying comparison of React app with and without SSR
        comparison_title = Text("React App: With and Without SSR", font_size=34).next_to(benefits_text, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(comparison_title))
        self.wait(1)

        # Non-SSR React App Simulation
        no_ssr_group = self.create_react_simulation("Without SSR").next_to(comparison_title, DOWN, buff=1).shift(LEFT*2)
        self.play(FadeIn(no_ssr_group))
        self.wait(1)

        # SSR React App Simulation
        ssr_group = self.create_react_simulation("With SSR").next_to(no_ssr_group, RIGHT, buff=1)
        self.play(FadeIn(ssr_group))
        self.wait(1)

        # Emphasizing the difference in load time
        self.play(Indicate(no_ssr_group, color=RED), Indicate(ssr_group, color=GREEN))
        self.wait(3)

    def create_react_simulation(self, title):
        container = VGroup()
        
        # Mock Browser
        browser_outline = Rectangle(width=5, height=3, color=WHITE)
        address_bar = Rectangle(width=4.5, height=0.3, color=BLUE).shift(UP * 1.1)
        content_box = Rectangle(width=4.5, height=2.2, color=GRAY).shift(DOWN * 0.2)
        
        # Content
        content = Text("Content goes here...", font_size=20, color=WHITE).move_to(content_box.get_center())
        address_text = Text("http://example.com", font_size=16, color=WHITE).move_to(address_bar.get_center())
        
        # Title
        comparison_title = Text(title, font_size=24).next_to(browser_outline, UP, buff=0.3)
        
        container.add(browser_outline, address_bar, content_box, content, address_text, comparison_title)
        return container