from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Training a Neural Network", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Backpropagation Explanation
        explanation = Text(
            "Training a neural network is like teaching it to recognize patterns.", 
            font_size=36
        ).next_to(title, DOWN, buff=0.5)
        backprop_text = Text(
            "We use a process called backpropagation.",
            font_size=36
        ).next_to(explanation, DOWN, buff=0.3)
        self.play(Write(explanation))
        self.play(Write(backprop_text))
        self.wait(2)
        
        # Image of a cat
        cat_image = self.create_cat_image().scale(0.5).shift(LEFT*3 + UP*0.5)
        self.play(FadeIn(cat_image))
        self.wait(1)

        # Neural Network Visualization
        neural_network = self.create_neural_network().scale(0.8).next_to(cat_image, RIGHT, buff=1)
        self.play(FadeIn(neural_network))
        self.wait(1)

        # Initial guess
        initial_guess_text = Text("Initial Guess", font_size=24, color=RED).next_to(neural_network, DOWN, buff=0.5)
        self.play(Write(initial_guess_text))
        self.wait(1)

        # Error Calculation
        error_calculation_text = Text("Error Calculation", font_size=24).next_to(initial_guess_text, DOWN, buff=0.3)
        self.play(Write(error_calculation_text))
        self.wait(1)

        # Backpropagation Visualization
        error_message = Text("Error", font_size=24, color=RED).move_to(neural_network.get_center()).shift(UP*1)
        self.play(FadeIn(error_message))
        self.wait(1)
        self.play(error_message.animate().move_to(cat_image.get_center() + DOWN*1))

        adjusting_weights_text = Text("Adjusting Weights", font_size=24, color=GREEN).move_to(neural_network.get_center()).shift(DOWN*1)
        self.play(FadeIn(adjusting_weights_text))
        self.wait(1)
        self.play(FadeOut(error_message), FadeOut(adjusting_weights_text))
        self.wait(1)

        # Process Repeats
        process_repeats_text = Text(
            "This process repeats many times with different images,",
            font_size=24
        ).next_to(neural_network, DOWN, buff=1)
        reducing_error_text = Text(
            "gradually reducing the error.",
            font_size=24
        ).next_to(process_repeats_text, DOWN, buff=0.3)
        self.play(Write(process_repeats_text))
        self.play(Write(reducing_error_text))
        self.wait(2)

        # Closing Statement
        closing_text = Text(
            "It's like practicing a skill over and over until you get it right.",
            font_size=28
        ).next_to(reducing_error_text, DOWN, buff=1)
        activation_functions_intro = Text(
            "Let's move on to activation functions, which help neurons decide when to activate.",
            font_size=28
        ).next_to(closing_text, DOWN, buff=0.3)
        self.play(Write(closing_text))
        self.play(Write(activation_functions_intro))
        self.wait(3)

    def create_cat_image(self):
        cat_body = Circle(radius=1, color=ORANGE, fill_opacity=1).shift(DOWN*0.5)
        left_ear = Polygon(
            [0.5, 1.5, 0], [0, 2.5, 0], [-0.5, 1.5, 0], color=ORANGE, fill_opacity=1
        ).shift(LEFT*0.5)
        right_ear = Polygon(
            [0.5, 1.5, 0], [0, 2.5, 0], [-0.5, 1.5, 0], color=ORANGE, fill_opacity=1
        ).shift(RIGHT*0.5)
        cat = VGroup(cat_body, left_ear, right_ear)
        cat.set_stroke(color=BLACK, width=2)
        return cat
    
    def create_neural_network(self):
        layer1 = VGroup(*[Dot(radius=0.2) for _ in range(3)]).arrange(DOWN, buff=0.4)
        layer2 = VGroup(*[Dot(radius=0.2) for _ in range(4)]).arrange(DOWN, buff=0.4).next_to(layer1, RIGHT, buff=0.8)
        layer3 = VGroup(*[Dot(radius=0.2) for _ in range(3)]).arrange(DOWN, buff=0.4).next_to(layer2, RIGHT, buff=0.8)

        connections = VGroup()
        for dot1 in layer1:
            for dot2 in layer2:
                connections.add(Line(dot1.get_center(), dot2.get_center(), color=BLUE))
        for dot2 in layer2:
            for dot3 in layer3:
                connections.add(Line(dot2.get_center(), dot3.get_center(), color=BLUE))
        
        neural_network = VGroup(layer1, layer2, layer3, connections)
        return neural_network