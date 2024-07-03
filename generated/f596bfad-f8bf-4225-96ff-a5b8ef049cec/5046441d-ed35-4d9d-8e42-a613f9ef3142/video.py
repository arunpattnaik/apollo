from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Neural Network for Recognizing Handwritten Digits", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # MNIST Sample Images
        mnist_text = Text("Sample images from the MNIST dataset", font_size=30).next_to(title, DOWN, buff=0.5)
        self.play(Write(mnist_text))
        self.wait(1)

        mnist_images = self.create_mnist_images().next_to(mnist_text, DOWN, buff=0.5)
        self.play(FadeIn(mnist_images))
        self.wait(3)

        # Feeding images into Neural Network
        feeding_text = Text("Feeding images into our neural network", font_size=32).next_to(mnist_images, DOWN, buff=0.5)
        self.play(Write(feeding_text))
        self.wait(2)

        # Neural Network Layers
        layers_text = Text("Processed through multiple layers", font_size=32).next_to(feeding_text, DOWN, buff=0.5)
        self.play(Write(layers_text))
        self.wait(2)

        layers_image = self.create_neural_network_layers().next_to(layers_text, DOWN, buff=0.5)
        self.play(FadeIn(layers_image))
        self.wait(2)

        # Outcome
        outcome_text = Text("Network accurately identifies the digits", font_size=32).next_to(layers_image, DOWN, buff=0.5)
        self.play(Write(outcome_text))
        self.wait(2)

        # Final message
        final_text_part1 = Text("This is just one example of how neural networks", font_size=36).shift(DOWN*1)
        final_text_part2 = Text("can be applied to solve real-world problems.", font_size=36).next_to(final_text_part1, DOWN)
        final_text_part3 = Text("Keep exploring to discover more amazing applications.", font_size=36).next_to(final_text_part2, DOWN, buff=0.5)
        final_text_part4 = Text("See you next time!", font_size=36, color=GREEN).next_to(final_text_part3, DOWN)

        self.play(Write(final_text_part1))
        self.play(Write(final_text_part2))
        self.wait(1)
        self.play(Write(final_text_part3))
        self.wait(1)
        self.play(Write(final_text_part4))
        self.wait(3)

    def create_mnist_images(self):
        """Creates a VGroup of sample MNIST images."""
        mnist_images = VGroup()
        for i in range(3):  # 3 rows
            for j in range(3):  # 3 columns
                rect = Square(side_length=1.2).move_to(RIGHT * (j - 1) + DOWN * (i - 1))
                number = Text(str((i * 3 + j) % 10), font_size=36).move_to(rect)
                mnist_images.add(rect, number)
        return mnist_images

    def create_neural_network_layers(self):
        """Creates a simple diagram of a neural network with multiple layers"""
        layers = VGroup()
        input_layer = Circle(radius=0.5, color=WHITE, fill_opacity=1).shift(LEFT * 4)
        hidden_layer_1 = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).next_to(input_layer, RIGHT, buff=1.5)
        hidden_layer_2 = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).next_to(hidden_layer_1, RIGHT, buff=1.5)
        output_layer = Circle(radius=0.5, color=GREEN, fill_opacity=1).next_to(hidden_layer_2, RIGHT, buff=1.5)

        layers.add(input_layer, hidden_layer_1, hidden_layer_2, output_layer)
        for i in range(4):
            line = Line(input_layer.get_center(), hidden_layer_1.get_center(), color=WHITE).shift(UP * (i - 1.5) * 0.5)
            self.play(Write(line))
            layers.add(line)
            line = Line(hidden_layer_1.get_center(), hidden_layer_2.get_center(), color=WHITE).shift(UP * (i - 1.5) * 0.5)
            self.play(Write(line))
            layers.add(line)
            line = Line(hidden_layer_2.get_center(), output_layer.get_center(), color=WHITE).shift(UP * (i - 1.5) * 0.5)
            self.play(Write(line))
            layers.add(line)

        return layers
