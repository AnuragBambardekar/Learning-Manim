from manim import *

class UpdaterGraphing(Scene):
    def construct(self):
        
        ax = Axes( 
            x_range=[-4,4,1], 
            x_length=10, 
            y_range=[-2,16,4], 
            y_length=5).add_coordinates().set_color(WHITE)

        parabola = ax.plot(
            lambda x: x**2, 
            x_range=[-4,4], 
            color=GREEN
            )

        k = ValueTracker(-4)

        slope = always_redraw(lambda: ax.get_secant_slope_group(
            x=k.get_value(), 
            graph=parabola, 
            dx=0.05, 
            secant_line_color=BLUE, 
            secant_line_length=3))

        pt = always_redraw(lambda: Dot().move_to(ax.c2p(k.get_value())))

        self.add(ax,parabola,slope, pt)
        self.wait()
        self.play(k.animate.set_value(4), run_time=3)