from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Vercel: Deploy and Host Your Web Applications", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Developer writing code on a computer
        dev_computer = self.create_dev_computer().scale(0.8).to_edge(LEFT, buff=1.5)
        self.play(FadeIn(dev_computer))

        # Code Writing Animation
        code_text = Text("""
        function main() {
            console.log("Hello, Vercel!");
        }

        main();
        """, font_size=24, font="Monospace").move_to(dev_computer.get_center() + DOWN * 0.5)
        code_box = SurroundingRectangle(code_text, color=WHITE, buff=0.2)
        self.play(Write(code_text), Create(code_box))
        self.wait(2)

        # Push button to deploy
        push_button = Text("Deploy to Vercel").next_to(dev_computer, RIGHT, buff=1.5)
        push_button_box = SurroundingRectangle(push_button, color=BLUE, buff=0.2)
        self.play(FadeIn(push_button), Create(push_button_box))
        self.wait(1)
        
        # Vercel takes over (Arrow indicating deployment)
        arrow = Arrow(start=push_button.get_right(), end=3*RIGHT, buff=0.1, color=YELLOW)
        vercel_logo = self.create_vercel_logo().scale(0.5).next_to(arrow.get_end(), RIGHT, buff=0.5)
        self.play(GrowArrow(arrow), FadeIn(vercel_logo))
        self.wait(1)
        
        # Code now accessible on the internet (Earth symbol)
        earth = self.create_earth().scale(0.7).next_to(vercel_logo, RIGHT, buff=1)
        self.play(FadeIn(earth))
        self.wait(2)

    def create_dev_computer(self):
        computer_group = VGroup()
        
        # Screen
        screen_outline = Rectangle(width=4, height=2.5, color=WHITE)
        screen_inner = Rectangle(width=3.8, height=2.3, color=BLACK).move_to(screen_outline.get_center())
        computer_group.add(screen_outline, screen_inner)
        
        # Keyboard
        keyboard = Rectangle(width=4, height=0.5, color=WHITE).next_to(screen_outline, DOWN, buff=0.1)
        computer_group.add(keyboard)
        
        return computer_group

    def create_vercel_logo(self):
        vercel_logo = VGroup()
        
        # Vercel's Triangle logo
        triangle = Polygon(np.array([0, 1, 0]),np.array([-1, -1, 0]),np.array([1, -1, 0]), color=WHITE, fill_color=WHITE, fill_opacity=1)
        vercel_logo.add(triangle)
        
        return vercel_logo

    def create_earth(self):
        earth = VGroup()
        
        # Create a simple depiction of Earth
        # Outer Circle
        circle = Circle(radius=1, color=BLUE_A, fill_opacity=1, fill_color=BLUE_D)
        
        # Some 'landmasses' on the Earth
        landmass1 = Polygon(
            np.array([-0.4, 0.2, 0]), 
            np.array([-0.6, 0.6, 0]), 
            np.array([-0.2, 0.8, 0]), 
            np.array([0, 0.5, 0]), 
            color=GREEN, fill_color=GREEN, fill_opacity=1
        )
        
        landmass2 = Polygon(
            np.array([0.1, -0.1, 0]), 
            np.array([0.3, -0.4, 0]), 
            np.array([0.7, -0.2, 0]), 
            np.array([0.6, 0.1, 0]), 
            color=GREEN, fill_color=GREEN, fill_opacity=1
        )
        
        earth.add(circle, landmass1, landmass2)
        
        return earth