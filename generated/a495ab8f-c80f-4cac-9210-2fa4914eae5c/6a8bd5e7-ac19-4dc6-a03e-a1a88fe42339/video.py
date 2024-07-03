from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Groq: The Tensor Streaming Processor (TSP)", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Introduction to the TSP
        tsp_intro = Text(
            "Groq's TSP is highly specialized for AI workloads.",
            font_size=36
        ).next_to(title, DOWN, buff=0.5)
        athlete_analogy = Text(
            "Think of it as a highly focused athlete.",
            font_size=36
        ).next_to(tsp_intro, DOWN, buff=0.5)
        self.play(Write(tsp_intro))
        self.wait(1)
        self.play(Write(athlete_analogy))
        self.wait(1)
        
        # Diagram of TSP architecture
        diagram_title = Text("TSP Architecture", font_size=40, color=BLUE).next_to(athlete_analogy, DOWN, buff=0.5)
        self.play(Write(diagram_title))
        self.wait(1)
        
        # Drawing TSP architecture
        diagram = self.create_tsp_diagram().scale(0.7).next_to(diagram_title, DOWN, buff=0.5)
        self.play(FadeIn(diagram))

        # Highlighting low latency and high throughput
        low_latency_highlight = Text("Incredibly Low Latency", font_size=28, color=GREEN).move_to(3 * LEFT + 2 * DOWN)
        high_throughput_highlight = Text("High Throughput", font_size=28, color=YELLOW).move_to(3 * RIGHT + 2 * DOWN)
        self.play(Write(low_latency_highlight), Write(high_throughput_highlight))
        self.wait(2)

        # Real-time AI mention
        real_time_ai_application = Text(
            "Ideal for Real-Time AI Applications!",
            font_size=32,
            color=RED
        ).next_to(diagram, DOWN, buff=1)
        self.play(Write(real_time_ai_application))
        self.wait(2)

    def create_tsp_diagram(self):
        dsp_diagram = VGroup()
        
        # Create main grid of processor units
        rows, cols = 4, 4
        for i in range(rows):
            for j in range(cols):
                unit = Square(side_length=0.5, color=WHITE, fill_color=BLUE, fill_opacity=0.8)
                unit.move_to(np.array([j, -i, 0]) * 0.6)
                dsp_diagram.add(unit)

        # Add stream connections with arrows
        for i in range(rows):
            for j in range(cols):
                if j < cols - 1:
                    arrow_right = Arrow(dsp_diagram[i*cols + j].get_right(), dsp_diagram[i*cols + j + 1].get_left(), buff=0.1, color=GREY)
                    dsp_diagram.add(arrow_right)
                if i < rows - 1:
                    arrow_down = Arrow(dsp_diagram[i*cols + j].get_bottom(), dsp_diagram[(i+1)*cols + j].get_top(), buff=0.1, color=GREY)
                    dsp_diagram.add(arrow_down)

        return dsp_diagram