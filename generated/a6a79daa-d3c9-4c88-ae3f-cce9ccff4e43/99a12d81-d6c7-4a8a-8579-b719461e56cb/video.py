from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Defense Strategies in Basketball", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to Defense Strategies
        defense_intro = Text("Common Defensive Strategies", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(defense_intro))
        self.wait(1)

        # Man-to-Man Defense
        man_to_man_text = Text("Man-to-Man Defense", font_size=28).next_to(defense_intro, DOWN, buff=0.5)
        self.play(Write(man_to_man_text))
        self.wait(1)

        court = self.create_basketball_court().scale(0.8).shift(DOWN * 2)
        self.play(FadeIn(court))
        self.wait(1)

        players_man = self.create_players(m2m=True).move_to(court.get_center())
        self.play(FadeIn(players_man))
        self.wait(2)

        # Transition to Zone Defense
        zone_defense_text = Text("Zone Defense", font_size=28).next_to(man_to_man_text, DOWN, buff=0.5)
        self.play(Transform(man_to_man_text, zone_defense_text))
        self.wait(1)

        players_zone = self.create_players(m2m=False).move_to(court.get_center())
        self.play(Transform(players_man, players_zone))
        self.wait(2)

        # Turnovers
        turnovers_text = Text("Creating Turnovers", font_size=28).next_to(zone_defense_text, DOWN, buff=0.5)
        steals_text = Text("Steals", font_size=24).next_to(turnovers_text, DOWN, buff=0.5).align_to(turnovers_text, LEFT)
        blocks_text = Text("Blocks", font_size=24).next_to(steals_text, DOWN, buff=0.2).align_to(turnovers_text, LEFT)
        mistakes_text = Text("Forcing Mistakes", font_size=24).next_to(blocks_text, DOWN, buff=0.2).align_to(turnovers_text, LEFT)

        self.play(Write(turnovers_text))
        self.wait(1)
        self.play(Write(steals_text))
        self.wait(1)
        self.play(Write(blocks_text))
        self.wait(1)
        self.play(Write(mistakes_text))
        self.wait(3)

    def create_basketball_court(self):
        court = VGroup()
        outer_box = Rectangle(width=6, height=10, color=WHITE)
        half_court_line = Line(outer_box.get_top(), outer_box.get_bottom(), color=WHITE)
        center_circle = Circle(radius=1, color=WHITE).move_to(outer_box.get_center())

        court.add(outer_box, half_court_line, center_circle)
        return court

    def create_players(self, m2m=True):
        team_a_color = BLUE
        team_b_color = RED

        if m2m:
            team_a_positions = [([-2, 4, 0]), ([-2, 2, 0]), ([-2, 0, 0]), ([-2, -2, 0]), ([-2, -4, 0])]
            team_b_positions = [([2, 4, 0]), ([2, 2, 0]), ([2, 0, 0]), ([2, -2, 0]), ([2, -4, 0])]
        else:
            team_a_positions = [([-2, 4, 0]), ([-2, -4, 0]), ([-3, 0, 0]), ([-1, 2, 0]), ([-1, -2, 0])]
            team_b_positions = [([2, 4, 0]), ([2, -4, 0]), ([3, 0, 0]), ([1, 2, 0]), ([1, -2, 0])]

        team_a_players = VGroup(*[Dot(point=pos, color=team_a_color) for pos in team_a_positions])
        team_b_players = VGroup(*[Dot(point=pos, color=team_b_color) for pos in team_b_positions])
        return VGroup(team_a_players, team_b_players)