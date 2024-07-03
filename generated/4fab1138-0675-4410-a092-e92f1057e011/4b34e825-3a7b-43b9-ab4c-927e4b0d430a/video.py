from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("HTML and CSS: Structure and Styling", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to HTML
        intro_text = Text("HTML: The Skeleton of a Webpage", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # Simple HTML document visualization
        html_code = """<!DOCTYPE html>
<html>
<head>
    <title>My Webpage</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
</body>
</html>"""

        html_code_mobject = Code(
            code=html_code,
            tab_width=4,
            background="window",
            language="html",
            insert_line_no=False,
            style="monokai",
            font="Courier",
            font_size=24,
            line_spacing=0.5,
        ).scale(0.5).next_to(intro_text, DOWN, buff=0.5)
        
        self.play(FadeIn(html_code_mobject))
        self.wait(2)

        # Highlighting <!DOCTYPE html>
        doctype = SurroundingRectangle(html_code_mobject[0], color=YELLOW, buff=0.1)
        doctype_label = Text("<!DOCTYPE html>", font_size=24, color=YELLOW).next_to(doctype, RIGHT, buff=0.2)
        self.play(Create(doctype), Write(doctype_label))
        self.wait(2)
        self.play(FadeOut(doctype), FadeOut(doctype_label))

        # Highlighting <html> tag
        html_tag = SurroundingRectangle(html_code_mobject[1], color=GREEN, buff=0.1)
        html_tag_label = Text("<html> ... </html>", font_size=24, color=GREEN).next_to(html_tag, RIGHT, buff=0.2)
        self.play(Create(html_tag), Write(html_tag_label))
        self.wait(2)
        self.play(FadeOut(html_tag), FadeOut(html_tag_label))

        # Highlighting <head> and <body>
        head_tag = SurroundingRectangle(html_code_mobject[2:5], color=BLUE, buff=0.1)
        head_tag_label = Text("<head> ... </head>", font_size=24, color=BLUE).next_to(head_tag, RIGHT, buff=0.2)
        body_tag = SurroundingRectangle(html_code_mobject[6:], color=RED, buff=0.1)
        body_tag_label = Text("<body> ... </body>", font_size=24, color=RED).next_to(body_tag, RIGHT, buff=0.2)
        
        self.play(Create(head_tag), Write(head_tag_label))
        self.wait(2)
        self.play(Create(body_tag), Write(body_tag_label))
        self.wait(2)
        self.play(FadeOut(head_tag), FadeOut(head_tag_label), FadeOut(body_tag), FadeOut(body_tag_label))
        
        # Adding H1 and Paragraph
        h1_tag = Text("<h1>Hello, World!</h1>", font_size=32, color=BLUE).to_edge(LEFT).shift(RIGHT * 2.5).shift(UP * 1.5)
        self.play(Write(h1_tag))
        self.wait(1)

        paragraph_tag = Text("<p>This is a paragraph.</p>", font_size=32, color=WHITE).to_edge(LEFT).shift(RIGHT * 3.8).shift(DOWN)
        self.play(Write(paragraph_tag))
        self.wait(2)
        
        # Thanks Text
        thanks_text = Text("That's HTML in action!", font_size=36).next_to(paragraph_tag, DOWN, buff=1)
        self.play(Write(thanks_text))
        self.wait(3)