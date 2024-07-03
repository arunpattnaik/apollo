from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Exploring Large Language Models", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text(
            "Imagine a machine that can understand and generate human language, "
            "almost like having a conversation with a friend. That's what large "
            "language models are all about.",
            font_size=28
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text, run_time=5))
        self.wait(1)

        # Description text
        desc_text = Text(
            "On the screen, you can see a simple diagram of a neural network, which is the backbone of these models. "
            "Let's start by understanding what a neural network is and how it works.",
            font_size=28
        ).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(desc_text, run_time=5))
        self.wait(1)

        # Neural network diagram
        nn_diagram = self.create_neural_network()
        nn_diagram.to_edge(DOWN)
        self.play(Create(nn_diagram))
        self.wait(2)

    def create_neural_network(self):
        # Function to create a simple neural network diagram
        layer_1 = self.create_layer(3, [-4, 0, 0])
        layer_2 = self.create_layer(5, [0, 0, 0])
        layer_3 = self.create_layer(4, [4, 0, 0])

        # Connect neurons with lines
        connections = VGroup()
        for neuron1 in layer_1:
            for neuron2 in layer_2:
                connections.add(Line(neuron1.get_center(), neuron2.get_center()))
        for neuron2 in layer_2:
            for neuron3 in layer_3:
                connections.add(Line(neuron2.get_center(), neuron3.get_center()))

        return VGroup(layer_1, layer_2, layer_3, connections)

    def create_layer(self, num_neurons, position):
        neurons = VGroup()
        for i in range(num_neurons):
            neuron = Circle(radius=0.2, color=WHITE, fill_opacity=1).shift(UP * i * 1.5)
            neurons.add(neuron)
        neurons.move_to(position)
        return neurons