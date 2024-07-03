from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Introducing Claude by Anthropic", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Description
        description = Text(
            "Claude is designed with a strong emphasis on safety and ethical considerations.", 
            font_size=28
        ).next_to(title, DOWN, buff=0.5)
        
        thoughtful_student_text = Text(
            "Imagine Claude as a thoughtful and cautious student who always thinks twice before speaking,", 
            font_size=28
        ).next_to(description, DOWN, buff=0.3)
        
        accurate_words_text = Text(
            "ensuring that their words are both accurate and considerate.",
            font_size=28
        ).next_to(thoughtful_student_text, DOWN, buff=0.3)

        self.play(Write(description))
        self.wait(2)
        self.play(Write(thoughtful_student_text))
        self.wait(2)
        self.play(Write(accurate_words_text))
        self.wait(2)

        # Diagram
        diagram_title = Text("Claude's Architecture", font_size=36, color=BLUE).to_edge(UP)
        self.play(FadeIn(diagram_title))
        self.wait(1)

        # Building the Diagram
        input_node = Circle(radius=0.5, color=YELLOW).shift(LEFT*3)
        input_label = Text("Input", font_size=24).next_to(input_node, DOWN)

        monitoring_node = Rectangle(width=3, height=1.5, color=GREEN).shift(UP*1)
        monitoring_label = Text("Monitoring", font_size=24).move_to(monitoring_node.get_center())

        controlling_node = Rectangle(width=3, height=1.5, color=GREEN).shift(DOWN*1)
        controlling_label = Text("Controlling", font_size=24).move_to(controlling_node.get_center())

        output_node = Circle(radius=0.5, color=YELLOW).shift(RIGHT*3)
        output_label = Text("Output", font_size=24).next_to(output_node, DOWN)

        arrows = VGroup(
            Arrow(input_node.get_right(), monitoring_node.get_left(), color=RED),
            Arrow(monitoring_node.get_right(), controlling_node.get_left(), buff=0.2, color=RED),
            Arrow(controlling_node.get_right(), output_node.get_left(), color=RED)
        )

        # Adding Diagram to Scene
        self.play(
            DrawBorderThenFill(input_node), Write(input_label),
            DrawBorderThenFill(monitoring_node), Write(monitoring_label),
            DrawBorderThenFill(controlling_node), Write(controlling_label),
            DrawBorderThenFill(output_node), Write(output_label),
            *[Write(arrow) for arrow in arrows]
        )
        self.wait(2)

        safety_text = Text(
            "Mechanisms for monitoring and controlling outputs to prevent harmful or biased responses.",
            font_size=28
        ).next_to(diagram_title, DOWN, buff=1)
        self.play(Write(safety_text))
        self.wait(2)

        suited_text = Text(
            "Claude is well-suited for applications where safety is paramount.",
            font_size=28
        ).next_to(safety_text, DOWN, buff=0.5)
        self.play(Write(suited_text))
        self.wait(2)

        # End Scene
        thanks_text = Text("Thank you for learning about Claude!", font_size=36).to_edge(DOWN)
        self.play(Write(thanks_text))
        self.wait(3)