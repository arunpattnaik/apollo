from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Server-Side Rendering (SSR) in React", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to SSR
        intro_text = Text("Imagine the server does most of the heavy lifting.", font_size=28).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # CSR vs SSR Texts
        csr_text = Text("Client-Side Rendering (CSR)", font_size=30, color=BLUE).to_edge(LEFT).shift(UP*1)
        ssr_text = Text("Server-Side Rendering (SSR)", font_size=30, color=GREEN).to_edge(RIGHT).shift(UP*1)
        self.play(Write(csr_text), Write(ssr_text))
        self.wait(2)

        # CSR Details
        browser_csr = self.create_browser("Browser does all the work").scale(0.5).next_to(csr_text, DOWN, buff=0.5)
        js_csr = Text("JavaScript is processed in the browser", font_size=24).next_to(browser_csr, DOWN, buff=0.5)
        self.play(FadeIn(browser_csr))
        self.play(Write(js_csr))
        self.wait(2)

        # SSR Details
        server_ssr = self.create_server("Server renders the page").scale(0.5).next_to(ssr_text, DOWN, buff=0.5)
        html_ssr = Text("Server sends fully rendered page", font_size=24).next_to(server_ssr, DOWN, buff=0.5)
        self.play(FadeIn(server_ssr))
        self.play(Write(html_ssr))
        self.wait(2)

        # Summary of CSR vs SSR
        summary_text = Text(
            "In CSR, the browser handles everything.\n"
            "In SSR, the server sends a fully rendered page.",
            font_size=28
        ).to_edge(DOWN)
        self.play(Write(summary_text))
        self.wait(3)

    def create_browser(self, label_text):
        browser = VGroup()
        
        # Browser window outline
        outline = Rectangle(width=4, height=2.5, color=WHITE)
        address_bar = Rectangle(width=3.8, height=0.3, color=BLUE).shift(UP*0.8)
        
        # Address bar elements
        address_text = Text("http://example.com", font_size=10, color=WHITE).scale(0.8).move_to(address_bar.get_center())
        
        # Content area
        content_area = Rectangle(width=3.8, height=1.8, color=GRAY).shift(DOWN*0.15)
        
        # Label
        label = Text(label_text, font_size=14, color=YELLOW).move_to(content_area.get_center()).shift(DOWN*0.6)
        
        browser.add(outline, address_bar, address_text, content_area, label)
        return browser

    def create_server(self, label_text):
        server = VGroup()

        # Server box outline
        outline = Rectangle(width=2.5, height=2.5, color=WHITE)

        # Server elements
        led_dot = Dot(radius=0.1, color=RED).shift(UP*0.85 + LEFT*0.75)
        server_label = Text("Server", font_size=14, color=WHITE).next_to(led_dot, RIGHT, buff=0.2).shift(UP*0.05)
        
        # Label
        label = Text(label_text, font_size=14, color=YELLOW).shift(DOWN*0.3)
        
        server.add(outline, led_dot, server_label, label)
        return server