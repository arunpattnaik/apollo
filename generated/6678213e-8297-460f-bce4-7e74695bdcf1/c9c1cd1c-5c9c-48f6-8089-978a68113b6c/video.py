from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Firebase Authentication", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Scenario introduction
        intro_text = Text("Imagine you have a fantastic app idea,", font_size=36).shift(UP*2)
        bouncer_text = Text("Firebase Auth is like a bouncer for your app,", font_size=36).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)
        self.play(Write(bouncer_text))
        self.wait(2)

        # Firebase Authentication Explanation
        explanation_text = Text("Making sure only the right users get in.", font_size=36).shift(DOWN*0.5)
        power_text = Text("Firebase Authentication is secure and efficient.", font_size=36).next_to(explanation_text, DOWN, buff=0.5)
        self.play(Write(explanation_text))
        self.wait(1)
        self.play(Write(power_text))
        self.wait(2)

        # App Diagram
        app_diagram = self.create_app_diagram().scale(0.8).shift(DOWN*1.5)
        self.play(FadeIn(app_diagram))
        self.wait(2)

        # End Scene
        self.play(FadeOut(title), FadeOut(intro_text), FadeOut(bouncer_text), FadeOut(explanation_text), FadeOut(power_text), FadeOut(app_diagram))
        self.wait(1)

    def create_app_diagram(self):
        app_diagram = VGroup()

        # Phone outline representing the app
        phone_outline = RoundedRectangle(corner_radius=0.5, height=5, width=2.5, color=BLUE).shift(LEFT*3)
        screen = RoundedRectangle(corner_radius=0.5, height=4.5, width=2, color=BLUE).shift(LEFT*3)
        
        # User login fields
        email_field = Rectangle(height=0.5, width=1.5, color=WHITE).move_to(screen.get_center() + UP)
        password_field = Rectangle(height=0.5, width=1.5, color=WHITE).move_to(screen.get_center())
        login_button = RoundedRectangle(corner_radius=0.25, height=0.5, width=1.5, color=GREEN).move_to(screen.get_center() + DOWN)

        email_text = Text("Email", font_size=18, color=BLACK).move_to(email_field.get_center())
        password_text = Text("Password", font_size=18, color=BLACK).move_to(password_field.get_center())
        login_text = Text("Login", font_size=18, color=WHITE).move_to(login_button.get_center())
        
        # Database block
        db_block = Rectangle(height=2, width=3, color=BLUE).shift(RIGHT*3)
        db_text = Text("Firebase Auth", font_size=24, color=WHITE).move_to(db_block.get_center())
        
        # Arrows
        arrow_left_to_right = Arrow(start=phone_outline.get_right(), end=db_block.get_left(), buff=0.5, color=YELLOW)
        arrow_label = Text("Auth Request", font_size=18, color=YELLOW).next_to(arrow_left_to_right, UP)

        # Group elements
        app_diagram.add(phone_outline, screen, email_field, password_field, login_button, email_text, password_text, login_text, db_block, db_text, arrow_left_to_right, arrow_label)
        
        return app_diagram