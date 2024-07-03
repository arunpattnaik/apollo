from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Next.js: API Routes", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Explanation
        explanation = Text(
            "Next.js allows you to create API endpoints\nwithin the same project.", 
            font_size=32, line_spacing=1
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)
        
        # Show directory
        directory_structure = VGroup(
            Text('project/', font_size=28, color=GREEN_B),
            Text('├── pages/', font_size=28, color=GREEN_B).shift(DOWN * 0.5),
            Text('│   ├── index.js', font_size=28).shift(DOWN * 1.0),
            Text('│   ├── about.js', font_size=28).shift(DOWN * 1.5),
            Text('│   ├── api/', font_size=28, color=GREEN_B).shift(DOWN * 2.0),
            Text('│   │   ├── hello.js', font_size=28).shift(DOWN * 2.5),
        ).to_edge(LEFT, buff=1)

        self.play(FadeIn(directory_structure))
        self.wait(2)
        
        # Highlight api directory
        api_highlight = SurroundingRectangle(directory_structure[-2:], color=BLUE, buff=0.2)
        self.play(Create(api_highlight))
        self.wait(1)
        
        # API code example
        api_code_example = Code(
            code=(
                "export default function handler(req, res) {\n"
                "  res.status(200).json({ message: 'Hello, world!' })\n"
                "}\n"
            ),
            tab_width=4,
            background="window",
            language="javascript",
            font="Monospace",
            font_size=24
        ).scale(0.7).to_edge(RIGHT, buff=1)

        self.play(FadeIn(api_code_example))
        self.wait(1)
        
        example_integration = Text(
            "This is perfect for handling form submissions, fetching data, \nor any other server-side logic.",
            font_size=28,
            line_spacing=1
        ).next_to(explanation, DOWN, buff=1)
        
        self.play(Write(example_integration))
        self.wait(3)

        # Highlight the chosen integration
        example_usage = Text(
            "Example: Handling Form Submission",
            font_size=28,
            line_spacing=1,
            color=YELLOW
        ).next_to(api_code_example, DOWN, buff=1)

        self.play(Write(example_usage))
        self.wait(3)