from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Firebase Authentication Simplified", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Firebase Auth Introduction
        intro_text = Text(
            "Firebase Auth supports various methods like Email, Phone, and third-party providers.",
            font_size=32
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Scenario: Email Sign-Up
        email_scenario_text = Text(
            "Example: Email Sign-Up Process",
            font_size=36
        ).next_to(intro_text, DOWN, buff=0.75)
        self.play(Write(email_scenario_text))
        self.wait(1)

        # Flowchart of Email Authentication
        steps, arrows = self.create_email_auth_flowchart()
        flowchart = VGroup(steps, arrows).scale(0.75).next_to(email_scenario_text, DOWN, buff=0.75)
        self.play(FadeIn(flowchart))
        self.wait(3)

        # Explanation of each step
        self.explain_step("Step 1: User Enters Email and Password", steps[0])
        self.explain_step("Step 2: Firebase Sends Verification Email", steps[1])
        self.explain_step("Step 3: User Verifies Email", steps[2])
        self.explain_step("Step 4: Credentials are Securely Stored", steps[3])
        
    def create_email_auth_flowchart(self):
        steps = VGroup()

        step1 = Rectangle(width=6, height=1.5, color=BLUE)
        step1_text = Text("User Enters Email and Password", font_size=24).move_to(step1.get_center())
        steps.add(VGroup(step1, step1_text))

        step2 = Rectangle(width=6, height=1.5, color=GREEN).next_to(step1, DOWN, buff=1)
        step2_text = Text("Firebase Sends Verification Email", font_size=24).move_to(step2.get_center())
        steps.add(VGroup(step2, step2_text))

        step3 = Rectangle(width=6, height=1.5, color=YELLOW).next_to(step2, DOWN, buff=1)
        step3_text = Text("User Verifies Email", font_size=24).move_to(step3.get_center())
        steps.add(VGroup(step3, step3_text))
        
        step4 = Rectangle(width=6, height=1.5, color=ORANGE).next_to(step3, DOWN, buff=1)
        step4_text = Text("Credentials are Securely Stored", font_size=24).move_to(step4.get_center())
        steps.add(VGroup(step4, step4_text))

        arrows = VGroup()
        arrows.add(Arrow(step1.get_bottom(), step2.get_top(), buff=0.1))
        arrows.add(Arrow(step2.get_bottom(), step3.get_top(), buff=0.1))
        arrows.add(Arrow(step3.get_bottom(), step4.get_top(), buff=0.1))

        return steps, arrows

    def explain_step(self, explanation, step_group):
        step_text = step_group[1]
        explanation_text = Text(explanation, font_size=28).next_to(step_group, RIGHT, buff=1)
        self.play(Write(explanation_text), Indicate(step_text))
        self.wait(2)
        self.play(FadeOut(explanation_text))
        self.wait(0.5)