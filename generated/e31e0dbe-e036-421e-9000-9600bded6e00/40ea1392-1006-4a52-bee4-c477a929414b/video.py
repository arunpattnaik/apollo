from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Benefits and Trade-offs of SSR", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Explanation
        explanation = Text("SSR improves performance and SEO but increases server load.", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(1)

        # Pros and Cons List
        pros_title = Text("Pros", font_size=36, color=GREEN).to_edge(LEFT).shift(UP*2)
        cons_title = Text("Cons", font_size=36, color=RED).to_edge(RIGHT).shift(UP*2)

        pros_list = VGroup(
            Text("1. Better SEO", font_size=30),
            Text("2. Improved Performance", font_size=30),
            Text("3. Instant Page Load", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(pros_title, DOWN, aligned_edge=LEFT, buff=0.5)

        cons_list = VGroup(
            Text("1. Increased Server Load", font_size=30),
            Text("2. More Complex Setup", font_size=30),
            Text("3. Potential Caching Issues", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(cons_title, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(pros_title), Write(cons_title))
        self.wait(1)
        self.play(Write(pros_list))
        self.wait(1)
        self.play(Write(cons_list))
        self.wait(2)

        # Reminder Text
        reminder_text = Text("The best choice depends on your specific needs.", font_size=28).next_to(explanation, DOWN, buff=2)
        self.play(Write(reminder_text))
        self.wait(2)

        # Thank you message
        thank_you_text = Text("Thanks for joining me today,\n I hope you now understand SSR in React!", font_size=32).next_to(reminder_text, DOWN, buff=1)
        self.play(Write(thank_you_text))
        self.wait(3)