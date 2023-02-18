from manim import *

class Errors(Scene):
    def construct(self):
        # an immediate feedback
        c = Circle(radius=2)

        # NameError: name 'circle' is not defined
        # self.play(Write(circle))

        # IndentationError: unexpected indent
        #    self.play(Write(c))

        # TypeError: Mobject.__init__() got an unexpected keyword argument 'r'
        # d = Square(r=2)

        # NameError: name 'CreateThenUnCreate' is not defined
        # self.play(CreateThenUnCreate(c))

        self.play(Write(c))