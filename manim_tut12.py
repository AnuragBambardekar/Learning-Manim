from manim import *

HOME = "C:\\Users\\anura\\Documents\\VSCode_Workspace\\Learning_Manim"

class SVGs(Scene):
    def construct(self):

        # Adding SVGs and Regular images
        icon = SVGMobject(f"{HOME}\\6god2.svg").scale(3)
        im = ImageMobject(f"{HOME}\\owl.png").scale(0.95).to_edge(UR)
        im2 = ImageMobject(f"{HOME}\\ovo.png").scale(0.3).to_edge(UL)

        self.play(DrawBorderThenFill(icon)) #only works on vectorized objects
        self.play(FadeIn(im, im2)) # to render PNGs, JPEGs
        self.wait()