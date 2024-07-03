from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("The Impact and Future of Large Language Models", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Applications
        applications_text = Text("Applications of Language Models", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(applications_text))
        self.wait(1)

        # Examples of applications
        chatbot_text = Text("Chatbots", font_size=28).move_to(UP*1)
        translation_text = Text("Translation Services", font_size=28).next_to(chatbot_text, DOWN, buff=0.5)
        creative_writing_text = Text("Creative Writing", font_size=28).next_to(translation_text, DOWN, buff=0.5)
        self.play(Write(chatbot_text), Write(translation_text), Write(creative_writing_text))
        self.wait(2)

        # Visualization of Models
        applications_group = VGroup(chatbot_text, translation_text, creative_writing_text)
        self.play(applications_group.animate.shift(UP*1.5))

        chatbot_image = self.create_chatbot().to_edge(LEFT)
        translation_image = self.create_translation().next_to(chatbot_image, RIGHT, buff=1)
        creative_writing_image = self.create_creative_writing().to_edge(RIGHT)
        
        self.play(FadeIn(chatbot_image), FadeIn(translation_image), FadeIn(creative_writing_image))
        self.wait(2)

        # Responsibility and Evolution
        responsible_text = Text("Use Responsibly", font_size=32).next_to(applications_group, DOWN, buff=1)
        accuracy_text = Text("More Accurate", font_size=32).next_to(responsible_text, DOWN, buff=0.5)
        fair_text = Text("More Fair", font_size=32).next_to(accuracy_text, DOWN, buff=0.5)
        useful_text = Text("More Useful", font_size=32).next_to(fair_text, DOWN, buff=0.5)
        self.play(Write(responsible_text), Write(accuracy_text), Write(fair_text), Write(useful_text))
        self.wait(2)

        # End Scene
        thanks_text = Text("Thank you for joining me.\nKeep exploring and stay curious!", font_size=36).next_to(useful_text, DOWN, buff=1.5)
        self.play(Write(thanks_text))
        self.wait(3)

        # Clear Scene
        self.play(FadeOut(title), FadeOut(applications_text), FadeOut(applications_group), 
                  FadeOut(chatbot_image), FadeOut(translation_image), FadeOut(creative_writing_image),
                  FadeOut(responsible_text), FadeOut(accuracy_text), FadeOut(fair_text), FadeOut(useful_text),
                  FadeOut(thanks_text))
        self.wait(1)

    def create_chatbot(self):
        chatbot = VGroup()
        
        # Outline of Chatbot
        outline = RoundedRectangle(width=2, height=3, corner_radius=0.5, color=BLUE)
        screen = Rectangle(width=1.8, height=2.5, color=LIGHT_GRAY).move_to(UP*0.3)
        
        # Chat bubble
        bubble = RoundedRectangle(width=1.2, height=0.5, corner_radius=0.2, color=WHITE).set_stroke(BLACK, width=1).move_to(DOWN*0.5)
        chatbot.add(outline, screen, bubble)
        return chatbot

    def create_translation(self):
        translation = VGroup()
        
        # Outline of Translation
        outline = Rectangle(width=3, height=3, color=RED)
        arrows = VGroup(
            Arrow(start=ORIGIN, end=RIGHT, buff=0.1, color=YELLOW),
            Arrow(start=RIGHT, end=ORIGIN, buff=0.1, color=YELLOW),
        ).arrange(RIGHT).move_to(outline.get_center())
        
        translation.add(outline, arrows)
        return translation

    def create_creative_writing(self):
        writing = VGroup()

        # Outline of Book
        outline = Rectangle(width=2, height=2.5, color=WHITE, fill_opacity=1).set_stroke(BLACK, width=1).move_to(UP*0.5)
        text = Text("Once upon a time...", font_size=14).move_to(DOWN*0.5)
        
        writing.add(outline, text)
        return writing
