# Attempting to make the Deathly Hallows Symbol from Harry Potter
from manim import *

config.background_color = WHITE

class TriangleExample(Scene):
    def construct(self):
        # triangle_1 = Triangle()
        # triangle_2 = Triangle().scale(2).rotate(60*DEGREES)
        # tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
        # self.add(tri_group)

        outside_triangle = Triangle().scale(4).set_color(BLACK).set_style(stroke_width=20)
        # self.add(outside_triangle)

        inscribed_circle = Circle(radius=2).set_y(-0.75).set_color(BLACK).set_style(stroke_width=20)
        # to_edge takes it to left side edge
        # to_corner takes it to bottom left
        # self.add(inscribed_circle)

        inscribed_line = Line(
                    start=outside_triangle.get_bottom(), end=outside_triangle.get_top()
                ).set_color(BLACK).set_style(stroke_width=20)
        # self.add(inscribed_line)
        
        # self.play(Write(triangle_2))
        # self.wait()

        self.play(Create(VGroup(outside_triangle, inscribed_circle, inscribed_line)), run_time=4)
        self.wait()
