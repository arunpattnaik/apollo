from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("The Fascinating World of AGI", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Intro Text
        intro_text = Text("Artificial General Intelligence (AGI) aims to make machines super-smart like humans.", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)
        
        # Robot Interacting
        agi_text = Text("An AGI Robot", font_size=32).shift(UP*2.5)
        self.play(Write(agi_text))
        
        # Chess
        chess_image = self.create_chess_scene().scale(0.4).to_edge(LEFT, buff=0.5).shift(DOWN)
        self.play(FadeIn(chess_image))
        
        # Cooking
        cooking_image = self.create_cooking_scene().scale(0.4).shift(DOWN)
        self.play(FadeIn(cooking_image))

        # Writing Poetry
        poetry_image = self.create_poetry_scene().scale(0.4).to_edge(RIGHT, buff=0.5).shift(DOWN)
        self.play(FadeIn(poetry_image))
        
        self.wait(2)
        
        # Dream of AGI
        agi_dream_text = Text("This is the dream of AGI:", font_size=36).shift(UP*1.5)
        self.play(Write(agi_dream_text))
        
        agi_capability_text = Text("A single system that can perform any intellectual task that a human can.", font_size=28).next_to(agi_dream_text, DOWN)
        self.play(Write(agi_capability_text))
        
        self.wait(3)
        
        # How to Get There
        how_text = Text("But how do we get there? Let's break it down step by step.", font_size=32).shift(DOWN*2.5)
        self.play(Write(how_text))
        
        self.wait(2)

    def create_chess_scene(self):
        chess_scene = VGroup()
        
        # Chessboard
        chessboard = Square(side_length=3, color=WHITE)
        grid = VGroup()
        for i in range(8):
            for j in range(8):
                square = Square(side_length=0.75, color=WHITE if (i+j) % 2 == 0 else BLACK, fill_opacity=0.8)
                square.move_to(chessboard.get_center() + np.array([(i-3.5) * 0.75, (j-3.5) * 0.75, 0]))
                grid.add(square)
        chess_piece1 = Circle(radius=0.35, fill_color=RED, fill_opacity=1).move_to(grid[10].get_center())
        chess_piece2 = Circle(radius=0.35, fill_color=RED, fill_opacity=1).move_to(grid[20].get_center())
        
        chess_scene.add(chessboard, grid, chess_piece1, chess_piece2)
        return chess_scene

    def create_cooking_scene(self):
        cooking_scene = VGroup()
        
        # Cooking Objects (Simplified)
        table = Rectangle(width=3, height=1, color=WHITE).shift(DOWN*0.5)
        stove = Rectangle(width=1.5, height=1, color=DARK_GREY).shift(UP*0.5)
        pot = Ellipse(width=1, height=0.5, color=GRAY).move_to(stove.get_center())
        
        cooking_scene.add(table, stove, pot)
        return cooking_scene

    def create_poetry_scene(self):
        poetry_scene = VGroup()
        
        # Poetry Book and Feather Pen
        book = Rectangle(width=2, height=3, color=WHITE).shift(UP*0.5)
        book_line = Line(start=book.get_bottom(), end=book.get_top(), color=WHITE)
        feather = VGroup(
            Circle(radius=0.1, color=WHITE), 
            Line(start=[-0.1, 0, 0], end=[-0.5, 0.5, 0], color=WHITE),
            Line(start=[0.1, 0, 0], end=[0.5, 0.5, 0], color=WHITE)
        ).move_to(book.get_center()).shift(DOWN*1.5)
        
        poetry_scene.add(book, book_line, feather)
        return poetry_scene