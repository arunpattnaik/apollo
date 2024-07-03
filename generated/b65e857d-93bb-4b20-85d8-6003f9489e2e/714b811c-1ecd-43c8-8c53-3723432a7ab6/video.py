from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Core Concepts of Next.js", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Pages concept
        pages_text = Text("'Pages' in Next.js", font_size=36).next_to(title, DOWN, buff=0.5)
        react_text = Text("In React: Use a Router", font_size=32).next_to(pages_text, DOWN, buff=0.5)
        next_text = Text("In Next.js: Every file in 'pages' is a route", font_size=32).next_to(react_text, DOWN, buff=0.5)
        self.play(Write(pages_text))
        self.wait(1)
        self.play(Write(react_text))
        self.wait(1)
        self.play(Write(next_text))
        self.wait(1)

        # Folder structure visualization
        folder_structure = self.create_folder_structure().scale(0.75).next_to(next_text, DOWN, buff=1)
        self.play(FadeIn(folder_structure))
        self.wait(2)

        # Routing example
        example_text = Text("Example: 'about.js' becomes '/about'", font_size=28).next_to(folder_structure, DOWN, buff=0.5)
        self.play(Write(example_text))
        self.wait(2)
        
        # End Scene
        self.play(FadeOut(title), FadeOut(pages_text), FadeOut(react_text), FadeOut(next_text), FadeOut(folder_structure), FadeOut(example_text))
        self.wait(1)

    def create_folder_structure(self):
        folder = VGroup()

        # Main folder
        folder_rect = Rectangle(width=6, height=4, color=WHITE, fill_opacity=0.1)
        folder_text = Text("pages", font_size=24).move_to(folder_rect.get_top() - UP*0.3)
        
        # Subfolders
        index_file = self.create_file("index.js").next_to(folder_rect.get_center(), UP*0.5, aligned_edge=LEFT)
        about_file = self.create_file("about.js").next_to(index_file, DOWN*0.5, aligned_edge=LEFT)
        contact_file = self.create_file("contact.js").next_to(about_file, DOWN*0.5, aligned_edge=LEFT)

        folder.add(folder_rect, folder_text, index_file, about_file, contact_file)
        return folder

    def create_file(self, name):
        file_rect = Rectangle(width=3, height=0.5, color=WHITE, fill_opacity=0.1)
        file_text = Text(name, font_size=24).move_to(file_rect.get_center())
        file_group = VGroup(file_rect, file_text)
        return file_group