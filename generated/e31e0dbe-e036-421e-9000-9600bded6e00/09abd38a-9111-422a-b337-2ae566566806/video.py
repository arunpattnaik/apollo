from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("How SSR Works in a React Application", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction to SSR in React
        intro_text = Text(
            "Using SSR with React is easy with Next.js", font_size=32
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(1)

        # Next.js Setup Visualization
        setup_title = Text("Simple Next.js Setup", font_size=32).next_to(intro_text, DOWN, buff=0.5)
        nextjs_code = Code(
            code="""
              // pages/index.js
              export default function Home({ data }) {
                return (
                  <div>
                    <h1>Hello, World!</h1>
                    <p>Data: {data}</p>
                  </div>
                );
              }

              export async function getServerSideProps() {
                const res = await fetch('https://api.example.com/data');
                const data = await res.json();
                
                return {
                  props: { data },
                };
              }
            """,
            language="javascript",
            font="Monospace",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=BLUE,
            insert_line_no=False
        ).scale(0.5).next_to(setup_title, DOWN, buff=0.3)

        self.play(Write(setup_title))
        self.play(FadeIn(nextjs_code))
        self.wait(1)

        # Highlight getServerSideProps
        gssp_text = Text("getServerSideProps", font_size=24, color=YELLOW).move_to(
            nextjs_code.get_center() + DOWN*1.5)
        self.play(Write(gssp_text))
        self.wait(2)

        # Explanation of getServerSideProps
        gssp_explanation = Text(
            "This function runs on the server and fetches data before rendering the page.",
            font_size=30,
            color=BLACK
        ).next_to(nextjs_code, DOWN, buff=0.5)

        self.play(Write(gssp_explanation))
        self.wait(3)

        # End Scene
        end_text = Text(
            "React components receive data right away, and the server sends a fully rendered HTML page to the client.",
            font_size=30
        ).next_to(gssp_explanation, DOWN, buff=0.5)
        self.play(Write(end_text))
        self.wait(3)