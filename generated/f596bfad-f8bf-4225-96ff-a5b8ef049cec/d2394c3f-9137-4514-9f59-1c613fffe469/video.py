from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Activation Functions in Neural Networks", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text("Activation functions introduce non-linearity, allowing the network to learn complex patterns.", font_size=28).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Common activation functions text
        activation_functions_text = Text("Common Activation Functions:", font_size=32).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(activation_functions_text))
        self.wait(1)

        # Displaying sigmoid, tanh and ReLU
        sigmoid_text = Text("Sigmoid", font_size=28).shift(LEFT*3 + UP)
        tanh_text = Text("tanh", font_size=28).shift(UP)
        relu_text = Text("ReLU", font_size=28).shift(RIGHT*3 + UP)
        
        self.play(Write(sigmoid_text), Write(tanh_text), Write(relu_text))
        self.wait(1)

        # Sigmoid function plot
        sigmoid_axes = Axes(x_range=[-4, 4], y_range=[-0.5, 1.5], x_length=4, y_length=3, axis_config={"color": BLUE}).next_to(sigmoid_text, DOWN)
        sigmoid_graph = sigmoid_axes.plot(lambda x: 1 / (1 + np.exp(-x)), color=YELLOW)
        self.play(Create(sigmoid_axes), Create(sigmoid_graph))
        self.wait(1)

        # Tanh function plot
        tanh_axes = Axes(x_range=[-4, 4], y_range=[-1.5, 1.5], x_length=4, y_length=3, axis_config={"color": BLUE}).next_to(tanh_text, DOWN)
        tanh_graph = tanh_axes.plot(np.tanh, color=YELLOW)
        self.play(Create(tanh_axes), Create(tanh_graph))
        self.wait(1)

        # ReLU function plot
        relu_axes = Axes(x_range=[-4, 4], y_range=[-1, 4], x_length=4, y_length=3, axis_config={"color": BLUE}).next_to(relu_text, DOWN)
        relu_graph = relu_axes.plot(lambda x: np.maximum(0, x), color=YELLOW)
        self.play(Create(relu_axes), Create(relu_graph))
        self.wait(1)

        # Explanation about ReLU
        relu_explanation = Text("ReLU outputs zero for negative inputs, and the input value for positive inputs.", font_size=26).next_to(relu_axes, DOWN, buff=0.5)
        self.play(Write(relu_explanation))
        self.wait(3)

        # Neural Network in action text
        nn_action_text = Text("Let's see a neural network in action with a real-world example!", font_size=32).to_edge(DOWN)
        self.play(Write(nn_action_text))
        self.wait(2)

        # Displaying a simple neural network
        input_layer = Text("Input Layer", font_size=20).shift(LEFT*4 + UP*2)
        hidden_layer = Text("Hidden Layer", font_size=20).next_to(input_layer, DOWN, buff=2)
        output_layer = Text("Output Layer", font_size=20).next_to(hidden_layer, DOWN, buff=2)

        input_nodes = VGroup(*[Circle(radius=0.2, color=BLUE).next_to(input_layer, LEFT, buff=0.5*i) for i in range(1, 6)])
        hidden_nodes = VGroup(*[Circle(radius=0.2, color=GREEN).next_to(hidden_layer, LEFT, buff=0.5*i) for i in range(1, 6)])
        output_nodes = VGroup(*[Circle(radius=0.2, color=RED).next_to(output_layer, LEFT, buff=0.5*i) for i in range(1, 6)])

        self.play(Write(input_layer), Write(hidden_layer), Write(output_layer))
        self.play(Create(input_nodes), Create(hidden_nodes), Create(output_nodes))
        self.wait(2)

        # Highlighting connections
        connections = VGroup(
            *[Line(input_node.get_center(), hidden_node.get_center(), color=WHITE) for input_node in input_nodes for hidden_node in hidden_nodes],
            *[Line(hidden_node.get_center(), output_node.get_center(), color=WHITE) for hidden_node in hidden_nodes for output_node in output_nodes]
        )
        self.play(Create(connections))
        self.wait(2)

        # End scene
        self.play(FadeOut(title), FadeOut(intro_text), FadeOut(activation_functions_text), FadeOut(sigmoid_text),
                  FadeOut(tanh_text), FadeOut(relu_text), FadeOut(sigmoid_axes), FadeOut(sigmoid_graph), FadeOut(tanh_axes),
                  FadeOut(tanh_graph), FadeOut(relu_axes), FadeOut(relu_graph), FadeOut(relu_explanation), 
                  FadeOut(nn_action_text), FadeOut(input_layer), FadeOut(hidden_layer), FadeOut(output_layer),
                  FadeOut(input_nodes), FadeOut(hidden_nodes), FadeOut(output_nodes), FadeOut(connections))