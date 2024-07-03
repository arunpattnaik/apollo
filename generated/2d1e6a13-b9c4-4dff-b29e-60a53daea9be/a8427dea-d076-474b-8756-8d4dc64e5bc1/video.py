from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Stocks", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Definition of Stock
        stock_definition = Text(
            "In the context of investing, a stock represents a share in the ownership of a company.", 
            font_size=32, t2c={"stock": YELLOW, "ownership": GREEN, "company": BLUE}
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(stock_definition))
        self.wait(2)

        # Visual of Stock Certificate
        stock_certificate = self.create_stock_certificate().scale(0.6).shift(LEFT*3)
        self.play(FadeIn(stock_certificate))
        self.wait(2)

        # Explanation of owning a stock
        owning_stock = Text(
            "When you own a stock, you own a piece of that company.", 
            font_size=32
        ).next_to(stock_definition, DOWN, buff=0.5)
        self.play(Write(owning_stock))
        self.wait(2)

        # Synonym for stocks
        equities_text = Text(
            "Stocks are also known as equities.", 
            font_size=32, t2c={"equities": YELLOW}
        ).next_to(owning_stock, DOWN, buff=0.5)
        self.play(Write(equities_text))
        self.wait(2)

        # Company Logos
        company_logos = self.create_company_logos().scale(0.5).shift(RIGHT*3)
        self.play(FadeIn(company_logos))
        self.wait(2)

        # Investment Explanation
        investment_explanation = Text(
            "Investing in stocks means you are buying a small part of a company with the hope \n"
            "that the company grows and becomes more valuable over time.",
            font_size=28
        ).next_to(equities_text, DOWN, buff=1)
        self.play(Write(investment_explanation))
        self.wait(3)

    def create_stock_certificate(self):
        certificate = VGroup()
        
        # Certificate outline
        outline = Rectangle(width=6, height=4, color=WHITE)
        # Certificate text
        certificate_text = Text("Stock Ownership", font_size=36, color=YELLOW).move_to(outline.get_center())
        certificate.add(outline, certificate_text)
        return certificate

    def create_company_logos(self):
        logos = VGroup()
        
        # Example Company Logos
        logo1 = Circle(radius=0.5, color=RED, fill_opacity=1).shift(UP)
        text1 = Text("Company A", font_size=24, color=WHITE).move_to(logo1.get_center())
        
        logo2 = Circle(radius=0.5, color=BLUE, fill_opacity=1)
        text2 = Text("Company B", font_size=24, color=WHITE).move_to(logo2.get_center())
        
        logo3 = Circle(radius=0.5, color=GREEN, fill_opacity=1).shift(DOWN)
        text3 = Text("Company C", font_size=24, color=WHITE).move_to(logo3.get_center())
        
        logos.add(VGroup(logo1, text1), VGroup(logo2, text2), VGroup(logo3, text3)).arrange(DOWN, buff=1)
        return logos