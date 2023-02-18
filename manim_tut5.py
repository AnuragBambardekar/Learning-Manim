from manim import *

class Library(Scene):
    def construct(self):

        ax = Axes() # Hover and Click (in VSCode) to see the library function Code

        # plot_line_graph
        plane = NumberPlane(
                    x_range = (0, 7),
                    y_range = (0, 5),
                    x_length = 7,
                    axis_config={"include_numbers": True},
                )
        plane.center()
        line_graph = plane.plot_line_graph(
            x_values = [0, 1.5, 2, 2.8, 4, 6.25],
            y_values = [1, 3, 2.25, 4, 2.5, 1.75],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,
        )
        self.play(Write(plane))

        self.play(Write(line_graph))

        self.play(Write(ax))