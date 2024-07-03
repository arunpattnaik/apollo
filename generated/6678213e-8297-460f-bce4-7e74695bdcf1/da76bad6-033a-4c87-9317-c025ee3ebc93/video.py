from manim import *

class VideoScene(Scene):
    def construct(self):
        # Title
        title = Text("Integrating Firebase Authentication", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Setting Up Firebase Project
        setup_text = Text("1. Set up Firebase Project", font_size=32).next_to(title, DOWN, buff=0.5)
        self.play(Write(setup_text))
        self.wait(1)

        firebase_console_image = self.create_firebase_console().next_to(setup_text, DOWN, buff=0.5)
        self.play(FadeIn(firebase_console_image))
        self.wait(2)

        # Enabling Authentication Methods
        enable_methods_text = Text("2. Enable Authentication Methods", font_size=32).next_to(firebase_console_image, DOWN, buff=0.5)
        self.play(Write(enable_methods_text))
        self.wait(1)

        method_list = self.create_method_list().next_to(enable_methods_text, DOWN, buff=0.5)
        self.play(FadeIn(method_list))
        self.wait(2)

        # Code Snippet for Sign-Up
        coding_text = Text("3. Start Coding!", font_size=32).next_to(method_list, DOWN, buff=0.5)
        self.play(Write(coding_text))
        self.wait(1)

        code_snippet = self.create_code_snippet().next_to(coding_text, DOWN, buff=0.5)
        self.play(FadeIn(code_snippet))
        self.wait(3)

    def create_firebase_console(self):
        firebase_console = VGroup()
        
        # Mock Firebase console
        outline = Rectangle(width=10, height=6, color=BLUE)
        header = Rectangle(width=9.8, height=0.5, color=GRAY).shift(UP*2.75)
        header_text = Text("Firebase Console", font_size=20, color=WHITE).move_to(header.get_center())
        
        # Authentication method icons
        auth_section = Rectangle(width=9.5, height=5, color=LIGHT_GRAY).shift(DOWN*0.25)
        email_icon = Circle(radius=0.5, color=ORANGE).shift(UP*1.5 + LEFT*3)
        social_icon = Circle(radius=0.5, color=RED).shift(UP*1.5)
        phone_icon = Circle(radius=0.5, color=BLUE).shift(UP*1.5 + RIGHT*3)
        
        firebase_console.add(outline, header, header_text, auth_section, email_icon, social_icon, phone_icon)
        return firebase_console

    def create_method_list(self):
        method_list = VGroup()
        
        # List of authentication methods
        email_text = Text("Email/Password", font_size=28, color=ORANGE).shift(UP*0.75 + LEFT*3)
        social_text = Text("Social Providers", font_size=28, color=RED).shift(UP*0.75)
        phone_text = Text("Phone Authentication", font_size=28, color=BLUE).shift(UP*0.75 + RIGHT*3)
        
        method_list.add(email_text, social_text, phone_text)
        return method_list

    def create_code_snippet(self):
        code_snippet = VGroup()
        
        # Code snippet for sign-up
        code_outline = Rectangle(width=9.5, height=3, color=GRAY)
        code_text = Text(
            "firebase.auth().createUserWithEmailAndPassword(email, password)\n"
            ".then((userCredential) => {\n"
            "  // Signed in\n"
            "  const user = userCredential.user;\n"
            "  console.log('User created:', user);\n"
            "})\n"
            ".catch((error) => {\n"
            "  const errorCode = error.code;\n"
            "  const errorMessage = error.message;\n"
            "  console.error('Error:', errorCode, errorMessage);\n"
            "});",
            font_size=20, 
            stroke_width=0
        ).move_to(code_outline.get_center())
        
        code_snippet.add(code_outline, code_text)
        return code_snippet