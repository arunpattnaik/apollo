from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Social Media Authentication with Firebase", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Explanation
        explanation = Text(
            "Enable providers in Firebase console and use 'signInWithPopup' in your code.",
            font_size=30,
        ).next_to(title, DOWN, buff=0.5).shift(UP*0.5)
        self.play(Write(explanation))
        self.wait(2)

        # Popup explanation
        popup_explanation = Text(
            "This method opens a popup for social media login.",
            font_size=30,
        ).next_to(explanation, DOWN, buff=0.5)
        self.play(Write(popup_explanation))
        self.wait(2)

        # Firebase handles the rest
        firebase_handles = Text(
            "Firebase handles everything securely.",
            font_size=28,
        ).next_to(popup_explanation, DOWN, buff=0.5)
        self.play(Write(firebase_handles))
        self.wait(2)

        # Showing Google sign-in implementation
        code_title = Text("Google Sign-In Implementation", font_size=36, color=BLUE).next_to(firebase_handles, DOWN, buff=1)
        self.play(Write(code_title))
        self.wait(1)

        code_example = Code(
            code="""
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
    
const auth = getAuth();
const provider = new GoogleAuthProvider();

signInWithPopup(auth, provider)
    .then((result) => {
        // User signed in!
        console.log(result.user);
    })
    .catch((error) => {
        // Handle errors here.
        console.error(error);
    });
            """,
            tab_width=4,
            background="window",
            language="javascript",
            font="Monospace",
            font_size=16,
            insert_line_no=False,
        ).scale(0.75).next_to(code_title, DOWN, buff=0.5).to_edge(LEFT)
        
        self.play(FadeIn(code_example))
        self.wait(4)

        # End Scene
        thank_you_text = Text("Thanks for watching! Happy coding!", font_size=36).next_to(code_example, DOWN, buff=1)
        self.play(Write(thank_you_text))
        self.wait(3)