from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Comparing GPT-3 and Claude in Practice", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text = Text("Let's look at a few examples.", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # Ask both models to write a story
        story_request_text = Text("Ask both models to write a story:", font_size=32).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(story_request_text))
        self.wait(1)

        # GPT-3's response
        gpt3_title = Text("GPT-3's Story:", font_size=28).to_edge(LEFT).shift(DOWN*1)
        gpt3_story = Text("Once upon a time, in a land far, far away...", font_size=24).next_to(gpt3_title, DOWN, buff=0.3).scale(0.7)
        self.play(Write(gpt3_title), Write(gpt3_story))
        self.wait(2)

        # Claude's response
        claude_title = Text("Claude's Story:", font_size=28).to_edge(RIGHT).shift(DOWN*1)
        claude_story = Text("In a distant land, there lived a community that valued kindness...", font_size=24).next_to(claude_title, DOWN, buff=0.3).scale(0.7)
        self.play(Write(claude_title), Write(claude_story))
        self.wait(2)

        # Highlighting differences
        gpt3_highlight = SurroundingRectangle(gpt3_story, color=YELLOW)
        claude_highlight = SurroundingRectangle(claude_story, color=GREEN)
        self.play(Create(gpt3_highlight), Create(claude_highlight))
        self.wait(2)
        
        # Comparing approaches
        compare_text = Text("Highlighting Different Approaches:", font_size=32).next_to(story_request_text, DOWN, buff=1.5)
        self.play(Write(compare_text))
        self.wait(1)

        # GPT-3's Approach
        gpt3_approach = Text("Highly creative and imaginative.", font_size=24, color=YELLOW).next_to(gpt3_highlight, DOWN, buff=0.3)
        self.play(Write(gpt3_approach))
        self.wait(2)

        # Claude's Approach
        claude_approach = Text("Focuses on ethical storytelling.", font_size=24, color=GREEN).next_to(claude_highlight, DOWN, buff=0.3)
        self.play(Write(claude_approach))
        self.wait(2)

        # End Scene
        end_text = Text("Both models offer unique strengths!",
                        font_size=36).next_to(compare_text, DOWN, buff=1.5)
        self.play(Write(end_text))
        self.wait(3)