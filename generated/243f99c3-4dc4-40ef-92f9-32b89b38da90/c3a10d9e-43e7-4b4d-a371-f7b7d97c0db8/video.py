from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Structure of a Next.js Project", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text = Text("In a Next.js app, the 'pages' directory is where the magic happens!", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # Visual Representation of Directory Structure
        folder_structure_title = Text("Directory Structure:", font_size=36).to_edge(LEFT).shift(UP*0.5)
        self.play(Write(folder_structure_title))
        self.wait(1)

        # Folder and File Representation
        root_folder = Text("my-next-app", font_size=28, color=BLUE).next_to(folder_structure_title, DOWN, buff=0.5).shift(RIGHT*0.5)
        pages_folder = Text("pages", font_size=24, color=BLUE).next_to(root_folder, DOWN, buff=0.5).shift(RIGHT*0.5)
        index_file = Text("index.js", font_size=20, color=WHITE).next_to(pages_folder, DOWN, buff=0.2).shift(RIGHT*0.5)
        about_file = Text("about.js", font_size=20, color=WHITE).next_to(index_file, DOWN, buff=0.2)

        self.play(Write(root_folder))
        self.play(Write(pages_folder))
        self.play(Write(index_file))
        self.play(Write(about_file))
        self.wait(2)

        # Mapping to URLs
        urls_title = Text("Maps to URLs:", font_size=36).next_to(folder_structure_title, RIGHT, buff=1).align_to(folder_structure_title, UP)
        self.play(Write(urls_title))
        self.wait(1)

        # URL Representation
        index_url = Text("'/': index.js", font_size=24, color=YELLOW).next_to(urls_title, DOWN, buff=0.5).align_to(urls_title, LEFT)
        about_url = Text("'/about': about.js", font_size=24, color=YELLOW).next_to(index_url, DOWN, buff=0.5).align_to(index_url, LEFT)

        self.play(Write(index_url))
        self.play(Write(about_url))
        self.wait(2)

        # Connecting Files to URLs
        index_arrow = Arrow(start=index_file.get_right(), end=index_url.get_left(), buff=0.1, color=WHITE)
        about_arrow = Arrow(start=about_file.get_right(), end=about_url.get_left(), buff=0.1, color=WHITE)

        self.play(GrowArrow(index_arrow))
        self.play(GrowArrow(about_arrow))
        self.wait(2)

        # Summary
        summary = Text("Routing in Next.js is intuitive and easy to manage!", font_size=32).next_to(intro_text, DOWN, buff=1)
        self.play(Write(summary))
        self.wait(3)