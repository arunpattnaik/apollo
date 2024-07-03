from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("SSR vs SSG in Next.js", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text(
            "SSR (Server-Side Rendering) and SSG (Static Site Generation)\n"
            "are two key features that set Next.js apart.",
            font_size=28,
            line_spacing=0.8
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # SSR Flowchart
        ssr_box = RoundedRectangle(height=2, width=6, color=BLUE).shift(LEFT * 3 + UP * 2)
        ssr_text = Text("SSR Flow", font_size=24).move_to(ssr_box.get_center())
        ssr_users = self.create_ssr_flow().scale(0.5).next_to(ssr_box, DOWN, buff=0.5)

        self.play(Create(ssr_box), Write(ssr_text))
        self.play(FadeIn(ssr_users))
        self.wait(2)

        # SSG Flowchart
        ssg_box = RoundedRectangle(height=2, width=6, color=GREEN).shift(RIGHT * 3 + UP * 2)
        ssg_text = Text("SSG Flow", font_size=24).move_to(ssg_box.get_center())
        ssg_flows = self.create_ssg_flow().scale(0.5).next_to(ssg_box, DOWN, buff=0.5)

        self.play(Create(ssg_box), Write(ssg_text))
        self.play(FadeIn(ssg_flows))
        self.wait(2)

        # SSR vs SSG Explanation
        explanation_text = Text(
            "SSR handles dynamic content efficiently,\n"
            "while SSG is perfect for static content that doesn't change often.",
            font_size=28,
            line_spacing=0.75
        ).shift(DOWN * 2 + RIGHT * 0.5)
        self.play(Write(explanation_text))
        self.wait(4)

    def create_ssr_flow(self):
        user = Dot().set_color(WHITE).move_to(LEFT * 4 + UP * 0.5)
        user_text = Text("User", font_size=20).next_to(user, DOWN, buff=0.1)
        server = Square(side_length=0.5).set_color(BLUE).next_to(user, RIGHT, buff=2)
        server_text = Text("Server", font_size=20).next_to(server, DOWN, buff=0.1)

        user_arrow = Arrow(user.get_center(), server.get_center(), buff=0.1)
        server_arrow = Arrow(server.get_center(), user.get_center(), buff=0.1, path_arc=-PI/2)

        return VGroup(user, user_text, server, server_text, user_arrow, server_arrow)

    def create_ssg_flow(self):
        build = Square(side_length=0.5).set_color(BLUE).move_to(RIGHT * 1 + UP * 0.5)
        build_text = Text("Build", font_size=20).next_to(build, DOWN, buff=0.1)
        file = Triangle().set_color(GREEN).next_to(build, RIGHT, buff=2)
        file_text = Text("File", font_size=20).next_to(file, DOWN, buff=0.1)
        user = Dot().set_color(WHITE).next_to(file, RIGHT, buff=2)
        user_text = Text("User", font_size=20).next_to(user, DOWN, buff=0.1)

        build_arrow = Arrow(build.get_center(), file.get_center(), buff=0.1)
        file_arrow = Arrow(file.get_center(), user.get_center(), buff=0.1, path_arc=-PI/2)

        return VGroup(build, build_text, file, file_text, user, user_text, build_arrow, file_arrow)