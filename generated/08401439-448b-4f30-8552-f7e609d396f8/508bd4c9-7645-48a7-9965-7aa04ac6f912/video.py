from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Impact of Elon Musk's Tweets", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # First tweet
        tweet1_text = Text("Elon Musk's Tweet: 'Tesla stock price is too high imo.'", font_size=30).to_edge(UP, buff=1.5)
        tweet1_image = self.create_tweet("Tesla stock price is too high imo.").scale(0.8).next_to(tweet1_text, DOWN)
        effect1_text = Text("Effect: Tesla stock price dropped significantly.", font_size=30).next_to(tweet1_image, DOWN, buff=0.5)
        
        self.play(Write(tweet1_text))
        self.play(FadeIn(tweet1_image))
        self.wait(1)
        self.play(Write(effect1_text))
        self.wait(2)

        # Second tweet
        tweet2_text = Text("Elon Musk's Tweet: 'Am considering taking Tesla private at $420. Funding secured.'", font_size=25).to_edge(UP, buff=1.5)
        tweet2_image = self.create_tweet("Am considering taking Tesla private at $420. Funding secured.").scale(0.8).next_to(tweet2_text, DOWN)
        effect2_text = Text("Effect: Led to confusion and an SEC investigation.", font_size=30).next_to(tweet2_image, DOWN, buff=0.5)
        
        self.play(FadeOut(tweet1_text), FadeOut(tweet1_image), FadeOut(effect1_text))
        self.play(Write(tweet2_text))
        self.play(FadeIn(tweet2_image))
        self.wait(1)
        self.play(Write(effect2_text))
        self.wait(2)

        # Conclusion
        conclusion_text = Text("These examples show how powerful and unpredictable Elon's tweets can be.", font_size=30).to_edge(DOWN)
        self.play(Write(conclusion_text))
        self.wait(2)

        self.play(FadeOut(conclusion_text))
        caution_text = Text("While his tweets can be exciting, they can also have serious consequences.", font_size=30).to_edge(DOWN)
        self.play(Write(caution_text))
        self.wait(3)

    def create_tweet(self, message):
        tweet_box = Rectangle(width=12, height=2, color=BLUE)
        tweet_text = Text(message, font_size=20).move_to(tweet_box.get_center())
        tweet = VGroup(tweet_box, tweet_text)
        return tweet