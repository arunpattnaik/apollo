from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Elon Musk's Relationship with Twitter", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Main Idea
        main_text = Text("A Perfect Example of Social Media Usage", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(main_text))
        self.wait(1)

        # Collage of Tweets
        collage = self.create_collage_of_tweets().scale(0.5).next_to(main_text, DOWN, buff=0.5)
        self.play(FadeIn(collage))
        self.wait(2)

        # Explanation
        explain_text = VGroup(
            Text("His tweets can inspire,", font_size=32),
            Text("inform, and even disrupt markets.", font_size=32)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(collage, DOWN, buff=0.5)
        self.play(Write(explain_text))
        self.wait(2)

        # Responsibility
        responsibility_text = Text("Remember the power of words and the responsibility that comes with it.", font_size=28).next_to(explain_text, DOWN, buff=0.75)
        self.play(Write(responsibility_text))
        self.wait(2)

        # End Scene
        thanks_text = Text("Thank you for joining me today,\nand I hope you found this exploration fascinating!", font_size=32).next_to(responsibility_text, DOWN, buff=0.75)
        self.play(Write(thanks_text))
        self.wait(3)

    def create_collage_of_tweets(self):
        # Simulating a collage of Elon Musk's tweets with sample text representations
        tweet1 = self.create_tweet_box("Will own no house.", "53.2K Likes")
        tweet2 = self.create_tweet_box("Tesla stock price is too high imo", "74.5K Likes")
        tweet3 = self.create_tweet_box("Dogecoin is the people's crypto", "385.6K Likes")
        tweet4 = self.create_tweet_box("One word: Doge", "264.3K Likes")

        tweets = VGroup(tweet1, tweet2, tweet3, tweet4).arrange_in_grid(rows=2, buff=0.5)
        collage = Rectangle(width=10, height=5.5, color=WHITE).surround(tweets)
        
        return VGroup(tweets, collage)
    
    def create_tweet_box(self, tweet_content, tweet_likes):
        tweet_box = VGroup(
            Text(tweet_content, font_size=20),
            Text(f"{tweet_likes}", font_size=18, color=YELLOW).next_to(ORIGIN, DOWN, aligned_edge=RIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        box_around = Rectangle(width=5, height=2.5, color=BLUE).surround(tweet_box)
        return VGroup(tweet_box, box_around)