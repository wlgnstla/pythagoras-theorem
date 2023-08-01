from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Polygon(
            ORIGIN - 1.8, 3 * RIGHT - 1.8, 3 * RIGHT + 4 * UP - 1.8,
            stroke_width=2,
            fill_opacity=0.2,
            color=BLUE
        )
        
        # Create the side labels
        a_label = Tex("c", color=WHITE)
        a_label.move_to(0.16*UP + 1.2*LEFT)
        b_label = Tex("a", color=WHITE).next_to(triangle, DOWN)
        c_label = Tex("b", color=WHITE).next_to(triangle, RIGHT)

        # Create the equation
        equation = MathTex("a^2 + b^2 = c^2", color=GREEN).scale(1.3)
        equation.move_to(-3 * UP + 0 * RIGHT)

        # Add all elements to the scene

        #this is the text
        text = Tex("My brain every time I walk diagonally:", color=WHITE).scale(1.4)
        self.play(Write(text),run_time=2)
        self.play(FadeOut(text),run_time=2)
        self.play(Create(triangle), run_time=2)
        self.play(Write(a_label), Write(b_label), Write(c_label),run_time=1)
        self.wait(0.5)
        self.play(Write(equation),run_time = 2)
        self.wait(2)
