from manim import *

class Getters(Scene):
    def construct(self):

        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
        circ = Circle().to_edge(DOWN)
        arrow = always_redraw(
            lambda: Line(
                    start=rect.get_bottom(), end=circ.get_top(), buff=0.2
                ).add_tip()
        )  # buff to not make it touch circle/ padding
        # always_redraw so that it moves along with the rectangle

        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait()

        self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4)
