from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Managing Authenticated Users with Firebase", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction Text
        intro_text = Text("Firebase provides robust tools for user management:", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # List of features
        features_list = VGroup(
            Text("• Get the current user's information", font_size=28),
            Text("• Update user profile", font_size=28),
            Text("• Send password reset emails", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(intro_text, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(features_list))
        self.wait(2)

        # Dashboard and user management features
        dashboard_image = self.create_dashboard().scale(0.8).next_to(features_list, DOWN, buff=1)
        self.play(FadeIn(dashboard_image))
        self.wait(2)

        # Explanation
        explanation_text = Text("Firebase Console - User Management", font_size=28).next_to(dashboard_image, DOWN, buff=0.5)
        self.play(Write(explanation_text))
        self.wait(2)

        # Summary and closing
        summary_text = Text("Easily keep track of users and ensure their information is up-to-date.", font_size=28).next_to(explanation_text, DOWN, buff=0.5)
        self.play(Write(summary_text))
        self.wait(2)

        closing_text = Text("Thanks for watching, and happy coding!", font_size=36).next_to(summary_text, DOWN, buff=1)
        self.play(Write(closing_text))
        self.wait(3)

    def create_dashboard(self):
        dashboard = VGroup()

        # Background rectangle for the dashboard
        background = Rectangle(width=11, height=6, color=BLUE, fill_opacity=0.1)
        
        # Different sections in the dashboard
        sections = VGroup(
            Rectangle(width=10, height=1, color=WHITE).shift(UP*2),
            Rectangle(width=10, height=1, color=WHITE).move_to(ORIGIN),
            Rectangle(width=10, height=1, color=WHITE).shift(DOWN*2)
        )
        
        # Text inside dashboard sections
        sections_text = VGroup(
            Text("User Information", font_size=24, color=YELLOW).move_to(sections[0].get_center()),
            Text("Update Profile", font_size=24, color=GREEN).move_to(sections[1].get_center()),
            Text("Password Reset", font_size=24, color=RED).move_to(sections[2].get_center())
        )
        
        dashboard.add(background, sections, sections_text)
        return dashboard