from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Next.js File-Based Routing System", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to file-based routing
        intro_text = Text("In Next.js, routes are linked to files and folders in the 'pages' directory.", font_size=24)
        intro_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Traditional React routing
        react_router_text = Text("Traditional React: React Router", font_size=32, color=BLUE).to_edge(LEFT)
        self.play(Write(react_router_text))
        self.wait(1)
        
        nextjs_routing_text = Text("Next.js Routing: File-based", font_size=32, color=GREEN).to_edge(RIGHT)
        self.play(Write(nextjs_routing_text))
        self.wait(2)

        # Directory structure
        directory_structure = VGroup(
            Text("pages/", font_size=24, color=YELLOW),
            Text("├── index.js", font_size=24),
            Text("├── about.js", font_size=24),
            Text("├── contact.js", font_size=24),
            Text("└── blog/", font_size=24, color=YELLOW),
            Text("    ├── index.js", font_size=24),
            Text("    └── [slug].js", font_size=24)
        ).arrange(DOWN).next_to(intro_text, DOWN, buff=2).to_edge(LEFT, buff=2)

        self.play(Write(directory_structure))
        self.wait(2)

        # Routes
        route_structure = VGroup(
            Text("/ (index.js)", font_size=24, color=YELLOW),
            Text("/about (about.js)", font_size=24),
            Text("/contact (contact.js)", font_size=24),
            Text("/blog (blog/index.js)", font_size=24),
            Text("/blog/[slug] ([slug].js)", font_size=24),
        ).arrange(DOWN).next_to(directory_structure, RIGHT, buff=2).to_edge(RIGHT, buff=2)

        self.play(Write(route_structure))
        self.wait(4)

        # End scene
        self.play(FadeOut(title), FadeOut(intro_text), FadeOut(react_router_text), FadeOut(nextjs_routing_text), FadeOut(directory_structure), FadeOut(route_structure))
        self.wait(1)