from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Iconic Moments and Players in NBA History", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Highlighting legendary players
        jordan_text = Text("Michael Jordan", font_size=32, color=RED).shift(UP * 1.5)
        lebron_text = Text("LeBron James", font_size=32, color=BLUE).next_to(jordan_text, DOWN, buff=0.5)
        kobe_text = Text("Kobe Bryant", font_size=32, color=PURPLE).next_to(lebron_text, DOWN, buff=0.5)
        
        self.play(Write(jordan_text))
        self.wait(0.5)
        self.play(Write(lebron_text))
        self.wait(0.5)
        self.play(Write(kobe_text))
        self.wait(2)

        # Highlight examples
        jordan_highlight = self.create_highlight_circle(color=RED).scale(0.5).next_to(jordan_text, LEFT, buff=0.5)
        lebron_highlight = self.create_highlight_circle(color=BLUE).scale(0.5).next_to(lebron_text, LEFT, buff=0.5)
        kobe_highlight = self.create_highlight_circle(color=PURPLE).scale(0.5).next_to(kobe_text, LEFT, buff=0.5)
        
        self.play(FadeIn(jordan_highlight), FadeIn(lebron_highlight), FadeIn(kobe_highlight))
        self.wait(2)

        # Inspiration message
        inspiration_text = Text(
            "These athletes inspire millions with their dedication, skill, and sportsmanship.",
            font_size=28
        ).next_to(kobe_text, DOWN, buff=1)
        
        self.play(Write(inspiration_text))
        self.wait(2)

        pick_basketball_text = Text(
            "Maybe you'll be inspired to pick up a basketball and create your own moments!",
            font_size=28
        ).next_to(inspiration_text, DOWN, buff=0.5)

        self.play(Write(pick_basketball_text))
        self.wait(2)

        # End Scene
        self.play(FadeOut(title), FadeOut(jordan_text), FadeOut(lebron_text), FadeOut(kobe_text), 
                  FadeOut(jordan_highlight), FadeOut(lebron_highlight), FadeOut(kobe_highlight), 
                  FadeOut(inspiration_text), FadeOut(pick_basketball_text))
        self.wait(1)

    def create_highlight_circle(self, color):
        return Circle(radius=1, color=color).shift(LEFT * 3)

