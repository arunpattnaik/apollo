from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Server-Side Rendering (SSR)", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # SSR Explanation
        ssr_text = Text("Server generates full HTML before sending to client.", font_size=28)
        ssr_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(ssr_text))
        self.wait(2)

        # SSR Timeline
        self.display_timeline("SSR Timeline", ssr_text)
        self.wait(2)
    
    def display_timeline(self, timeline_title, reference_point):
        # Title for the timeline
        timeline_title_text = Text(timeline_title, font_size=32).next_to(reference_point, DOWN, buff=1)
        self.play(Write(timeline_title_text))
        self.wait(1)

        # Elements in the Timeline
        server_box = self.create_server_box().to_edge(LEFT, buff=2).shift(DOWN)
        self.play(FadeIn(server_box))
        
        arrow_to_browser = Arrow(start=server_box.get_right(), end=RIGHT * 2 + DOWN, buff=0.2)
        browser_box = self.create_browser_box().next_to(arrow_to_browser, RIGHT, buff=0.2)
        
        self.play(GrowArrow(arrow_to_browser), FadeIn(browser_box))
        self.wait(1)

        # Labels under the Boxes
        server_label = Text("Server", font_size=20).next_to(server_box, DOWN, buff=0.2)
        browser_label = Text("Browser", font_size=20).next_to(browser_box, DOWN, buff=0.2)
        
        self.play(Write(server_label), Write(browser_label))
        self.wait(1)

        # Indicate "Time to Interactive"
        tti_text = Text("Time to Interactive", font_size=20, color=GREEN).next_to(browser_box, UP, buff=0.5)
        self.play(Write(tti_text))
        self.wait(1)

    def create_server_box(self):
        server_box = VGroup()
        
        # Server box outline and label
        box = Rectangle(width=4, height=2, color=WHITE)
        box_label = Text("Rendering HTML", font_size=20).move_to(box.get_center())

        server_box.add(box, box_label)
        return server_box

    def create_browser_box(self):
        browser_box = VGroup()
        
        # Browser box outline and label
        box = Rectangle(width=4, height=2, color=WHITE)
        box_label = Text("Content Loaded", font_size=20).move_to(box.get_center())

        browser_box.add(box, box_label)
        return browser_box

