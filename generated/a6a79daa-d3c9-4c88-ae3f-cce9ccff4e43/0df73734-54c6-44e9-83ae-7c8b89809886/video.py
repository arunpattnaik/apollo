from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("The Culture and Excitement of the NBA", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Highlights
        highlights_text = Text("Memorable Moments in NBA History", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(highlights_text))
        self.wait(1)

        # Elements representing highlights
        highlight1 = Text("Buzzer-Beaters", font_size=28, color=YELLOW).shift(UP)
        highlight2 = Text("Slam Dunks", font_size=28, color=RED).next_to(highlight1, DOWN, buff=0.5)
        self.play(Write(highlight1))
        self.play(Write(highlight2))
        self.wait(2)
        
        # Beyond the highlights
        beyond_text = Text("Beyond the Highlights", font_size=32).next_to(highlight2, DOWN, buff=1)
        self.play(Write(beyond_text))
        self.wait(1)
        
        # Sportsmanship, teamwork, and community involvement
        sportsmanship_text = Text("Sportsmanship", font_size=28, color=GREEN).shift(LEFT*2)
        teamwork_text = Text("Teamwork", font_size=28, color=BLUE).next_to(sportsmanship_text, RIGHT, buff=1)
        community_text = Text("Community Involvement", font_size=28, color=PURPLE).next_to(sportsmanship_text, DOWN, buff=1.5)
        self.play(Write(sportsmanship_text))
        self.play(Write(teamwork_text))
        self.play(Write(community_text))
        self.wait(2)
        
        # Player impact off the court
        player_impact_text = Text("Players making a positive impact", font_size=28).next_to(beyond_text, DOWN, buff=1)
        self.play(Write(player_impact_text))
        self.wait(1)
        
        # Conclusion
        conclusion_text = Text("NBA Basketball offers something for everyone!", font_size=30).next_to(player_impact_text, DOWN, buff=1)
        self.play(Write(conclusion_text))
        self.wait(2)
        
        # Final message
        final_message = Text("Keep that enthusiasm alive, and maybe one day, you'll make unforgettable plays!", font_size=24).next_to(conclusion_text, DOWN, buff=1)
        self.play(Write(final_message))
        self.wait(3)