from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Practical Tips for Starting to Invest", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Main tip about diversification
        diversification_text = Text("Diversify Your Portfolio", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(diversification_text))
        self.wait(1)
        
        # Show Pie Chart illustrating diversification
        labels = [
            Text("Technology", font_size=24, color=RED).move_to(UP*2 + LEFT*2.5),
            Text("Healthcare", font_size=24, color=BLUE).move_to(UP*2 + LEFT*0.5),
            Text("Finance", font_size=24, color=GREEN).move_to(UP*2 + RIGHT*1.5)
        ]
        
        chart = self.create_pie_chart(slices=[0.4, 0.3, 0.3], colors=[RED, BLUE, GREEN])
        chart.next_to(diversification_text, DOWN, buff=1)

        self.play(FadeIn(chart), *[Write(label) for label in labels])
        self.wait(2)

        # Emphasize doing research
        research_text = Text("Do Your Research on Companies", font_size=32).next_to(chart, DOWN, buff=1)
        self.play(Write(research_text))
        self.wait(1)

        # Brokers offer tools
        brokers_text = Text("Use Broker Tools and Resources", font_size=32).next_to(research_text, DOWN, buff=0.5)
        self.play(Write(brokers_text))
        self.wait(2)
        
        # Final message
        final_message = Text("By understanding the basics and starting with a solid plan,\nyou'll be well on your way to successful investing.", font_size=28).next_to(brokers_text, DOWN, buff=1)
        self.play(Write(final_message))
        self.wait(3)
        
        # End Scene
        thanks_text = Text("Thanks for joining me today, and happy investing!", font_size=36).next_to(final_message, DOWN, buff=1)
        self.play(Write(thanks_text))
        self.wait(3)

    def create_pie_chart(self, slices, colors):
        wedges = VGroup()
        start_angle = 0
        for i, (slice, color) in enumerate(zip(slices, colors)):
            angle = 360 * slice
            wedge = AnnularSector(
                inner_radius=0.5,
                outer_radius=2,
                angle=angle * DEGREES,
                start_angle=start_angle * DEGREES,
                fill_opacity=1,
                color=color
            )
            wedges.add(wedge)
            start_angle += angle
        return wedges