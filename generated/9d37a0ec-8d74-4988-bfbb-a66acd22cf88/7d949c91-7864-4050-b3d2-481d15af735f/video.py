from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Basics of Matrix Algebra", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # List of topics covered
        topics = [
            "Matrix Addition", 
            "Scalar Multiplication", 
            "Matrix Multiplication", 
            "Identity Matrix", 
            "Inverse Matrix"
        ]
        topics_text = VGroup(
            *[Text(topic, font_size=32) for topic in topics]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(topics_text))
        self.wait(2)

        # Applications
        applications_title = Text("Applications of Matrices", font_size=36).next_to(topics_text, DOWN, buff=1)
        self.play(Write(applications_title))
        self.wait(1)

        applications = [
            "Computer Graphics", 
            "Solving Systems of Equations"
        ]
        applications_text = VGroup(
            *[Text(app, font_size=32) for app in applications]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(applications_title, DOWN, buff=0.5)
        
        self.play(FadeIn(applications_text))
        self.wait(2)

        # Keep Practicing
        keep_practicing_text = Text("Keep Practicing!", font_size=36, color=BLUE).next_to(applications_text, DOWN, buff=1)
        self.play(Write(keep_practicing_text))
        self.wait(2)

        # Thanks and see you in the next lesson
        thanks_text = Text("Thanks for joining me today,", font_size=36)
        next_lesson_text = Text("and I can't wait to see you in the next lesson!", font_size=36).next_to(thanks_text, DOWN, buff=0.5)
        final_group = VGroup(thanks_text, next_lesson_text).next_to(keep_practicing_text, DOWN, buff=1)

        self.play(Write(thanks_text), Write(next_lesson_text))
        self.wait(3)