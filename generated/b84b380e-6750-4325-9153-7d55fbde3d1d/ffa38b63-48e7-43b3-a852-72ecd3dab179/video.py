from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Vercel Instant Previews", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Developer making changes
        dev_text = Text("Developer makes changes...").to_edge(LEFT).shift(DOWN*1.5)
        self.play(Write(dev_text))
        self.wait(1)

        code_changes = Text("git push origin feature/new-feature", font_size=20, color=YELLOW).next_to(dev_text, DOWN, buff=0.5)
        self.play(Write(code_changes))
        self.wait(1)

        # Preview URL generation
        url_gen_text = Text("Generating preview URL...").to_edge(RIGHT).shift(UP*1)
        self.play(Write(url_gen_text))
        self.wait(1)

        preview_url = Text("https://preview.vercel.app/feature/new-feature", font_size=20, color=BLUE).next_to(url_gen_text, DOWN, buff=0.5)
        self.play(Write(preview_url))
        self.wait(1)

        # Showing URL to the team
        view_changes_text = Text("Team views changes in real-time:", font_size=32).next_to(title, DOWN, buff=1)
        self.play(Write(view_changes_text))
        self.wait(1)

        preview_browser = self.create_browser("https://preview.vercel.app/feature/new-feature").next_to(view_changes_text, DOWN, buff=0.8)
        self.play(FadeIn(preview_browser))
        self.wait(2)

        # Ending message
        ending_message = Text("It's like having a crystal ball!", font_size=36).next_to(view_changes_text, DOWN, buff=5)
        self.play(Write(ending_message))
        self.wait(3)

    def create_browser(self, url_text):
        browser = VGroup()
        
        # Browser window outline
        outline = Rectangle(width=10, height=6, color=WHITE)
        address_bar = Rectangle(width=9.5, height=0.5, color=BLUE).shift(UP*2.3)
        
        # Address bar elements
        address_text = Text(url_text, font_size=20, color=WHITE).move_to(address_bar.get_center())
        
        # Visualization of a page
        page_content = Rectangle(width=9.5, height=4.5, color=LIGHT_GRAY).shift(DOWN*0.75)
        feature_text = Text("New Feature Preview", font_size=24, color=BLACK).move_to(page_content.get_center())
        
        browser.add(outline, address_bar, address_text, page_content, feature_text)
        return browser