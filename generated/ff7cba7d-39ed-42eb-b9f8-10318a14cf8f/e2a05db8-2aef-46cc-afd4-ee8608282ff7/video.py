from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Basketball Positions and Their Roles", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Team players on the court
        team_text = Text("Each team has five players on the court:", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(team_text))
        self.wait(1)

        # Positions on the court
        positions = ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]
        position_texts = [Text(pos, font_size=28) for pos in positions]
        
        court = Rectangle(width=10, height=6, color=WHITE).shift(DOWN)
        self.play(Create(court))
        
        pg = position_texts[0].move_to(court.get_top() + DOWN)
        sg = position_texts[1].move_to(court.get_top() + DOWN * 2)
        sf = position_texts[2].move_to(court.get_center())
        pf = position_texts[3].move_to(court.get_bottom() + UP * 2)
        center = position_texts[4].move_to(court.get_bottom() + UP)

        self.play(*[Write(pos) for pos in position_texts])
        self.wait(1)

        # Point Guard Role
        pg_role = Text("Point Guard: The 'Floor General'", font_size=28).next_to(court, RIGHT, buff=1)
        pg_responsibility = Text("Directs plays and ensures smooth gameplay.", font_size=24).next_to(pg_role, DOWN, buff=0.5)
        self.play(Write(pg_role))
        self.play(Write(pg_responsibility))
        self.wait(2)

        # Center Role
        center_role = Text("Center: Tallest Player", font_size=28).next_to(pg_responsibility, DOWN, buff=1)
        center_responsibility = Text("Positioned near the basket for blocking shots and grabbing rebounds.", font_size=24).next_to(center_role, DOWN, buff=0.5)
        self.play(Write(center_role))
        self.play(Write(center_responsibility))
        self.wait(2)

        # Strategy appreciation
        strategy_text = Text("Understanding these roles helps appreciate the strategy behind the game.", font_size=28).next_to(center_responsibility, DOWN, buff=1)
        self.play(Write(strategy_text))

        self.wait(3)

        # End Scene
        self.play(FadeOut(title), FadeOut(team_text), FadeOut(court), *[FadeOut(pos) for pos in position_texts], 
                  FadeOut(pg_role), FadeOut(pg_responsibility), FadeOut(center_role), FadeOut(center_responsibility), 
                  FadeOut(strategy_text))
        self.wait(1)