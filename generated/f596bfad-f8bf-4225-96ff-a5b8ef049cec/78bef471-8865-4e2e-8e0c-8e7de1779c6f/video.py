from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Exploring Neural Networks", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction Text
        intro_text = Text("Imagine you have a brain inside your computer,", font_size=36).shift(UP*2)
        networking_text = Text("capable of learning and making decisions.", font_size=36).next_to(intro_text, DOWN)
        self.play(Write(intro_text), Write(networking_text))
        self.wait(2)

        # Simple neuron visualization
        neuron_title = Text("A Simple Neuron", font_size=36).shift(UP*0.5)
        self.play(Write(neuron_title))
        self.wait(1)

        neuron_diagram = self.create_neuron_diagram().scale(0.75).shift(DOWN*1)
        self.play(FadeIn(neuron_diagram))
        self.wait(2)

        # Transition to working together
        transition_text = Text("Ready to explore how these neurons work together?", font_size=36).to_edge(DOWN)
        self.play(Write(transition_text))
        self.wait(2)

        # End the scene
        self.play(FadeOut(title), FadeOut(intro_text), FadeOut(networking_text), FadeOut(neuron_title), FadeOut(neuron_diagram), FadeOut(transition_text))
        self.wait(1)

    def create_neuron_diagram(self):
        neuron = VGroup()
        
        # Inputs
        inputs = VGroup(*[
            Circle(radius=0.2, color=BLUE).shift(LEFT*3 + UP*i)
            for i in range(-2, 3)
        ])
        input_texts = VGroup(*[
            Text(f"x{i+1}", font_size=24).next_to(inputs[i], LEFT)
            for i in range(5)
        ])
        
        # Neuron
        neuron_circle = Circle(radius=1.0, color=WHITE).shift(RIGHT*1.5)
        neuron_text = Text("Neuron", font_size=24).move_to(neuron_circle.get_center())
        
        # Output
        output = Circle(radius=0.2, color=RED).shift(RIGHT*6)
        output_text = Text("Output", font_size=24).next_to(output, RIGHT)
        
        # Arrows Connecting Inputs to Neuron
        arrows_to_neuron = VGroup(*[
            Arrow(start=inputs[i].get_right(), end=neuron_circle.get_left(), buff=0.1)
            for i in range(5)
        ])

        # Arrow Connecting Neuron to Output
        arrow_to_output = Arrow(start=neuron_circle.get_right(), end=output.get_left(), buff=0.1)
        
        neuron.add(inputs, input_texts, neuron_circle, neuron_text, output, output_text, arrows_to_neuron, arrow_to_output)
        return neuron
        