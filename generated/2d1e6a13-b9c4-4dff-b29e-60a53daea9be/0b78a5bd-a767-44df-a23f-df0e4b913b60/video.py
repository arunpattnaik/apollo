from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Investing in Stocks", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text(
            "Have you ever wondered how people make money\nin the stock market or felt overwhelmed by\nwhere to begin?", 
            font_size=28, line_spacing=0.8
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Transition text
        transition_text = Text(
            "Let's break it down to understand what stocks are,\n"
            "why you might want to invest in them, and how to get started.", 
            font_size=28, line_spacing=0.8
        ).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(transition_text))
        self.wait(2)

        # Stock exchange visualization prompt
        stock_exchange_title = Text("Imagine a bustling stock exchange floor...", font_size=30, color=YELLOW)
        stock_exchange_title.to_edge(DOWN)
        self.play(Write(stock_exchange_title))
        self.wait(1)

        self.play(FadeOut(stock_exchange_title))
        self.visualize_stock_exchange()
        self.wait(3)

    def visualize_stock_exchange(self):
        # Floor backdrop
        floor = Rectangle(width=14, height=8, color=BLUE, fill_opacity=0.3).move_to([0, 0, 0])
        self.play(FadeIn(floor))

        # Adding numbers and charts
        for _ in range(5):
            for _ in range(5):
                number = Text(f"{np.random.uniform(100, 1000):.2f}", font_size=24, color=YELLOW)
                number.move_to(np.random.uniform(low=[-6, -3, 0], high=[6, 3, 0]))
                self.add(number)
        
        chart = self.create_chart()
        chart.scale(0.5).shift(DOWN * 1.5 + RIGHT * 2)
        self.play(DrawBorderThenFill(chart))

    def create_chart(self):
        chart_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_numbers": False}
        )

        x_vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        y_vals = [1, 3, 2.5, 6, 4.5, 5.5, 7, 6.5, 8, 9]

        graph = chart_axes.plot_line_graph(
            x_values=x_vals,
            y_values=y_vals,
            add_vertex_dots=True,
        )

        return VGroup(chart_axes, graph)