from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Components of the Apollo Spacecraft", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Diagram of the Apollo spacecraft
        spacecraft_diagram = self.create_apollo_spacecraft().scale(0.8)
        spacecraft_diagram.to_edge(LEFT, buff=1)
        self.play(DrawBorderThenFill(spacecraft_diagram))
        self.wait(1)
        
        # Labels for the components
        command_module = Text("Command Module", font_size=24, color=YELLOW).next_to(spacecraft_diagram, RIGHT, buff=0.5).shift(UP*2)
        service_module = Text("Service Module", font_size=24, color=BLUE).next_to(spacecraft_diagram, RIGHT, buff=0.5)
        lunar_module = Text("Lunar Module", font_size=24, color=GREEN).next_to(spacecraft_diagram, RIGHT, buff=0.5).shift(DOWN*2)
        
        self.play(Write(command_module))
        self.play(Write(service_module))
        self.play(Write(lunar_module))
        self.wait(2)
        
        # Details for Command Module
        command_details = VGroup(
            Text("Command Module:", font_size=20, color=YELLOW).shift(UP*2.5).to_edge(RIGHT, buff=1),
            Text("- Astronauts lived and worked here", font_size=20).next_to(command_module, DOWN, buff=0.2)
        )
        self.play(Write(command_details))
        self.wait(2)
        
        # Details for Service Module
        service_details = VGroup(
            Text("Service Module:", font_size=20, color=BLUE).next_to(command_details, DOWN, buff=1.5),
            Text("- Provided propulsion", font_size=20).next_to(service_module, DOWN, buff=0.2),
            Text("- Electrical power", font_size=20).next_to(service_module, DOWN, buff=0.5),
            Text("- Storage for consumables", font_size=20).next_to(service_module, DOWN, buff=0.8)
        )
        self.play(Write(service_details))
        self.wait(2)
        
        # Details for Lunar Module
        lunar_details = VGroup(
            Text("Lunar Module:", font_size=20, color=GREEN).next_to(service_details, DOWN, buff=1.5),
            Text("- Descent stage for landing", font_size=20).next_to(lunar_module, DOWN, buff=0.2),
            Text("- Ascent stage for returning", font_size=20).next_to(lunar_module, DOWN, buff=0.5)
        )
        self.play(Write(lunar_details))
        self.wait(2)
        
    def create_apollo_spacecraft(self):
        spacecraft = VGroup()
        
        command_module = Polygon(
            [-1, 2, 0], [1, 2, 0], [1, 1, 0], [-1, 1, 0],
            color=YELLOW, fill_opacity=0.5
        )
        service_module = Polygon(
            [-1, 1, 0], [1, 1, 0], [1, -2, 0], [-1, -2, 0],
            color=BLUE, fill_opacity=0.5
        )
        descent_stage = Polygon(
            [-1.5, -2, 0], [1.5, -2, 0], [1.5, -3, 0], [-1.5, -3, 0],
            color=GREEN, fill_opacity=0.5
        )
        ascent_stage = Polygon(
            [-1, -3, 0], [1, -3, 0], [1, -4, 0], [-1, -4, 0],
            color=GREEN, fill_opacity=0.3
        )

        lunar_module = VGroup(descent_stage, ascent_stage).next_to(service_module, DOWN, buff=0.1)
        
        spacecraft.add(command_module, service_module, lunar_module)
        return spacecraft