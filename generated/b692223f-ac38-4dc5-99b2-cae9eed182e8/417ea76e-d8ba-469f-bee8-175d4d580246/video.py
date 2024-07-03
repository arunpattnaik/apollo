from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("How Neural Networks Learn", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to training
        intro_text = Text("This process is called 'training.'", font_size=36).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)
        
        # Illustrating flow of text data
        dataset_text = Text("Imagine we have a huge dataset of text,", font_size=32).next_to(intro_text, DOWN, buff=0.5)
        library_text = Text("like all the books in a library.", font_size=32).next_to(dataset_text, DOWN, buff=0.3)
        self.play(Write(dataset_text))
        self.play(Write(library_text))
        self.wait(2)

        # Flow of text data into neural network
        flow_text = Text("We feed this text into the neural network,", font_size=32).shift(UP*0.5)
        self.play(Write(flow_text))
        self.wait(1)

        # Visualizing the neural network
        neural_network = self.create_neural_network().scale(0.8).shift(DOWN*0.5)
        self.play(FadeIn(neural_network))
        self.wait(2)

        # Backpropagation
        backpropagation_text = Text("The network adjusts its weights to minimize errors", font_size=32).next_to(flow_text, DOWN, buff=0.5)
        backpropagation_text2 = Text("a process called 'backpropagation.'", font_size=32).next_to(backpropagation_text, DOWN, buff=0.3)
        self.play(Write(backpropagation_text))
        self.play(Write(backpropagation_text2))
        self.wait(2)

        # Final notes
        final_notes = Text("Over time, it gets really good at predicting the next word,", font_size=32).next_to(backpropagation_text2, DOWN, buff=0.5)
        final_notes2 = Text("or even generating entire paragraphs that make sense.", font_size=32).next_to(final_notes, DOWN, buff=0.3)
        self.play(Write(final_notes))
        self.play(Write(final_notes2))
        self.wait(3)

        # End Scene
        self.play(FadeOut(title), FadeOut(intro_text), FadeOut(dataset_text), FadeOut(library_text), 
                  FadeOut(flow_text), FadeOut(backpropagation_text), FadeOut(backpropagation_text2), FadeOut(final_notes), 
                  FadeOut(final_notes2), FadeOut(neural_network))
        self.wait(1)

    def create_neural_network(self):
        network = VGroup()

        # Layers of network
        input_layer = VGroup(*[Dot(color=BLUE) for _ in range(5)]).arrange(DOWN, buff=0.5)
        hidden_layer_1 = VGroup(*[Dot(color=GREEN) for _ in range(4)]).arrange(DOWN, buff=0.5).shift(RIGHT*2)
        hidden_layer_2 = VGroup(*[Dot(color=GREEN) for _ in range(4)]).arrange(DOWN, buff=0.5).shift(RIGHT*4)
        output_layer = VGroup(*[Dot(color=RED) for _ in range(3)]).arrange(DOWN, buff=0.5).shift(RIGHT*6)

        layers = [input_layer, hidden_layer_1, hidden_layer_2, output_layer]
        
        # Adding connections between layers
        for l1, l2 in zip(layers[:-1], layers[1:]):
            for dot1 in l1:
                for dot2 in l2:
                    network.add(Line(dot1.get_center(), dot2.get_center(), color=GRAY))

        network.add(*input_layer, *hidden_layer_1, *hidden_layer_2, *output_layer)
        return network