from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Neural Networks: Inspired by the Human Brain", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Draw neural network description
        input_nodes = self.create_layer(3, UP*1.5, "Input Layer")
        hidden_nodes = self.create_layer(4, ORIGIN, "Hidden Layer")
        output_nodes = self.create_layer(2, DOWN*1.5, "Output Layer")

        self.connect_layers(input_nodes, hidden_nodes)
        self.connect_layers(hidden_nodes, output_nodes)

        # Wait to show connections
        self.wait(2)

        # Explanation of connections and weights
        weight_text = Text("Each connection has a weight", font_size=24).next_to(output_nodes, RIGHT, buff=1)
        self.play(Write(weight_text))
        self.wait(1)

        # Highlighting weight adjustment process
        adjustment_text = Text("Weights adjust as the network learns", font_size=24).next_to(weight_text, DOWN, buff=0.5)
        self.play(Write(adjustment_text))
        self.wait(2)

        # End Scene
        conclusion_text = Text("The more it learns, the better it gets at understanding and generating language", font_size=28).to_edge(DOWN)
        self.play(Write(conclusion_text))
        self.wait(3)

    def create_layer(self, num_nodes, position, label_text):
        nodes = VGroup()
        for i in range(num_nodes):
            node = Dot(radius=0.15, color=BLUE)
            node.move_to(position + RIGHT * i * 1.5)
            nodes.add(node)
        
        label = Text(label_text, font_size=20).next_to(nodes, LEFT, buff=0.5)
        self.play(FadeIn(nodes), Write(label))
        self.wait(0.5)

        return nodes

    def connect_layers(self, layer1, layer2):
        for node1 in layer1:
            for node2 in layer2:
                connection = Line(node1.get_center(), node2.get_center(), color=GREY)
                self.play(Create(connection), run_time=0.5)
        self.wait(1)
