from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Vercel: Your Magical Bridge to the Internet", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Description of Vercel
        description_text = Text("Seamless, efficient, and collaborative deployment", font_size=32).next_to(title, DOWN, buff=0.75)
        self.play(Write(description_text))
        self.wait(2)
        
        # Illustration of the individual developer
        solo_dev = Text("Solo Developer", font_size=28, color=BLUE).shift(LEFT*3 + UP*1)
        solo_dev_idea = Star(color=YELLOW, fill_opacity=1).scale(0.5).next_to(solo_dev, DOWN, buff=0.5)      
        self.play(Write(solo_dev))
        self.play(FadeIn(solo_dev_idea))
        self.wait(1)
        
        # Illustration of the team
        team = Text("Large Development Team", font_size=28, color=GREEN).shift(RIGHT*3 + UP*1)
        team_member_1 = Circle(radius=0.3, color=RED).next_to(team, LEFT, buff=0.4)
        team_member_2 = Circle(radius=0.3, color=RED).next_to(team, RIGHT, buff=0.4)
        self.play(Write(team))
        self.play(FadeIn(team_member_1), FadeIn(team_member_2))
        self.wait(1)

        # Vercel = Magical Bridge
        bridge = Text("Vercel: The Magical Bridge", font_size=32, color=PURPLE).shift(DOWN*1.5)
        self.play(Write(bridge))
        self.wait(2)

        self.play(
            Create(Line(UP*1.75 + LEFT*3, bridge.get_center(), color=WHITE).set_stroke(width=4)),
            Create(Line(UP*1.75 + RIGHT*3, bridge.get_center(), color=WHITE).set_stroke(width=4)),
        )
        self.wait(2)

        # Concluding Thanks
        thanks_text = Text("Thanks for joining me today!", font_size=36).next_to(bridge, DOWN, buff=1)
        self.play(Write(thanks_text))
        self.wait(3)