from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("CSS Selectors: Targeting Specific Elements", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # List of items
        ul_text = Text("<ul>\n  <li>First item</li>\n  <li>Second item</li>\n  <li>Third item</li>\n</ul>", font_size=24).to_edge(LEFT)
        self.play(Write(ul_text))
        self.wait(1)

        # li selector
        li_selector = Text("li { ... }", font_size=24, color=BLUE).next_to(ul_text, RIGHT, buff=1)
        self.play(Write(li_selector))
        self.wait(1)

        # :first-child pseudo-class
        first_child_selector = Text("li:first-child { color: purple; }", font_size=24, color=PURPLE).next_to(li_selector, DOWN, aligned_edge=LEFT)
        self.play(Write(first_child_selector))
        self.wait(1)

        # Applying first-child style
        ul_text_updated = Text("<ul>\n  <li style='color: purple;'>First item</li>\n  <li>Second item</li>\n  <li>Third item</li>\n</ul>", font_size=24).to_edge(LEFT)
        self.play(FadeOut(ul_text), FadeIn(ul_text_updated))
        self.wait(1)

        # Classes
        class_text = Text("Classes (start with a dot)", font_size=28).next_to(first_child_selector, DOWN, buff=1)
        class_example = Text(".highlight { font-weight: bold; }", font_size=24, color=YELLOW).next_to(class_text, DOWN, buff=0.5)
        self.play(Write(class_text), Write(class_example))
        self.wait(1)

        # Applying class
        ul_text_updated_2 = Text("<ul>\n  <li style='color: purple;'>First item</li>\n  <li class='highlight'>Second item</li>\n  <li>Third item</li>\n</ul>", font_size=24).to_edge(LEFT)
        self.play(FadeOut(ul_text_updated), FadeIn(ul_text_updated_2))
        self.wait(1)

        # IDs
        id_text = Text("IDs (start with a hash)", font_size=28).next_to(class_example, DOWN, buff=1)
        id_example = Text("#main-title { font-size: 24px; }", font_size=24, color=GREEN).next_to(id_text, DOWN, buff=0.5)
        self.play(Write(id_text), Write(id_example))
        self.wait(1)

        # Applying ID
        ul_text_updated_3 = Text("<ul>\n  <li style='color: purple;'>First item</li>\n  <li class='highlight'>Second item</li>\n  <li id='main-title'>Third item</li>\n</ul>", font_size=24).to_edge(LEFT)
        self.play(FadeOut(ul_text_updated_2), FadeIn(ul_text_updated_3))
        self.wait(1)

        # Note highlight and showcasing HTML structure
        highlight_text = Text("<li class='highlight'>Second item</li>", font_size=20, color=YELLOW).next_to(id_example, DOWN)
        id_text_example = Text("<li id='main-title'>Third item</li>", font_size=20, color=GREEN).next_to(highlight_text, DOWN)
        self.play(Write(highlight_text), Write(id_text_example))
        self.wait(2)

        # End Scene
        end_message = Text("You've just learned the basics of HTML and CSS. Keep experimenting!", font_size=28).next_to(id_text_example, DOWN, buff=1)
        self.play(Write(end_message))
        self.wait(3)