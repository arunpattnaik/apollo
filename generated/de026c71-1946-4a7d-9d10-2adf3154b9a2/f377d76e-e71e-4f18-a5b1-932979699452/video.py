from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Static Site Generation (SSG) in Next.js", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Description of SSG
        ssg_text = Text(
            "HTML is generated at build time, not on each request.",
            font_size=30
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(ssg_text))
        self.wait(1)

        # Imagine having a blog
        blog_text = Text(
            "Imagine you have a blog with hundreds of posts.",
            font_size=30
        ).next_to(ssg_text, DOWN, buff=0.5)
        self.play(Write(blog_text))
        self.wait(1)

        # Generate HTML files once
        generate_text = Text(
            "Next.js generates all the HTML files once,",
            font_size=30
        ).next_to(blog_text, DOWN, buff=0.5)
        serve_text = Text(
            "and serves them directly.",
            font_size=30
        ).next_to(generate_text, DOWN, buff=0.2)
        self.play(Write(generate_text))
        self.play(Write(serve_text))
        self.wait(1)

        # Flowchart showing SSR vs SSG
        ssr_text = Text("Server-Side Rendering (SSR)", font_size=24, color=BLUE)
        ssg_text = Text("Static Site Generation (SSG)", font_size=24, color=GREEN)

        request_1 = Rectangle(width=2, height=1, color=BLUE).to_edge(LEFT).shift(UP*1)
        response_1 = Rectangle(width=2, height=1, color=BLUE).next_to(request_1, RIGHT, buff=1)
        for _ in range(2):
            request_1.add(request_1.copy().next_to(response_1, RIGHT, buff=1).shift(LEFT))

        request_2 = Rectangle(width=2, height=1, color=GREEN).to_edge(LEFT).shift(DOWN*1)
        response_2 = Rectangle(width=2, height=1, color=GREEN).next_to(request_2, RIGHT, buff=1)
        for _ in range(2):
            request_2.add(request_2.copy().next_to(response_2, RIGHT, buff=1).shift(LEFT))

        ssr_flow = Group(ssr_text, request_1, response_1, request_1[1:], response_1[1:])
        ssr_flow.arrange(RIGHT, buff=0.5).shift(UP*1.5)
        self.play(FadeIn(ssr_flow), ssr_text.animate.shift(LEFT*0.75))

        ssg_flow = Group(ssg_text, request_2, response_2, request_2[1:], response_2[1:])
        ssg_flow.arrange(RIGHT, buff=0.5).shift(DOWN*0.5)
        self.play(FadeIn(ssg_flow), ssg_text.animate.shift(LEFT*0.75))

        self.wait(3)

        # Key takeaway
        takeaway = Text(
            "Makes your site incredibly fast.", font_size=36,
            color=YELLOW
        ).next_to(ssg_flow, DOWN, buff=1)
        self.play(Write(takeaway))
        self.wait(2)