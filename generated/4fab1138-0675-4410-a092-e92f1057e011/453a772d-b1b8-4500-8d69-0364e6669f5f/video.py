from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Linking CSS to HTML", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction of the three methods
        intro_text = Text("There are three ways to link CSS to HTML:", font_size=36).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        inline_css_title = Text("1. Inline CSS", font_size=36, color=BLUE).to_edge(LEFT).shift(UP)
        inline_css_example = Text("<h1 style='color: green;'>Hello, World!</h1>", font_size=28, color=YELLOW).next_to(inline_css_title, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(inline_css_title))
        self.play(Write(inline_css_example))
        self.wait(2)

        internal_css_title = Text("2. Internal CSS", font_size=36, color=BLUE).next_to(inline_css_title, DOWN, buff=1)
        internal_css_example = Text(
            "<head>\n"
            "  <style>\n"
            "    h1 { color: blue; }\n"
            "  </style>\n"
            "</head>", 
            font_size=28, 
            color=YELLOW,
            line_spacing=1.2
        ).next_to(internal_css_title, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(internal_css_title))
        self.play(Write(internal_css_example))
        self.wait(2)
        
        external_css_title = Text("3. External CSS", font_size=36, color=BLUE).next_to(internal_css_title, DOWN, buff=1)
        external_css_example_html = Text(
            "<head>\n"
            "  <link rel='stylesheet' type='text/css' href='styles.css'>\n"
            "</head>", 
            font_size=28, 
            color=YELLOW,
            line_spacing=1.2
        ).next_to(external_css_title, DOWN, buff=0.3, aligned_edge=LEFT)
        external_css_example_css = Text(
            "/* styles.css */\n"
            "h1 { color: red; }", 
            font_size=28, 
            color=GREEN,
            line_spacing=1.2
        ).next_to(external_css_example_html, DOWN, buff=0.7, aligned_edge=LEFT)
        self.play(Write(external_css_title))
        self.play(Write(external_css_example_html))
        self.wait(1)
        self.play(Write(external_css_example_css))
        self.wait(2)
        
        # Highlighting the benefit of external CSS
        benefit_text = Text(
            "External CSS keeps our HTML clean and organized,\n"
            "making it easier to maintain.",
            font_size=32
        ).to_edge(DOWN, buff=1)
        self.play(Write(benefit_text))
        self.wait(3)