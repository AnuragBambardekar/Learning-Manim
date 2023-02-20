from manim import *

class SimpleText(Scene):
    def construct(self):
        text = Text("Bamba")
        # self.add(text) # Static Text displayed on Screen
        # self.remove(text)

        # self.play(Write(text), run_time=4) # Text written L->R
        # self.remove(text)

        # self.play(AddTextLetterByLetter(text), run_time=4) # Add text letter by letter
        # self.remove(text)

        # self.play(Create(text), run_time=4)
        # self.play(Uncreate(text), run_time=4)

        # self.play(DrawBorderThenFill(text), run_time=4)
        # self.remove(text)

        # self.play(GrowFromCenter(text))
        # self.play(ShrinkToCenter(text))

        self.play(FadeIn(text))
        self.play(FadeOut(text))

        self.wait()
        