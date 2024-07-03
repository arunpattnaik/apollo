from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Twitter: A Social Media Platform", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)

        # Description text
        description_text = Text(
            "Twitter is a platform where users post short messages called tweets.",
            font_size=28
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(description_text))
        self.wait(2)

        # Show Twitter feed
        twitter_feed = self.create_twitter_feed().scale(0.7).shift(DOWN*0.5)
        self.play(FadeIn(twitter_feed))
        self.wait(1.5)

        # Highlight tweets
        elon_tweet = self.create_tweet("Elon Musk", "Great news! We're launching a new product next week. Stay tuned!", GREEN).scale(0.7).shift(UP*1.5)
        news_tweet = self.create_tweet("News Outlet", "Breaking: New advancements in AI technology.", BLUE).scale(0.7).shift(DOWN*0.5)
        joke_tweet = self.create_tweet("Funny Person", "Why don't scientists trust atoms? Because they make up everything!", YELLOW).scale(0.7).next_to(news_tweet, DOWN, buff=0.5)

        self.play(FadeIn(elon_tweet), FadeIn(news_tweet), FadeIn(joke_tweet))
        self.wait(3)

        # Elon Musk's impact
        elon_musk_text = Text(
            "Elon Musk uses Twitter to share updates and make announcements.",
            font_size=28
        ).next_to(twitter_feed, DOWN, buff=0.5)
        self.play(Write(elon_musk_text))
        self.wait(3)

        # Power of direct communication
        communication_text = Text(
            "This allows him to reach millions instantly.",
            font_size=28,
            color=RED
        ).next_to(elon_musk_text, DOWN, buff=0.5)
        self.play(Write(communication_text))
        self.wait(3)

        # End scene
        self.play(FadeOut(title), FadeOut(description_text), FadeOut(twitter_feed), 
                  FadeOut(elon_tweet), FadeOut(news_tweet), FadeOut(joke_tweet), 
                  FadeOut(elon_musk_text), FadeOut(communication_text))
        self.wait(1)

    def create_twitter_feed(self):
        feed = VGroup()

        feed_outline = Rectangle(width=8, height=5, color=WHITE)
        feed.add(feed_outline)
        
        for i in range(5):
            tweet_bg = Rectangle(width=7.5, height=0.8, color=BLUE, fill_opacity=0.1).shift(UP*(2-i))
            feed.add(tweet_bg)

        return feed

    def create_tweet(self, user, content, color):
        tweet = VGroup()

        user_text = Text(user, font_size=24, color=color).to_edge(LEFT)
        content_text = Text(content, font_size=20).next_to(user_text, DOWN, aligned_edge=LEFT).shift(DOWN*0.1)
        
        tweet.add(user_text, content_text)
        return tweet