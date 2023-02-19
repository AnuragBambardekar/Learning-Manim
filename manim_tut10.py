from manim import *

class Graphing(Scene):
    def construct(self):

        plane = NumberPlane(
            x_range=[-4,4,2], x_length=7, y_range=[0,16,4], y_length=5
        ).add_coordinates()

        labels = plane.get_axis_labels(
            x_label='x', 
            y_label='f(x)'
            )

        parabola = plane.plot(
            lambda x: x**2, 
            x_range=[-4,4], 
            color=GREEN
            )

        func_label = MathTex(
            "f(x)={x}^{2}"
            ).scale(0.9).next_to(parabola, UR, buff=0.5).set_color(GREEN)


        area = plane.get_riemann_rectangles(graph=parabola, x_range=[-2,3], dx=0.2, stroke_width=0.1, stroke_color=WHITE)

        self.play(DrawBorderThenFill(plane))
        # self.play(Create(parabola))
        self.play(Create(VGroup(labels,parabola, func_label)))
        self.wait()
        self.play(Create(area))
        name = Text("A Parabola").to_edge(UL, buff=0.5)
        self.play(Write(name))
        self.wait()
