from manim import *

class Test(Scene):
    def construct(self):
        circ = Circle(radius=2.4, color=RED)
        self.play(Create(circ))