from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Exploring CSS Properties", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Define colors
        LIGHT_BLUE = "#ADD8E6"

        # Box styling demonstration
        box = Rectangle(width=4, height=2, fill_color=LIGHT_BLUE, fill_opacity=1, stroke_color=BLACK).shift(UP*0.5)
        box_text = Text("This is a box", font_size=24).move_to(box.get_center())
        self.play(FadeIn(box), Write(box_text))
        self.wait(1)

        # CSS properties
        css_text = Text(".box {", font_size=32).to_edge(LEFT).shift(DOWN*1.5)
        width_text = Text("width: 200px;", font_size=28).next_to(css_text, RIGHT, buff=0.3)
        height_text = Text("height: 100px;", font_size=28).next_to(width_text, DOWN, aligned_edge=LEFT)
        bg_color_text = Text("background-color: lightblue;", font_size=28).next_to(height_text, DOWN, aligned_edge=LEFT)
        border_text = Text("border: 1px solid black;", font_size=28).next_to(bg_color_text, DOWN, aligned_edge=LEFT)
        closing_brace = Text("}", font_size=32).next_to(border_text, DOWN, aligned_edge=LEFT)
        
        css_group = VGroup(css_text, width_text, height_text, bg_color_text, border_text, closing_brace)
        self.play(Write(css_text))
        self.play(Write(width_text))
        self.play(Write(height_text))
        self.play(Write(bg_color_text))
        self.play(Write(border_text))
        self.play(Write(closing_brace))
        self.wait(1)

        # Box styles adjustment
        self.play(box.animate.set_width(4), 
                  box.animate.set_height(2), 
                  box.animate.set_fill(color=LIGHT_BLUE), 
                  box.animate.set_stroke(color=BLACK, width=1))
        self.wait(1)

        # Adding padding and margin
        new_css_text = Text(".box {", font_size=32).to_edge(LEFT).shift(DOWN*2.5)
        padding_text = Text("padding: 10px;", font_size=28).next_to(new_css_text, RIGHT, buff=0.3)
        margin_text = Text("margin: 20px;", font_size=28).next_to(padding_text, DOWN, aligned_edge=LEFT)
        new_closing_brace = Text("}", font_size=32).next_to(margin_text, DOWN, aligned_edge=LEFT)
        
        new_css_group = VGroup(new_css_text, padding_text, margin_text, new_closing_brace)
        self.play(Write(new_css_text))
        self.play(Write(padding_text))
        self.play(Write(margin_text))
        self.play(Write(new_closing_brace))
        self.wait(1)

        # Adjust box with padding and margin
        padded_box = Rectangle(width=4.4, height=2.4, fill_color=LIGHT_BLUE, fill_opacity=1, stroke_color=BLACK).shift(UP*0.5+LEFT*2.6)
        margin_rect = Rectangle(width=5*1.5, height=3.4, fill_opacity=0, stroke_color=GREEN).shift(UP*0.5+LEFT*2.6)
        padded_text = Text("Padding: 10px inside", font_size=20).next_to(padded_box, DOWN)
        margin_text = Text("Margin: 20px outside", font_size=20).next_to(margin_rect, UP)

        self.play(Transform(box, padded_box), 
                  Write(padded_text))
        self.wait(1)
        self.play(FadeIn(margin_rect), 
                  Write(margin_text))
        self.wait(1)

        # End Scene
        self.wait(2)