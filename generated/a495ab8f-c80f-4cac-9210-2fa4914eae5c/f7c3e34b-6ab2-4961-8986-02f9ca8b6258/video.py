from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("NVIDIA GPUs and Their Power", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to NVIDIA
        intro_text = Text("NVIDIA is well-known for its Graphics Processing Units (GPUs)", font_size=36).shift(UP*2)
        self.play(Write(intro_text))
        self.wait(2)

        # GPUs are versatile
        versatile_text = Text("These GPUs are incredibly versatile", font_size=36).next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(versatile_text))
        self.wait(2)

        # Backbone of AI and ML
        ai_ml_text = Text("Backbone of many AI and Machine Learning advancements", font_size=36).next_to(versatile_text, DOWN, buff=0.5)
        self.play(Write(ai_ml_text))
        self.wait(2)

        # GPU as multitasker
        multitasker_text = Text("Imagine a GPU as a highly efficient multitasker", font_size=36).next_to(ai_ml_text, DOWN, buff=0.5)
        self.play(Write(multitasker_text))
        self.wait(2)

        # Transition to visual representation
        transition_text = Text("Visual representation of a GPU with multiple cores:", font_size=36).next_to(multitasker_text, DOWN, buff=0.5)
        self.play(Write(transition_text))
        self.wait(2)
        self.play(FadeOut(intro_text), FadeOut(versatile_text), FadeOut(ai_ml_text),
                  FadeOut(multitasker_text), FadeOut(transition_text))

        # Create and display GPU visual
        gpu_visual = self.create_gpu_visual().scale(0.6).to_edge(LEFT, buff=1)
        self.play(FadeIn(gpu_visual))
        self.wait(2)

        # Description of GPU parallelism
        parallelism_text = Text("Multiple cores working in parallel", font_size=36).next_to(gpu_visual, RIGHT, buff=0.5)
        self.play(Write(parallelism_text))
        self.wait(2)

        applications_text = Text("Powerful for tasks: image recognition, NLP, etc.", font_size=36).next_to(parallelism_text, DOWN, buff=0.5)
        self.play(Write(applications_text))
        self.wait(3)
    
    def create_gpu_visual(self):
        gpu = VGroup()

        gpu_body = Rectangle(width=6, height=4, color=WHITE)
        gpu.add(gpu_body)

        # Cores inside GPU
        num_cores_x = 6
        num_cores_y = 4

        core_width = 0.8
        core_height = 0.8
        core_color = BLUE

        for i in range(num_cores_x):
            for j in range(num_cores_y):
                core = Square(side_length=core_width, color=core_color, fill_opacity=0.8)
                x_offset = (i - (num_cores_x - 1) / 2) * (core_width + 0.1)
                y_offset = (j - (num_cores_y - 1) / 2) * (core_height + 0.1)
                core.move_to(gpu_body.get_center() + np.array([x_offset, y_offset, 0]))
                gpu.add(core)

        return gpu