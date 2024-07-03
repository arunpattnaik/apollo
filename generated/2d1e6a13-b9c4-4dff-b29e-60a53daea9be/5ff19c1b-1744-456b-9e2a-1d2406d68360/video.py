from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Why Investing in Stocks Can Be Rewarding", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Potential for Growth and Income
        growth_income_text = Text("Potential for Growth and Income", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(growth_income_text))
        self.wait(1)

        # Graph of Stock Price Rising
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": BLUE}
        ).shift(DOWN*0.5)

        labels_x = Text("Time (Years)").next_to(axes.x_axis, RIGHT)
        labels_y = Text("Stock Price ($)").next_to(axes.y_axis, UP)
        graph = axes.plot(lambda x: 0.5 * x ** 2, color=GREEN)

        # Points highlighting buy low and sell high
        buy_point = Dot(axes.coords_to_point(1.5, 1.5**2 * 0.5), color=YELLOW).scale(1.2)
        sell_point = Dot(axes.coords_to_point(8, 8**2 * 0.5), color=RED).scale(1.2)

        buy_label = Text("Buy Low", font_size=24, color=YELLOW).next_to(buy_point, DOWN)
        sell_label = Text("Sell High", font_size=24, color=RED).next_to(sell_point, UP)

        self.play(Create(axes), Write(labels_x), Write(labels_y))
        self.play(Create(graph))
        self.play(FadeIn(buy_point), FadeIn(sell_point), Write(buy_label), Write(sell_label))
        self.wait(1)

        # Stock Price Increase Example
        price_increase_text = Text("Stock Price Increases Over Time", font_size=28).next_to(graph, LEFT, buff=0.5)
        self.play(Write(price_increase_text))
        self.wait(1)

        # Dividends Explanation
        dividends_text = Text("Some Companies Pay Dividends", font_size=32).next_to(growth_income_text, DOWN, buff=0.5)
        self.play(Write(dividends_text))
        self.wait(1)

        # Dividends Visualization
        coin = Circle(radius=0.2, color=GOLD, fill_opacity=1).next_to(dividends_text, DOWN, buff=0.5)
        dollar_sign = Text("$", font_size=24, color=WHITE).move_to(coin.get_center())
        dividend_icon = VGroup(coin, dollar_sign)
        dividend_text = Text("Steady Income Stream", font_size=28).next_to(dividend_icon, RIGHT, buff=0.5)

        self.play(FadeIn(dividend_icon), Write(dividend_text))
        self.wait(1)

        # End Scene
        end_text = Text("Investing Can Be Rewarding!", font_size=36, color=GREEN).next_to(dividend_text, DOWN, buff=1)
        self.play(Write(end_text))
        self.wait(2)