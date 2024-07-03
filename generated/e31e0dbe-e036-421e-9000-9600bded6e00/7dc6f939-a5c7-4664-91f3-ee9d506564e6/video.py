from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Client-Side Rendering (CSR) with React", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step descriptions
        description_text = Text(
            "In CSR, your browser downloads a minimal HTML,\nfetches the JavaScript, then React takes over\nto render the content.",
            font_size=30
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(description_text))
        self.wait(3)

        # Timeline
        timeline = NumberLine(x_range=[0, 10, 1], length=10, color=BLUE, include_numbers=False)
        timeline.next_to(description_text, DOWN, buff=1)
        
        initial_request_label = Text("Initial Request", font_size=24).next_to(timeline.number_to_point(1), UP)
        download_js_label = Text("Download JS", font_size=24).next_to(timeline.number_to_point(5), UP)
        render_content_label = Text("Render Content", font_size=24).next_to(timeline.number_to_point(8), UP)
        time_to_interactive_label = Text("Time to Interactive", font_size=24, color=RED).next_to(timeline, DOWN, buff=0.5).shift(RIGHT*2)

        self.play(Create(timeline))
        self.play(Write(initial_request_label), Write(download_js_label), Write(render_content_label))
        self.wait(2)

        # Highlighting the gap (time to interactive)
        gap_line = DoubleArrow(start=timeline.number_to_point(1), end=timeline.number_to_point(8), color=RED, buff=0)
        self.play(Create(gap_line))
        self.play(Write(time_to_interactive_label))
        self.wait(2)
        
        # End Scene
        self.play(FadeOut(title), FadeOut(description_text), FadeOut(timeline), FadeOut(initial_request_label), 
                  FadeOut(download_js_label), FadeOut(render_content_label), FadeOut(gap_line), FadeOut(time_to_interactive_label))
        self.wait(1)