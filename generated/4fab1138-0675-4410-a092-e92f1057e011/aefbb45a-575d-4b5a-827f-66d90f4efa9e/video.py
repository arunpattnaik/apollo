from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to CSS", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Display a simple CSS file
        css_code = VGroup(
            Text("/* Simple CSS File */", font_size=32),
            Text("h1 {", font_size=32),
            Text("    color: blue;", font_size=32),
            Text("}", font_size=32),
            Text("p {", font_size=32),
            Text("    color: red;", font_size=32),
            Text("    font-size: 20px;", font_size=32),
            Text("}", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.75)
        
        css_code.to_edge(LEFT)
        
        self.play(FadeIn(css_code), run_time=4)
        self.wait(2)

        # Show HTML code example
        html_code_h1 = Text("<h1>This is a Heading</h1>", font_size=32, color=BLUE).to_edge(RIGHT).shift(UP*2)
        html_code_p = Text("<p>This is a paragraph.</p>", font_size=32, color=RED).next_to(html_code_h1, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(Write(html_code_h1), run_time=2)
        self.wait(1)

        # Adding CSS styles
        self.play(css_code[1].animate.set_color(BLUE))
        self.play(css_code[2].animate.set_color(BLUE))
        self.wait(1)

        self.play(Transform(html_code_h1, Text("<h1>This is a Heading</h1>", font_size=32, color=BLUE).to_edge(RIGHT).shift(UP*2)))
        self.wait(1)

        self.play(Write(html_code_p), run_time=2)
        self.wait(1)

        self.play(css_code[4].animate.set_color(RED), css_code[5].animate.set_color(RED), css_code[6].animate.set_color(RED))
        self.wait(1)

        self.play(Transform(html_code_p, Text("<p>This is a paragraph.</p>", font_size=32, color=RED).next_to(html_code_h1, DOWN, buff=0.5, aligned_edge=LEFT)))
        self.wait(1)

        # Explain CSS properties
        explanation = Text("CSS uses properties like color, font-size, and margin to style elements.", font_size=24).next_to(html_code_p, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(explanation), run_time=3)
        self.wait(2)

        final_explanation = Text("See how CSS transforms the look of our HTML?", font_size=24).next_to(explanation, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(final_explanation), run_time=2)
        self.wait(3)

        # End Scene
        self.play(FadeOut(title), FadeOut(css_code), FadeOut(html_code_h1), FadeOut(html_code_p), FadeOut(explanation), FadeOut(final_explanation))
        self.wait(1)