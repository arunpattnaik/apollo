from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("A Whirlwind Tour of Next.js", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Intuitive routing
        routing_text = Text("Intuitive Routing", font_size=36, color=BLUE).shift(UP*2)
        self.play(Write(routing_text))
        self.wait(1)

        routing_desc = Text("File-based routing system.", font_size=24).next_to(routing_text, DOWN)
        self.play(Write(routing_desc))
        self.wait(1)

        # Server-side rendering
        ssr_text = Text("Server-Side Rendering", font_size=36, color=GREEN).next_to(routing_desc, DOWN, buff=0.5)
        self.play(Write(ssr_text))
        self.wait(1)

        ssr_desc = Text("Render pages on the server.", font_size=24).next_to(ssr_text, DOWN)
        self.play(Write(ssr_desc))
        self.wait(1)

        # API Routes
        api_text = Text("API Routes", font_size=36, color=PURPLE).next_to(ssr_desc, DOWN, buff=0.5)
        self.play(Write(api_text))
        self.wait(1)

        api_desc = Text("Create full API endpoints.", font_size=24).next_to(api_text, DOWN)
        self.play(Write(api_desc))
        self.wait(1)
        
        # Dynamic Data Fetching
        dynamic_text = Text("Dynamic Data Fetching", font_size=36, color=ORANGE).next_to(api_desc, DOWN, buff=0.5)
        self.play(Write(dynamic_text))
        self.wait(1)

        dynamic_desc = Text("Fetch data at build time.", font_size=24).next_to(dynamic_text, DOWN)
        self.play(Write(dynamic_desc))
        self.wait(1)
        
        # Closing statement
        closing_text = Text("Start Building with Next.js!", font_size=36, color=YELLOW).next_to(dynamic_desc, DOWN, buff=1)
        closing_desc = Text("Happy Coding!", font_size=36, color=WHITE).next_to(closing_text, DOWN)
        self.play(Write(closing_text))
        self.wait(1)
        self.play(Write(closing_desc))

        self.wait(3)