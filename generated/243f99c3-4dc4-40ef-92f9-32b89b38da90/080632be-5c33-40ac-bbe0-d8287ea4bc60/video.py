from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Next.js Server-Side Rendering (SSR)", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Explanation text
        ssr_explanation = Text(
            "SSR renders pages on the server before sending to the browser.\n"
            "This means faster load times and better SEO.",
            font_size=28,
            line_spacing=1.5
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(ssr_explanation))
        self.wait(2)
        
        # Flowchart components
        client_box = self.create_box_with_text("Client", color=BLUE).shift(LEFT*3 + UP*2)
        request_arrow = Arrow(client_box.get_right(), client_box.get_right() + RIGHT*2)
        server_box = self.create_box_with_text("Server", color=GREEN).next_to(request_arrow, RIGHT)
        fetch_data_box = self.create_box_with_text("Fetch Data", color=ORANGE).next_to(server_box, DOWN, buff=1.5)
        render_page_box = self.create_box_with_text("Render Page", color=PURPLE).next_to(fetch_data_box, DOWN, buff=1.5)
        response_arrow = Arrow(server_box.get_bottom(), render_page_box.get_top())
        html_arrow = Arrow(render_page_box.get_right(), render_page_box.get_right() + RIGHT*2)
        html_box = self.create_box_with_text("HTML", color=YELLOW).next_to(html_arrow, RIGHT)
        client_html_arrow = Arrow(html_box.get_right(), client_box.get_right() + RIGHT*4)

        self.play(FadeIn(client_box))
        self.play(GrowArrow(request_arrow))
        self.wait(1)
        self.play(FadeIn(server_box))
        self.wait(1)
        self.play(GrowArrow(response_arrow))
        self.wait(1)
        self.play(FadeIn(fetch_data_box))
        self.wait(1)
        self.play(FadeIn(render_page_box))
        self.wait(1)
        self.play(GrowArrow(html_arrow))
        self.wait(1)
        self.play(FadeIn(html_box))
        self.wait(1)
        self.play(GrowArrow(client_html_arrow))
        self.wait(2)
        
        # Performance highlighting
        performance_text = Text(
            "SSR is a game-changer for performance!",
            font_size=32, 
            color=RED
        ).to_edge(DOWN)
        self.play(Write(performance_text))
        self.wait(2)

    def create_box_with_text(self, text, color, width=3, height=1):
        box = Rectangle(width=width, height=height, color=color)
        box_text = Text(text, font_size=22).move_to(box.get_center())
        return VGroup(box, box_text)