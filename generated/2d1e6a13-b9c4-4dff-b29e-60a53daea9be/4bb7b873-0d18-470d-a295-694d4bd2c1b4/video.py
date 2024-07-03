from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("How to Start Investing in Stocks", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step 1: Open a brokerage account
        step1_text = Text("Step 1: Open a Brokerage Account", font_size=36).next_to(title, DOWN, buff=0.5)
        self.play(Write(step1_text))
        self.wait(1)

        # List of popular brokerage platforms
        brokerage_text = Text("Popular Online Brokerage Platforms:", font_size=30).next_to(step1_text, DOWN, buff=0.5)
        self.play(Write(brokerage_text))
        self.wait(1)

        broker_list = VGroup(
            Text("1. Broker A", font_size=28),
            Text("2. Broker B", font_size=28),
            Text("3. Broker C", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(brokerage_text, DOWN, buff=0.5).shift(LEFT*2)
        
        self.play(*[Write(broker) for broker in broker_list])
        self.wait(1)

        # Features with checkmarks
        features_list = VGroup(
            Text("Low Fees", font_size=28),
            Text("User-Friendly Interface", font_size=28),
            Text("Educational Resources", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(broker_list, RIGHT, buff=1.5)

        checkmarks = VGroup(
            Text("✔", font_size=36, color=GREEN).next_to(features_list[0], LEFT, buff=0.5),
            Text("✔", font_size=36, color=GREEN).next_to(features_list[1], LEFT, buff=0.5),
            Text("✔", font_size=36, color=GREEN).next_to(features_list[2], LEFT, buff=0.5),
        )
        
        self.play(*[Write(feature) for feature in features_list], *[Write(check) for check in checkmarks])
        self.wait(2)

        # Step 2: Fund your account
        step2_text = Text("Step 2: Fund Your Account", font_size=36).next_to(features_list, DOWN, buff=1.5)
        self.play(Write(step2_text))
        self.wait(1)

        # Transfer money from bank
        transfer_text = Text("Transfer money from your bank account to your brokerage account.", font_size=30).next_to(step2_text, DOWN, buff=0.5)
        self.play(Write(transfer_text))
        self.wait(2)

        # Visual representation of transfer
        bank = self.create_bank_icon().scale(0.5).to_edge(LEFT, buff=2).shift(DOWN*2)
        arrow = Arrow(start=LEFT, end=RIGHT, buff=1, color=BLUE).next_to(bank, RIGHT, buff=0.5)
        broker_account = self.create_broker_account_icon().scale(0.5).next_to(arrow, RIGHT, buff=0.5)
        
        self.play(FadeIn(bank), GrowArrow(arrow), FadeIn(broker_account))
        self.wait(2)

        # End scene
        self.play(FadeOut(title), FadeOut(step1_text), FadeOut(brokerage_text), FadeOut(broker_list),
                  FadeOut(features_list), FadeOut(checkmarks), FadeOut(step2_text), FadeOut(transfer_text),
                  FadeOut(bank), FadeOut(arrow), FadeOut(broker_account))
        self.wait(1)

    def create_bank_icon(self):
        bank = VGroup()
        # Bank icon - simplified house shape
        bank.add(
            Polygon(
                [-1, 1, 0], [1, 1, 0], [1.2, -1, 0], [-1.2, -1, 0],
                color=WHITE, fill_opacity=1, stroke_color=BLACK
            )
        )
        bank.add(
            Polygon(
                [-1.2, -1, 0], [1.2, -1, 0], [0.8, -1.5, 0], [-0.8, -1.5, 0],
                color=WHITE, fill_opacity=1, stroke_color=BLACK
            )
        )
        return bank

    def create_broker_account_icon(self):
        broker_account = VGroup()
        # Broker account icon - simple screen shape
        broker_account.add(
            Rectangle(width=2, height=1.5, color=WHITE, fill_opacity=1, stroke_color=BLACK)
        )
        broker_account.add(
            Rectangle(width=1.8, height=1.3, color=GRAY, fill_opacity=1, stroke_color=BLACK).shift(DOWN*0.15)
        )
        return broker_account