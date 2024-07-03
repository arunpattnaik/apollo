from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Exploring API Routes in Next.js", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text
        intro_text = Text("In Next.js, API endpoints are created by adding files to 'pages/api'.", font_size=28).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)

        # File structure visualization
        file_structure = VGroup(
            Text("pages", font_size=28).align_on_border(LEFT).shift(UP*0.5 + LEFT*4),
            Text("api", font_size=28).next_to(Text("pages", font_size=28), DOWN, aligned_edge=LEFT),
            Text("hello.js", font_size=28).next_to(Text("api", font_size=28), DOWN, aligned_edge=LEFT)
        )
        self.play(Write(file_structure[0]))
        self.play(Write(file_structure[1]))
        self.play(Write(file_structure[2]))
        self.wait(2)

        # Text for endpoint accessibility
        endpoint_text = Text("'pages/api/hello.js' -> accessible at '/api/hello'", font_size=28).next_to(file_structure, RIGHT, buff=1)
        self.play(Write(endpoint_text))
        self.wait(2)

        # Simple API route example text
        api_route_text = Text("Example API Route that returns JSON:", font_size=28).next_to(endpoint_text, DOWN, buff=1)
        self.play(Write(api_route_text))
        self.wait(2)

        # Example API route code box
        api_code = """
        // pages/api/hello.js
        export default function handler(req, res) {
          res.status(200).json({ message: 'Hello, world!' });
        }
        """
        code_box = Code(code=api_code, language='javascript', font_size=20, background="rectangle").next_to(api_route_text, DOWN)
        self.play(Write(code_box))
        self.wait(3)

        # Highlighting the integration aspect
        integration_text = Text("Integration of frontend and backend in one project is a game-changer!", font_size=28).next_to(code_box, DOWN, buff=1)
        self.play(Write(integration_text))
        self.wait(3)

        # End scene
        thanks_text = Text("Thank you for exploring with us!", font_size=36).next_to(integration_text, DOWN, buff=1)
        self.play(Write(thanks_text))
        self.wait(3)