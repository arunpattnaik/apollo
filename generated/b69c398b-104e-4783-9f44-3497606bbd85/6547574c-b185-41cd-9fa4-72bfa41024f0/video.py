from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("OpenAI's GPT: An Overview", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text("Generative Pre-trained Transformer (GPT)", font_size=36).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # GPT-3 Text
        gpt3_text = Text("GPT-3: The Most Well-Known Iteration", font_size=32).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(gpt3_text))
        self.wait(2)

        # Library metaphor text
        library_text = Text("Imagine a vast library with books on every subject.", font_size=28).next_to(gpt3_text, DOWN, buff=1)
        self.play(Write(library_text))
        self.wait(2)

        # Neural network visualization
        nn_title = Text("Neural Network of GPT-3", font_size=36, color=YELLOW).to_edge(LEFT).shift(DOWN*1.5)
        self.play(Write(nn_title))
        self.wait(1)

        # Neural network diagram
        nn_diagram = self.create_nn_diagram().next_to(nn_title, RIGHT, buff=1)
        self.play(Write(nn_diagram))
        self.wait(2)

        # How it generates text
        generation_text = Text("GPT-3 generates human-like text based on learned patterns.", font_size=28).to_edge(DOWN)
        self.play(Write(generation_text))
        self.wait(2)

        # End Scene
        final_text = Text("It's like having a conversation with someone who has an encyclopedic knowledge of the world!", font_size=32).next_to(library_text, DOWN, buff=1.5)
        self.play(Write(final_text))
        self.wait(3)

    def create_nn_diagram(self):
        # Neural network layers
        layers = VGroup()
        input_layer = VGroup()
        hidden_layer1 = VGroup()
        hidden_layer2 = VGroup()
        output_layer = VGroup()
        
        # Create nodes for each layer
        for i in range(5):
            input_layer.add(Dot(radius=0.15).shift(UP*i*0.6).set_color(BLUE))
        for i in range(7):
            hidden_layer1.add(Dot(radius=0.15).shift(UP*i*0.6).align_to(input_layer, LEFT).shift(RIGHT*1.5).set_color(RED))
        for i in range(7):
            hidden_layer2.add(Dot(radius=0.15).shift(UP*i*0.6).align_to(hidden_layer1, LEFT).shift(RIGHT*1.5).set_color(RED))
        for i in range(5):
            output_layer.add(Dot(radius=0.15).shift(UP*i*0.6).align_to(hidden_layer2, LEFT).shift(RIGHT*1.5).set_color(GREEN))
        
        # Add connections between nodes
        connections = VGroup()
        for input_node in input_layer:
            for hidden_node1 in hidden_layer1:
                connections.add(Line(input_node.get_center(), hidden_node1.get_center()).set_stroke(width=1))
        for hidden_node1 in hidden_layer1:
            for hidden_node2 in hidden_layer2:
                connections.add(Line(hidden_node1.get_center(), hidden_node2.get_center()).set_stroke(width=1))
        for hidden_node2 in hidden_layer2:
            for output_node in output_layer:
                connections.add(Line(hidden_node2.get_center(), output_node.get_center()).set_stroke(width=1))

        layers.add(input_layer, hidden_layer1, hidden_layer2, output_layer)
        return VGroup(connections, layers).scale(0.5).shift(DOWN*1)