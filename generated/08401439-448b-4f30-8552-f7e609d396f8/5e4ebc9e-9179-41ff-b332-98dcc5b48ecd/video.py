from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Elon Musk's Tweets and Their Impact on Markets", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        intro_text = Text("Elon Musk's tweets can significantly impact the stock market and public opinion.", font_size=28).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Example of Tesla stock price fluctuation
        tesla_text = Text("Effect on Tesla's Stock Price", font_size=32, color=RED).next_to(intro_text, DOWN, buff=1)
        self.play(Write(tesla_text))
        self.wait(1)

        # Creating the graph for Tesla's stock price
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[600, 800, 20],
            axis_config={"color": WHITE}
        ).scale(0.8).shift(DOWN)

        x_label = Text("Time", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Stock Price", font_size=24).next_to(axes.y_axis, UP)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        stock_prices = [650, 670, 700, 670, 710, 730, 720, 750, 740, 760]
        points = [axes.c2p(x, y) for x, y in enumerate(stock_prices)]
        graph = VGroup(*[Dot(point, color=YELLOW) for point in points])

        for i in range(len(points) - 1):
            self.play(Create(Line(points[i], points[i + 1], color=BLUE)), run_time=0.5)
        
        self.play(Create(graph))
        self.wait(1)

        tweet_point = points[3]
        tweet_arrow = Arrow(start=tweet_point + UP*1, end=tweet_point, buff=0.1, color=YELLOW)
        tweet_label = Text("Elon's Tweet", font_size=24, color=YELLOW).next_to(tweet_arrow, UP)

        self.play(Create(tweet_arrow), Write(tweet_label))
        self.wait(2)

        conclusion_text = Text("Investors and the public pay close attention to his tweets.", font_size=28).next_to(tesla_text, DOWN, buff=0.5)
        self.play(Write(conclusion_text))
        self.wait(2)

        # Influence on cryptocurrencies
        crypto_text = Text("Influence on Cryptocurrencies", font_size=32, color=GREEN).next_to(conclusion_text, DOWN, buff=1.5)
        self.play(Write(crypto_text))
        self.wait(1)

        bitcoin_text = Text("Bitcoin", font_size=28, color=ORANGE).next_to(crypto_text, DOWN, buff=0.5).shift(LEFT*3)
        dogecoin_text = Text("Dogecoin", font_size=28, color=WHITE).next_to(crypto_text, DOWN, buff=0.5).shift(RIGHT*3)

        self.play(Write(bitcoin_text), Write(dogecoin_text))
        self.wait(2)

        # Concluding remarks
        concluding_remarks = Text(
            "Elon's power to influence markets\nwith just a few words is fascinating and controversial.",
            font_size=28, line_spacing=1
        ).next_to(crypto_text, DOWN, buff=1.5)
        self.play(Write(concluding_remarks))
        self.wait(2)

        thanks_text = Text("Thank you for watching!", font_size=36).next_to(concluding_remarks, DOWN, buff=1.5).to_edge(DOWN)
        self.play(Write(thanks_text))
        self.wait(3)