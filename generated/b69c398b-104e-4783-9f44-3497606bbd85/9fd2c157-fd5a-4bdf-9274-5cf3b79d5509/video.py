from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Conclusion: GPT-3 vs Claude", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction texts
        intro_texts = [
            "Both OpenAI's GPT and Anthropic's Claude are remarkable.",
            "Each has its own unique strengths."
        ]

        intro_text_mobs = [Text(text, font_size=28).shift(UP * 2 - i * 0.5) for i, text in enumerate(intro_texts)]
        for mob in intro_text_mobs:
            self.play(Write(mob))
            self.wait(1)

        strengths_texts = [
            "GPT-3 excels in creativity and breadth of knowledge.",
            "Claude shines in safety and ethical considerations."
        ]

        strengths_text_mobs = [Text(text, font_size=28).shift(UP * 0.5 - i * 0.5) for i, text in enumerate(strengths_texts)]
        for mob in strengths_text_mobs:
            self.play(Write(mob))
            self.wait(1)

        # Summary chart
        chart_title = Text("Key Feature Comparison", font_size=36).to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(chart_title))
        self.wait(1)

        # Comparison chart
        table = Table(
            [["Model", "GPT-3", "Claude"],
             ["Strength", "Creativity & Knowledge", "Safety & Ethics"],
             ["Weakness", "Can be inaccurate", "More conservative"]],
            include_outer_lines=True
        ).shift(DOWN*1).scale(0.75)
        
        self.play(Create(table))
        self.wait(2)

        # Conclusion texts
        conclusion_texts = [
            "Depending on your needs, you might choose one over the other,",
            "or even use them together to complement each other's strengths."
        ]

        conclusion_text_mobs = [Text(text, font_size=28).shift(DOWN - i * 0.5) for i, text in enumerate(conclusion_texts)]
        for mob in conclusion_text_mobs:
            self.play(Write(mob))
            self.wait(1)

        # Thanks message
        thanks_text = Text("Thanks for joining me on this exploration.\nI hope you now have a deeper understanding\nof these incredible AI language models!", font_size=24).to_edge(DOWN)
        self.play(Write(thanks_text))
        self.wait(3)