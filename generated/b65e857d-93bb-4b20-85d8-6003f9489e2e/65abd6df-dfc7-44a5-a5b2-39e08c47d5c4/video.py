from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Dynamic Routing and Data Fetching in Next.js", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Dynamic Routing Text
        dynamic_routing_text = Text("Dynamic Routing", font_size=32, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(Write(dynamic_routing_text))
        self.wait(1)

        # Example of dynamic routing
        example_route = Text("/posts/[id]", font_size=28).next_to(dynamic_routing_text, DOWN, buff=0.5)
        self.play(Write(example_route))
        self.wait(1)

        # Data Fetching Methods Text
        data_fetching_text = Text("Data Fetching Methods", font_size=32, color=GREEN).next_to(example_route, DOWN, buff=0.5)
        self.play(Write(data_fetching_text))
        self.wait(1)

        # Examples of data fetching methods
        fetching_methods = VGroup(
            Text("getStaticProps", font_size=28),
            Text("getServerSideProps", font_size=28),
            Text("getStaticPaths", font_size=28),
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(data_fetching_text, DOWN, buff=0.5, aligned_edge=LEFT)

        for method in fetching_methods:
            self.play(Write(method))
            self.wait(1)

        # Visual representation of data fetching process
        server_box = self.create_labelled_box("Server", RED).scale(0.5).to_edge(LEFT, buff=1).shift(DOWN*2)
        page_box = self.create_labelled_box("Page", BLUE).scale(0.5).to_edge(RIGHT, buff=1).shift(DOWN*2)
        data_arrow = Arrow(server_box.get_right(), page_box.get_left(), buff=0.1)
        
        self.play(FadeIn(server_box), FadeIn(page_box), GrowArrow(data_arrow))
        self.wait(1)

        # End Scene
        conclusion = Text("With these tools, you can build highly dynamic\nand data-driven applications with ease.", font_size=30).shift(DOWN*2)
        self.play(Write(conclusion), FadeOut(server_box), FadeOut(page_box), FadeOut(data_arrow))
        self.wait(2)

    def create_labelled_box(self, text, color):
        box = VGroup()
        rectangle = Rectangle(width=2, height=1, color=color)
        label = Text(text, font_size=24, color=color).move_to(rectangle.get_center())
        box.add(rectangle, label)
        return box