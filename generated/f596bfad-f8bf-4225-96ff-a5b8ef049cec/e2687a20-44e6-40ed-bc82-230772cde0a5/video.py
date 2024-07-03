from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Layers in a Neural Network", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Diagram of Neural Network
        input_layer_text = Text("Input Layer", font_size=24).to_edge(LEFT).shift(UP*2)
        hidden_layer_text = Text("Hidden Layers", font_size=24).next_to(input_layer_text, RIGHT, buff=2.5)
        output_layer_text = Text("Output Layer", font_size=24).to_edge(RIGHT).shift(UP*2)

        self.play(Write(input_layer_text), Write(hidden_layer_text), Write(output_layer_text))
        self.wait(1)

        # Draw Neural Network Layers
        input_neurons = self.create_layer(4, LEFT*4 + DOWN)
        hidden_neurons1 = self.create_layer(5, LEFT*1 + DOWN)
        hidden_neurons2 = self.create_layer(5, RIGHT*2 + DOWN)
        output_neurons = self.create_layer(3, RIGHT*5 + DOWN)

        self.play(FadeIn(input_neurons), FadeIn(hidden_neurons1), FadeIn(hidden_neurons2), FadeIn(output_neurons))
        self.wait(1)

        # Show connections
        self.create_connections(input_neurons, hidden_neurons1)
        self.create_connections(hidden_neurons1, hidden_neurons2)
        self.create_connections(hidden_neurons2, output_neurons)
        
        self.wait(2)

        # Explanation text
        explanation_text = Text(
            "Input Layer receives data, Hidden Layers process the data,\nand Output Layer gives the result.",
            font_size=28
        ).next_to(hidden_layer_text, DOWN, buff=3.5)
        self.play(Write(explanation_text))
        self.wait(2)

        # Weights adjustment
        weights_text = Text("Weights adjust during training", font_size=32, color=BLUE).next_to(explanation_text, DOWN, buff=1)
        self.play(Write(weights_text))

        # Simulate weight adjustment
        self.simulate_weights_adjustment(input_neurons, hidden_neurons1, hidden_neurons2, output_neurons)
        self.wait(2)

    def create_layer(self, num_neurons, position):
        layer = VGroup()
        for i in range(num_neurons):
            neuron = Circle(radius=0.2, color=WHITE, fill_opacity=1)
            neuron.shift(DOWN * i * 0.75 + position)
            layer.add(neuron)
        return layer

    def create_connections(self, layer1, layer2):
        for neuron1 in layer1:
            for neuron2 in layer2:
                connection = Line(neuron1.get_center(), neuron2.get_center(), stroke_width=1)
                self.add(connection)

    def simulate_weights_adjustment(self, input_layer, hidden_layer1, hidden_layer2, output_layer):
        layers = [input_layer, hidden_layer1, hidden_layer2, output_layer]
        for i in range(len(layers) - 1):
            for neuron1 in layers[i]:
                for neuron2 in layers[i+1]:
                    weight = Line(neuron1.get_center(), neuron2.get_center(), stroke_width=2, color=YELLOW)
                    self.play(Create(weight), run_time=0.2)
                    self.remove(weight)