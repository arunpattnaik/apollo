from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Basketball Positions", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Court diagram
        court = self.create_court().scale(0.8).shift(DOWN*0.5)
        self.play(FadeIn(court))
        self.wait(1)

        # Positions
        point_guard_pos = self.add_position(court, "Point Guard", 2*UP+2*LEFT, color=BLUE)
        shooting_guard_pos = self.add_position(court, "Shooting Guard", UP+2*LEFT, color=RED)
        small_forward_pos = self.add_position(court, "Small Forward", RIGHT+UP, color=GREEN)
        power_forward_pos = self.add_position(court, "Power Forward", 2*RIGHT, color=PURPLE)
        center_pos = self.add_position(court, "Center", DOWN, color=ORANGE)
        
        positions_dict = {
            "Point Guard": point_guard_pos,
            "Shooting Guard": shooting_guard_pos,
            "Small Forward": small_forward_pos,
            "Power Forward": power_forward_pos,
            "Center": center_pos
        }

        # Descriptions
        descriptions = [
            ("Point Guard", "The 'floor general', directing plays and distributing the ball."),
            ("Shooting Guard", "Typically one of the team's best shooters."),
            ("Small Forward", "Versatile, able to score from inside and outside."),
            ("Power Forward", "Plays close to the basket, involved in rebounding and defense."),
            ("Center", "Usually the tallest player, anchoring the defense and scoring near the hoop.")
        ]

        description_texts = VGroup()
        
        for i, (pos, desc) in enumerate(descriptions):
            pos_text = Text(pos + ":", font_size=24, color=positions_dict[pos].get_color())
            desc_text = Text(desc, font_size=24).next_to(pos_text, RIGHT)
            line = VGroup(pos_text, desc_text).shift(DOWN*2.5 + DOWN*i)
            description_texts.add(line)

        self.play(Write(description_texts), run_time=4)
        self.wait(3)

        # End scene
        self.play(FadeOut(title), FadeOut(court), FadeOut(description_texts))
        self.wait(1)

    def create_court(self):
        # Create a basic basketball court
        court = VGroup()
        
        court_outline = Rectangle(width=6, height=10, color=WHITE)
        half_court_line = Line(start=ORIGIN, end=court_outline.get_top(), color=WHITE)
        center_circle = Circle(radius=0.75, color=WHITE).move_to(ORIGIN)
        hoop = Circle(radius=0.25, color=WHITE).move_to(court_outline.get_top() - DOWN*1)

        court.add(court_outline, half_court_line, center_circle, hoop)
        return court

    def add_position(self, court, position_name, position_offset, color=WHITE):
        position = Dot(color=color).shift(position_offset)
        label = Text(position_name, font_size=24, color=color).next_to(position, direction=position_offset)
        self.play(FadeIn(position), Write(label))
        return position